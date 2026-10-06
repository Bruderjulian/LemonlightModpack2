# Lemonlight developer notes

Maintainer notes for the Lemonlight modpack (forked from Fabulously Optimized).
For the player-facing overview and the edition/version policy, see [README](README.md).

## What lives where

- `Packwiz/<mc-version>/` - Lemonlight (normal): `pack.toml`, `index.toml`, `mods/*.pw.toml`, `config/`, `resourcepacks/`. One folder per supported Minecraft version (1.19.x and newer only).
- `Packwiz-Full/<mc-version>/` - Lemonlight Full: same layout, normal plus the Full-only extras.
- `CurseForge/manifest.json`, `Modrinth/modrinth.index.json` - Full-edition publish files (complete mod set).
- `MultiMC-Packwiz/` - Prism/MultiMC auto-update instances (normal + Full). Their `instance.cfg` files point at the raw `pack.toml` URLs - update `YOUR-ORG/lemonlight` to the real repo location.
- `MultiMC/` - static instance template (deprecated install method, kept for reference).
- `CLI tools/` - maintainer scripts, see [CLI tools/README](CLI%20tools/README.md).
- `Resource Packs/` - bundled resource pack sources and their localization files.
- `.github/` - issue templates and workflows (partly still reference upstream; see README TODOs).

## Build process

1. Update the normal variant in `Packwiz/<mc-version>/` (mods via packwiz, configs by hand) and test in Prism Launcher/MultiMC.
2. Re-sync the Full variant: `python "CLI tools/Build full variant.py" --all` (or `--version <mc>` for one).
3. Bump versions with `CLI tools/Update version.py`.
4. Export/publish manually to Modrinth/CurseForge from the Full file set.
5. Announce to your players.

Notes:

- As seen in `.gitignore`, no JAR files are committed. Get them via packwiz, Prism Launcher, CurseForge or Modrinth.
- `pack.toml` holds a sha256 of `index.toml` - the build script refreshes it automatically; if you edit `index.toml` by hand, recompute it.
- Keep the 1.19+ only policy: do not re-add version folders older than 1.19.x.
