---
layout: plugin

id: SmartABL
title: SmartABL
description: Simple plugin to reduce the number of ABLs triggered.
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
- unified
- marlin
- prusa
- prusa-buddy
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
The plugin reads `ABL_CMD`<sup>1</sup> from your print file and check the bed mesh
in memory<sup>M</sup>.
- If mesh is updated, `M420 S1`<sup>M</sup> is sent in order to load bed mesh from memory.
- If mesh is outdated or doesn't exist, `ABL_CMD` is sent in order to generate a new mesh.
On Marlin, `M500` is also sent to save the mesh on the eeprom.

> <sup>1</sup>: `ABL_CMD` can be `G29` (Marlin/Prusa-buddy), `G80` (Prusa)
> or `BED_MESH_CALIBRATE` (Klipper). This can be customized in SmartABL settings.

> Warning: Prusa and Klipper require at least 1 ABL to track the state.

> Note: By default, the standard ABL command for each firmware triggers SmartABL algorithm,
> however, you can customize this behaviour in settings: the command that triggers the algorithm, the command sent
> to the printer or even ignore commands.

References:
- [G29<sup>M,B</sup>](https://marlinfw.org/docs/gcode/G029.html)
- [M420<sup>M,B</sup>](https://marlinfw.org/docs/gcode/M420.html)
- [M500<sup>M</sup>](https://marlinfw.org/docs/gcode/M500.html)
- [G80<sup>P</sup>](https://reprap.org/wiki/G-code#G80:_Mesh-based_Z_probe)
- [G81<sup>P</sup>](https://reprap.org/wiki/G-code#G81:_Mesh_bed_leveling_status)
- [BED\_MESH\_CALIBRATE<sup>K</sup>](https://www.klipper3d.org/Bed_Mesh.html#calibration)
- [BED\_MESH\_OUTPUT<sup>K</sup>](https://www.klipper3d.org/Bed_Mesh.html#output)


Credits to [Oscar](https://3dprinting.stackexchange.com/a/15953/27154)
for the idea.

## Compatibility
- Marlin (M)
- Prusa (P)
- Prusa-buddy (B)
- Klipper (K)
- Custom*

> *: You can customize the gcode triggering ABL and the gcode sent to the printer
> in settings. Check the setting "Enable SmartABL on unknown firmware" to use not
> detected firmwares.

> Want your firmware to be compatible? Open an Issue on github so we can add it 🙂
>
> Don't forget to upload plugin_SmartABL.log!!

## Configuration
### Commands
- `@SMARTABLRESET`: Send this command by terminal or gcode to zero the counter.

### Settings panel
**GCODES**
- Trigger custom gcode(s): By default, SmartABL only triggers with the standard ABL
commands, i.e. `G29/G80/BED_MESH_CALIBRATE`. However, you can define here
a list of gcodes that can trigger SmartABl, e.g. macros or non-standard commands.
Default: disabled (G29).

- ABL custom gcode(s): By default, SmartABL sends the standard ABL
commands, i.e. `G29/G80/BED_MESH_CALIBRATE`. However, you can define here
a list of gcodes that will be sent instead, e.g. macros or non-standard commands.
Default: disabled (G29).

- Ignore gcode(s): Define here if you want to skip gcodes. The commands defined here
won't be sent to the printer.
Default: disabled.

**Force bed leveling**
- After `#` days. Default: enabled (1).
- After `#` prints. Default: enabled (5).
- If current print bed temperature is different from last print.
Default: enabled.
- If current print hotend temperature is different from last print.
Default: enabled.

**Extras**
- Take into account failed/stopped jobs in prints counter.
Default: disabled (only successful prints increase the counter).
- Enable SmartABL on unknown firmwares.
Default: disabled.
  > You have to enable and configure <code>Trigger custom gcode(s)</code> and
  > <code>ABL custom gcode(s)</code>. If you don't configure these two settings,
  > SmartABL assumes marlin firmware by default (i.e. G29 read from file and
  > G29 send to printer when ABL is needed)

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
