<div align="center">

# Lemonlight

A simple Minecraft modpack focusing on performance and graphics enhancements, tailored for our server.

Forked from [Fabulously Optimized](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized).

</div>

## Editions

| Edition | Folder | Includes |
|---|---|---|
| **Lemonlight** (normal) | `Packwiz/<minecraft-version>/` | Performance and graphics base pack |
| **Lemonlight Full** | `Packwiz-Full/<minecraft-version>/` (also `CurseForge/`, `Modrinth/`) | Normal plus extras |

Full adds, on top of normal:

- Shader support (Iris Shaders) - now in both editions
- Controller support (Controlify)
- Open-to-internet play (e4mc)
- Cape mods (Capes / Cape Provider / Better Capes)
- High-res screenshots and replay recording (Fabrishot / Renice Shot, Flashback)
- Better Mount HUD
- Minimaps, AppleSkin, Mouse Tweaks and other HUD/utilities now in both editions (see below)
- Remaining Full-only extras from the Simply Optimized set (26.3): Litematica suite, Jade, Better Advancements/Stats, Not Enough Crashes, inventory/tooltip helpers, cosmetics and TCDCommons

The performance mods from that set (Sodium-family helpers, C2ME, Krypton, VMP, AsyncParticles, BadOptimizations, ScalableLux, `z*` worldgen libs and other `optimization`-tagged mods) are in **both** editions. Server-only ones (ServerCore, structure/worldgen optimizers) install server-side only.

## Supported versions

Only **Minecraft 1.21.8 and newer** are supported (`Packwiz/` folders below 1.21.8 have been removed), including their changelog history ([CHANGELOG](CHANGELOG.md)) and mod table columns ([INCLUDED-MODS](INCLUDED-MODS.md)).

## Download

- **Prism Launcher / MultiMC (auto-update):** use the instances in `MultiMC-Packwiz/` (`Lemonlight (auto-update)` or `Lemonlight Full (auto-update)`). They track the 26.3 pack.
- **Modrinth / CurseForge:** use the files in `Modrinth/` and `CurseForge/` (Full edition).

## Credits

- [Fabulously Optimized](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized) and its contributors for the base pack this fork is built on.
- All developers who made the mods that are, have been and will be in the modpack.
- Everyone who uses, tests and shares the modpack!

## Developer section

### Repo layout

- `Packwiz/<version>/` - Lemonlight (normal) sources: `pack.toml`, `index.toml`, `mods/*.pw.toml`, `config/`, `resourcepacks/`.
- `Packwiz-Full/<version>/` - Lemonlight Full sources, same layout, generated from normal plus extras (see below).
- `CurseForge/` (`manifest.json`) and `Modrinth/` (`modrinth.index.json`) - Full-edition publish files (complete mod set).
- `MultiMC-Packwiz/` - auto-update launcher instances (normal + Full, tracking 26.3).
- `MultiMC/` - static launcher instance template (deprecated upstream, kept for reference).
- `CLI tools/` - maintainer scripts.
- `Resource Packs/` - bundled resource pack sources.
- `INCLUDED-MODS.md` - mod comparison table (1.19+ only).
- `CHANGELOG.md` - changelog (1.19+ history retained from upstream, pre-1.19 removed).

### Normal vs Full

The Full-only mods ("extras") are defined in `FULL_ONLY_STEMS` in [`CLI tools/Build full variant.py`](CLI%20tools/Build%20full%20variant.py):

- `iris`, `irisshaders` - shaders
- `controlify`, `midnightcontrols` - controllers
- `e4mc`, `e4mc_minecraft` - open-to-internet
- `capes`, `cape-provider` - capes
- `fabrishot`, `renice-shot` - hi-res screenshots
- `better-mount-hud`, `bettermounthud` - mount HUD
- everything else that is only in `Packwiz-Full/` (minimaps, Litematica, Jade, Flashback, cosmetics, utilities - merged from the Simply Optimized set for 26.3)

`Packwiz/` (normal) excludes them; `Packwiz-Full/` includes everything.

### Workflows

Update the normal variant first (mods, configs), then re-sync Full:

```sh
python "CLI tools/Build full variant.py" --all
python "CLI tools/Build full variant.py" --version 26.3
```

The script preserves Full-only mods, rebuilds `index.toml` and refreshes the `pack.toml` index hash. See [`CLI tools/README.md`](CLI%20tools/README.md) and [`DEVELOPER-README.md`](DEVELOPER-README.md) for the full maintainer flow.

- Keep the 1.21.8+ only policy: do not re-add version folders older than 1.21.8.
- When adding mods by hand, mirror the Simply Optimized merge: `optimization`/`library` mods go to both editions, everything else Full-only.

### First-release TODOs

- [ ] Replace `YOUR-ORG/lemonlight` in `MultiMC-Packwiz/*/instance.cfg` with the real repo so auto-update resolves.
- [ ] Set the `author` fields (`Packwiz/*/pack.toml`, `CurseForge/manifest.json`) to the server team.
- [ ] Point `Modrinth/` and `CurseForge/` project metadata at the new project pages.
- [ ] Review leftover upstream links (`download.fo`, wiki) in configs and decide what players should see.
- [ ] Decide on translations: `crowdin.yml` and `Resource Packs/` localization still target upstream.
- [ ] Review `.github/workflows/auto-publish.yml` (currently gated on the upstream org).

### License

See [LICENSE](LICENSE.md) (upstream license retained, including attribution requirements).
