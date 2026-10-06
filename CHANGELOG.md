# Lemonlight changelog
This is the changelog for [Lemonlight](README.md), a Fabric modpack for our Minecraft server, forked from [Fabulously Optimized](https://www.curseforge.com/minecraft/modpacks/fabulously-optimized).

Only Minecraft 1.21.8 and newer are supported: older history has been removed. The entries below are retained from upstream.
# Chase the Skies (10.x.x)

## 1.21.8

### 10.4.0 (2026-06-09)

Maintenance update! Only the most important changes have been made.

- Added Crash Assistant to help users in case of crashes
- Updated Entity Model Features, Entity Texture Features, BetterGrassify, Controlify, Dynamic FPS, e4mc, Entity Culling, Fabric API, Fabric Language Kotlin, FerriteCore, Forge Config API Port, ImmediatelyFast, LambDynamicLights, Language Reload, Mod Menu, OptiGUI, Puzzle, Skyboxify, YetAnotherConfigLib, Zoomify
- Disabled MC-89146 and MC-199467 in Debugify
- Disabled cape providers that have stopped working
- Updated and enforced Fabric Loader 0.19.3

### 10.3.1 (2025-11-11)

- Updated BetterGrassify, Controlify, Entity Culling, Fabric API, Fabric Language Kotlin, ImmediatelyFast, Iris Shaders, LambDynamicLights, No Chat Reports, Optiboxes, Sodium
  - Freezing issues should now be fixed on Intel GPUs
- Updated translations
- Updated Fabric Loader to 0.17.3

### 10.3.0 (2025-10-05)

- Updated Fabric API, Iris Shaders, LambDynamicLights, Lithium, MoreCulling, Optiboxes, Remove Reloading Screen, Sodium, Sodium Extra, Zoomify
  - Sodium is now on v0.7, meaning various bugfixes and performance improvements. Some of _your_ mods may be incompatible with it for now, in that case keep using v10.2.2.
- Adjusted Remove Reloading Screen to make applying resource packs work in the background again
- Hid two sub-mods from Mod Menu to avoid confusion
- Adjusted Optiboxes MMH text as it now supports options GUI via Mod Menu
- Updated translations in 8 languages

### 10.2.2 (2025-09-20)

- Updated Fabric Language Kotlin, LambDynamicLights, Paginated Advancements
- Updated Spanish, Venezuela translation

### 10.2.1 (2025-09-07)

- Updated Fabric Language Kotlin, Fabric API
- Removed OptiGUI and Polytone workarounds

### 10.2.0 (2025-09-07)

- Removed Polytone - early alpha that isn't officially supported, to be readded when it updates
- OptiGUI currently does not support the latest version of Fabric Language Kotlin, an older version is used
- (Refer to 9.1.0 changelog for other big changes as they were backported before 10.2.0 release)

Changes from beta 6 to stable:

- Removed Polytone - early alpha that isn't officially supported, to be readded when it updates
- Updated Entity Texture Features, Mod Menu, OptiGUI
- Removed Mod Menu workaround as the issue was fixed
- Updated Anglish

### 10.2.0-beta.6 (2025-08-30)

- Updated Fabric API, Forge Config API Port
- Downgraded Fabric Language Kotlin to workaround issues with OptiGUI
- Adjusted mods button position on pause screen to workaround servers that provide custom links
- Adjusted Remove Reloading Screen options to workaround servers that provide a custom resource pack
- Fixed incorrect titles on LAN servers in server list
- Muted speech reminding narrator for translated languages that have not had updates for a while
- Updated translations for 9 languages and the English variants
- Force-enabled: Polytone

### 10.2.0-beta.5 (2025-08-26)

- Updated Entity Model Features, Entity Texture Features, Controlify, Fabric API, Fabric Language Kotlin, LambDynamicLights
- Updated translations for 13 languages
- Slightly adjusted tutorial text, tutorial is now also available on the wiki
- Force-enabled: Polytone

### 10.2.0-beta.4 (2025-08-12)

- Added Optiboxes as an alternative to Nuit (OptiFine skybox support)
- Updated Fabric API
- Updated translations for 11 languages
- Updated EntityCulling on Mod Menu Helper as it now has a GUI config
- Updated and enforced Fabric Loader 0.17.2
- Force-enabled: Polytone

### 10.2.0-beta.3 (2025-08-03)

- Updated LambDynamicLights, ImmediatelyFast, Fabrishot, Fabric API, Capes
- Per user feedback, Better Grass is now disabled by default
  - The mod is not going anywhere, new instances will just have to explicitly turn it on in Video Settings
- Added a first-run guide for new instances
  - This is done by enabling the onboarding accessibility screen again and changing its text
  - First-run narrator speech sentence is muted for translated languages
- Fixed pause menu F9 hint to reflect currently present mod
- Force-enabled: Polytone

### 10.2.0-beta.2 (2025-07-26)

- Readded Polytone
  - According to the developer, it is an early build and not all features may work yet
  - Force-enabled in this case refers to the mod being built for 1.21.7 (usually cross-compatible with 1.21.8 but here not marked as such)
- Updated Debugify, Capes, BetterGrassify
- Force-enabled: Polytone

### 10.2.0-beta.1 (2025-07-18)

- Updated Entity Culling, Forge Config API Port, ImmediatelyFast, Lithium
- Available in CurseForge App again
- Temporarily incompatible: Polytone

### 10.2.0-alpha.1 (2025-07-17)

A new Minecraft version with fixes against game freezing and crashes! Not available on CurseForge due to file rejection (Fabric API not marked as 1.21.8-compatible).

- Updated Fabric API
- Force-enabled: ImmediatelyFast, Lithium, Forge Config API Port
- Temporarily incompatible: Polytone

_The removal of Entity Texture Features and Entity Model Features in this version was not actually done (nor necessary) and as such the changelog has been edited._

## 1.21.7

### 10.1.0-alpha.4 (2025-07-17)

- Readded Continuity
- Updated Capes, Fabric API, ImmediatelyFast
- Temporarily incompatible: Polytone

_The removal of Entity Texture Features and Entity Model Features in this version was not actually done (nor necessary) and as such the changelog has been edited._

### 10.1.0-alpha.3 (2025-07-06)

- Readded Paginated Advancements
- Updated Entity Culling, Fabric API, No Chat Reports
- Hid tr7zw API module from Mod Menu (again)
- Config GUI crashes (edit config file instead!): Capes
- Temporarily incompatible: Continuity, Polytone

### 10.1.0-alpha.2 (2025-07-01)

- Updated Debugify, Forge Config API Port, ImmediatelyFast, Lithium
- Fixed high-resolution screenshot hotkey note being crossed out despite being available
- Config GUI crashes (edit config file instead!): Capes
- Temporarily incompatible: Continuity, Paginated Advancements, Polytone

### 10.1.0-alpha.1 (2025-06-30)

Now with Lava Dennis music disc and a painting of Chicken! Wait a minute...

- Updated Fabric API
- Config GUI crashes (edit config file instead!): Capes
- Force-enabled: ImmediatelyFast, Lithium, Forge Config API Port
- Temporarily incompatible: Continuity, Paginated Advancements, Polytone

## 1.21.6

### 10.0.0-alpha.6 (2025-06-30)

⚠️ Warning: Some crashes, rendering and texture errors were found on 1.21.6. Mojang has released 1.21.7 to fix this, see the FO version above.

- Readded Fabrishot, e4mc, No Chat Reports
- Updated Dynamic FPS, Fabric API, Iris Shaders
- Config GUI crashes (edit config file instead!): Capes
- Temporarily incompatible: Continuity, Paginated Advancements, Polytone

### 10.0.0-alpha.5 (2025-06-25)

- Readded Animatica, Better Mount HUD, FastQuit
- Updated Fabric API, Fabric Language Kotlin, Forge Config API Port, Sodium Extra
- Hid tr7zw API module from Mod Menu
- Config GUI crashes (edit config file instead!): Capes
- Temporarily incompatible: Fabrishot/Bigshot, Continuity, e4mc, No Chat Reports, Paginated Advancements, Polytone

### 10.0.0-alpha.4 (2025-06-21)

- Updated Controlify
  - Fixed crash on Linux
- Config GUI crashes (edit config file instead!): Capes
- Temporarily incompatible: Animatica/MoreMcmeta, Fabrishot/Bigshot, BetterMountHud, Continuity, Enhanced Block Entities, e4mc, FastQuit, ModernFix, No Chat Reports, Paginated Advancements, Polytone

### 10.0.0-alpha.3 (2025-06-21)

- Readded Controlify, Entity Culling, MoreCulling, Reese's Sodium Options, Sodium Extra, Zoomify
- Updated Cloth Config API, Fabric API, ImmediatelyFast, Mod Menu, Remove Reloading Screen
- Config GUI crashes (edit config file instead!): Capes
- Temporarily incompatible: Animatica/MoreMcmeta, Fabrishot/Bigshot, BetterMountHud, Continuity, Enhanced Block Entities, e4mc, FastQuit, ModernFix, No Chat Reports, Paginated Advancements, Polytone

### 10.0.0-alpha.2 (2025-06-18)

- Removed EntityCulling due to crashes
- Config GUI crashes (edit config file instead!): Capes
- Temporarily incompatible: Animatica/MoreMcmeta, Fabrishot/Bigshot, BetterMountHud, Controlify, Continuity, Enhanced Block Entities, e4mc, EntityCulling, FastQuit, ModernFix, MoreCulling, No Chat Reports, Paginated Advancements, Polytone, Reese's Sodium Options, Sodium Extra, Zoomify

### 10.0.0-alpha.1 (2025-06-18)

It's time to Chase the ~~Skies~~ Mods!

Remember that Vibrant Visuals - the official shaders - [are currently only available on Bedrock Edition](<https://www.minecraft.net/en-us/article/vibrant-visuals-java-edition>). When using user-made shaders (Iris), note that vanilla changed the way fog works and shaders must update to work with it.

- Updated Entity Model Features, Entity Texture Features, BetterGrassify, Cloth Config, Dynamic FPS, Fabric API, Forge Config API Port, ImmediatelyFast, Iris Shaders, LambDynamicLights, Language Reload, Lithium, Mod Menu, OptiGUI, Puzzle, Remove Reloading Screen, Sodium, YetAnotherConfigLib
- Config GUI crashes (edit config file instead!): Capes
- Temporarily incompatible: Animatica/MoreMcmeta, Fabrishot/Bigshot, BetterMountHud, Controlify, Continuity, Enhanced Block Entities, e4mc, FastQuit, ModernFix, MoreCulling, No Chat Reports, Paginated Advancements, Polytone, Reese's Sodium Options, Sodium Extra, Zoomify

