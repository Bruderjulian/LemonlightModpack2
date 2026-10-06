"""Build/sync the Lemonlight Full variant from the normal (lean) variant.

Layout:
  Packwiz/<mc-version>/        Lemonlight (normal, performance/base only)
  Packwiz-Full/<mc-version>/   Lemonlight Full (normal + extras)

Full-only mods ("extras") are defined in FULL_ONLY_STEMS below. A version
folder may use different file names for the same mod across Minecraft
versions (e.g. "capes" vs "cape-provider"), so matching is done on the
mod file stem (filename without ".pw.toml").

Usage (run from the repository root):
  python "CLI tools/Build full variant.py" --all            # first run: split
  python "CLI tools/Build full variant.py" --all            # later runs: re-sync
  python "CLI tools/Build full variant.py" --version 26.3   # single version

First run (Packwiz-Full/<version> does not exist yet):
  1. Copy Packwiz/<version> to Packwiz-Full/<version> (complete mod set).
  2. Rename the copy to "Lemonlight Full".
  3. Strip the Full-only mods from Packwiz/<version> (the normal variant),
     drop their entries from index.toml and refresh the index hash.
  4. Rename the normal pack to "Lemonlight".

Later runs (Packwiz-Full/<version> already exists):
  1. Remember which mods are Full-only (present in Full, absent in normal).
  2. Re-copy shared files (config, resourcepacks, normal mods, index base)
     from Packwiz/<version> to Packwiz-Full/<version>.
  3. Re-add the Full-only mods and rebuild the Full index.toml + hash.

Only the Python standard library is used.
"""

import argparse
import hashlib
import re
import shutil
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PACKWIZ = REPO_ROOT / "Packwiz"
PACKWIZ_FULL = REPO_ROOT / "Packwiz-Full"

NORMAL_NAME = "Lemonlight"
FULL_NAME = "Lemonlight Full"

# Mod file stems (without ".pw.toml") that are only part of Lemonlight Full.
# Normal = performance/base mods. Full = normal + these extras.
FULL_ONLY_STEMS = {
    # Shader support
    "iris",
    "irisshaders",
    # Controller support
    "controlify",
    "midnightcontrols",
    # Open-to-internet (LAN sharing)
    "e4mc",
    "e4mc_minecraft",
    # Cape mods
    "capes",
    "cape-provider",
    # High-res screenshots
    "fabrishot",
    "renice-shot",
    # Extra HUD
    "better-mount-hud",
    "bettermounthud",
}

ROOT_SHARED_FILES = ["mmc-export.toml", "pre-launch.sh", "pre-launch.ps1",
                     "post-exit.sh", "post-exit.ps1"]


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def set_pack_name(pack_toml: Path, name: str) -> None:
    text = pack_toml.read_text(encoding="utf-8")
    new_text, count = re.subn(r'^name\s*=.*$', f'name = "{name}"',
                              text, count=1, flags=re.MULTILINE)
    if count == 0:
        raise ValueError(f"No name field found in {pack_toml}")
    pack_toml.write_text(new_text, encoding="utf-8")


def refresh_index_hash(pack_toml: Path) -> None:
    """Recompute the [index] hash from the version folder's index.toml."""
    index_toml = pack_toml.parent / "index.toml"
    digest = sha256_file(index_toml)
    text = pack_toml.read_text(encoding="utf-8")
    new_text, count = re.subn(r'^hash\s*=.*$', f'hash = "{digest}"',
                              text, count=1, flags=re.MULTILINE)
    if count == 0:
        raise ValueError(f"No hash field found in {pack_toml}")
    pack_toml.write_text(new_text, encoding="utf-8")


def remove_mods_from_version(version_dir: Path, stems: set) -> list:
    """Delete mods/*.pw.toml files and their index.toml entries. Returns removed stems."""
    mods_dir = version_dir / "mods"
    index_toml = version_dir / "index.toml"
    removed = []
    for stem in sorted(stems):
        mod_file = mods_dir / f"{stem}.pw.toml"
        if mod_file.exists():
            mod_file.unlink()
            removed.append(stem)
    if removed:
        gone = {f'mods/{stem}.pw.toml' for stem in removed}
        text = index_toml.read_text(encoding="utf-8")
        preamble, *blocks = text.split("[[files]]")
        kept = []
        for block in blocks:
            file_lines = [l for l in block.splitlines() if l.startswith("file =")]
            if len(file_lines) == 1 and any(g in file_lines[0] for g in gone):
                continue  # block belongs to a removed mod
            kept.append(block)
        index_toml.write_text(preamble + "[[files]]" + "[[files]]".join(kept),
                              encoding="utf-8")
        refresh_index_hash(version_dir / "pack.toml")
    return removed


def full_only_stems(full_mods: Path, normal_mods: Path) -> set:
    def stems(d: Path) -> set:
        if not d.exists():
            return set()
        return {p.name[:-len(".pw.toml")] if p.name.endswith(".pw.toml") else p.stem
                for p in d.glob("*.pw.toml")}
    return stems(full_mods) - stems(normal_mods)


def init_full_version(version: str) -> None:
    src = PACKWIZ / version
    dst = PACKWIZ_FULL / version
    shutil.copytree(src, dst)
    set_pack_name(dst / "pack.toml", FULL_NAME)
    set_pack_name(src / "pack.toml", NORMAL_NAME)
    removed = remove_mods_from_version(src, FULL_ONLY_STEMS)
    print(f"[{version}] Full created; normal drops: {', '.join(removed) or 'none'}")


def sync_full_version(version: str) -> None:
    src = PACKWIZ / version
    dst = PACKWIZ_FULL / version
    extras = full_only_stems(dst / "mods", src / "mods")
    extra_files = {}
    for stem in extras:
        mod_file = dst / "mods" / f"{stem}.pw.toml"
        if mod_file.exists():
            extra_files[stem] = mod_file.read_bytes()
    shutil.rmtree(dst)
    shutil.copytree(src, dst)
    for stem, data in extra_files.items():
        (dst / "mods" / f"{stem}.pw.toml").write_bytes(data)
    # Rebuild Full index.toml: normal index + entries for extras.
    set_pack_name(dst / "pack.toml", FULL_NAME)
    set_pack_name(src / "pack.toml", NORMAL_NAME)
    if extra_files:
        index_text = (dst / "index.toml").read_text(encoding="utf-8")
        if not index_text.endswith("\n"):
            index_text += "\n"
        for stem in sorted(extra_files):
            pw_text = (dst / "mods" / f"{stem}.pw.toml").read_bytes()
            digest = hashlib.sha256(pw_text).hexdigest()
            index_text += (f'\n[[files]]\nfile = "mods/{stem}.pw.toml"\n'
                           f'hash = "{digest}"\nmetafile = true\n')
        (dst / "index.toml").write_text(index_text, encoding="utf-8")
    refresh_index_hash(dst / "pack.toml")
    print(f"[{version}] Full re-synced; extras kept: {', '.join(sorted(extras)) or 'none'}")


def ensure_root_files() -> None:
    PACKWIZ_FULL.mkdir(exist_ok=True)
    for name in ROOT_SHARED_FILES:
        src = PACKWIZ / name
        if src.exists():
            shutil.copy2(src, PACKWIZ_FULL / name)


def process_version(version: str) -> None:
    if not (PACKWIZ / version / "pack.toml").exists():
        print(f"[{version}] skipped: no Packwiz/{version}/pack.toml", file=sys.stderr)
        return
    if not (PACKWIZ_FULL / version).exists():
        init_full_version(version)
    else:
        sync_full_version(version)


def main() -> None:
    parser = argparse.ArgumentParser(description="Build/sync the Lemonlight Full variant.")
    parser.add_argument("--all", action="store_true", help="Process every version in Packwiz/")
    parser.add_argument("--version", help="Process a single Minecraft version, e.g. 26.3")
    args = parser.parse_args()
    if not args.all and not args.version:
        parser.error("Pass --all or --version <mc-version>.")
    ensure_root_files()
    if args.all:
        versions = sorted(p for p in PACKWIZ.iterdir()
                          if p.is_dir() and (p / "pack.toml").exists())
        for version_dir in versions:
            process_version(version_dir.name)
    else:
        process_version(args.version)


if __name__ == "__main__":
    main()
