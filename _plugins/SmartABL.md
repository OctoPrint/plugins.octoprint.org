---
layout: plugin

id: SmartABL
title: SmartABL
description: Simple plugin to improve auto bed leveling, adding some conditions in order to minimize the number of ABLs triggered.
authors:
- scmanjarrez
license: AGPLv3

date: 2022-12-29

homepage: https://github.com/scmanjarrez/OctoPrint-SmartABL
source: https://github.com/scmanjarrez/OctoPrint-SmartABL
archive: https://github.com/scmanjarrez/OctoPrint-SmartABL/archive/master.zip

tags:
- abl
- auto bed leveling
- bed level
- bed leveling
- leveling
- bl-touch
- mesh
- probe
- bilinear
- marlin

featuredimage: /assets/img/plugins/SmartABL/settings.png

compatibility:
  octoprint:
  - 1.4.0
  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=3,<4"

---

# SmartABL

## How it works?

The plugin reads `G29*` from ***.gcode** and check the bed mesh
in memory.
- If mesh is updated, `M429 S1` is sent in order to load bed mesh from memory.
- If mesh is outdated or doesn't exist, `G29*` and `M500` are sent in order to
generate a new mesh and save it to eeprom, respectively.
> *: By default, the same ABL command read from your file is sent to the printer.

References:
- [G29](https://marlinfw.org/docs/gcode/G029.html)
- [M420](https://marlinfw.org/docs/gcode/M420.html)
- [M500](https://marlinfw.org/docs/gcode/M500.html)

Credits to [Oscar](https://3dprinting.stackexchange.com/a/15953/27154)
for the idea.

## Configuration

By default, SmartABL **does not change** the behaviour of the
auto bed leveling. User *must* change default values in settings:

### Settings panel

**Leveling command**
- Ignore gcode read from files and send a custom gcode instead.
Default: disabled (G29).

**Force bed leveling**
- After `#` days. Default: disabled (1).
- After `#` prints. Default: disabled (5).
- If current print bed temperature is different from last print.
Default: disabled.
- If current print hotend temperature is different from last print.
Default: disabled.

**Prints counter**
- Take into account failed prints in the counter.
Default: disabled (only successful prints increase the counter).

<div align="center">
    <img alt="Screenshot of SmartABL settings panel" src="/assets/img/plugins/SmartABL/settings.png" width="80%"></img>
</div>

### Side panel

- **ABL Restricted**: Normal behaviour, the plugin chooses when to trigger ABL
based on your settings.

- **ABL Always**: Ignore settings; the plugin always trigger ABL. Handy when you
need to force-update your mesh.

<div align="center">
    <img alt="Screenshot of SmartABL side panel" src="assets/img/plugins/SmartABL/sidepanel.png" width="30%"></img>
</div>

## Support me
You find this plugin helpful and want to support me?

<a href="https://ko-fi.com/Zuzumebachi">
    <img alt="Ko-fi link to support me" src="/assets/img/plugins/SmartABL/kofi_button_red.png" width="25%">
</a>
