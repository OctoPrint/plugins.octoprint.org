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
- prusa
- klipper

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

The plugin reads `ABL_CMD`<sup>1</sup> from ***.gcode** and check the bed mesh
in memory<sup>M</sup>.
- If mesh is updated, `M429 S1`<sup>M</sup> is sent in order to load bed mesh from memory.
- If mesh is outdated or doesn't exist, `ABL_CMD` is sent in order to generate a new mesh.
On Marlin, `M500` is also sent to save the mesh on the eeprom.

> <sup>1</sup>: ABL_CMD can be `G29` (Marlin), `G80` (Prusa) or `BED_MESH_CALIBRATE` (Klipper).

> <sup>M</sup>: Marlin-only compatible.

> Note: Prusa and Klipper require at least 1 ABL to track the state.

> Note: By default, the same ABL command read from your file is sent to the printer, but
> can be customized in SmartABL settings.

References:
- [G29<sup>M</sup>](https://marlinfw.org/docs/gcode/G029.html)
- [M420<sup>M</sup>](https://marlinfw.org/docs/gcode/M420.html)
- [M500<sup>M</sup>](https://marlinfw.org/docs/gcode/M500.html)
- [G80<sup>P</sup>](https://reprap.org/wiki/G-code#G80:_Mesh-based_Z_probe)
- [G81<sup>P</sup>](https://reprap.org/wiki/G-code#G81:_Mesh_bed_leveling_status)
- [BED\_MESH\_CALIBRATE<sup>K</sup>](https://www.klipper3d.org/Bed_Mesh.html#calibration)
- [BED\_MESH\_OUTPUT<sup>K</sup>](https://www.klipper3d.org/Bed_Mesh.html#output)


Credits to [Oscar](https://3dprinting.stackexchange.com/a/15953/27154)
for the idea.

## Compatibility
- Marlin
- Prusa
- Klipper

> Want your firmware to be compatible? Open an Issue on github so we can add compatibility 😊

## Configuration

By default, SmartABL **does not change** the behaviour of the
auto bed leveling. User *must* change default values in settings:

### Settings panel

**Leveling command**
- Ignore gcode read from files and send a custom gcode instead.
Default: disabled (G29).

**Ignore gcodes**
- Skip gcodes listed here.

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
    <img alt="Screenshot of SmartABL settings panel" src="/assets/img/plugins/SmartABL/settings.png" width="90%">
</div>

### Side panel

- **ABL Restricted**: Normal behaviour, the plugin chooses when to trigger ABL
based on your settings.

- **P/FP**: Number of current prints/Number of prints to force ABL.

- **ABL Always**: Ignore settings; the plugin always trigger ABL. Handy when you
need to force-update your mesh.

<div align="center">
    <img alt="Screenshot of SmartABL side panel" src="/assets/img/plugins/SmartABL/sidepanel.png" width="40%">
</div>

## Support me
You find this plugin helpful and want to support me?

<a href="https://ko-fi.com/Zuzumebachi">
    <img alt="Ko-fi link to support me" src="/assets/img/plugins/SmartABL/kofi_button_red.png" width="25%">
</a>
