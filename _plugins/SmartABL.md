---
layout: plugin

id: SmartABL
title: SmartABL
description: Simple plugin to improve auto bed leveling, adding some conditions in order to minimize the number of ABLs triggered.
authors:
- Sergio C
license: AGPLv3

date: 2022-12-07

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

The plugin replaces `G29` from ***.gcode** and check the bed mesh
in memory.
- If mesh is updated, `M429 S1` is sent in order to load bed mesh from memory.
- If mesh is outdated, `G29` and `M500` are sent in order to
generate a new mesh and save it to eeprom, respectively.

References:
- [G29](https://marlinfw.org/docs/gcode/G029.html)
- [M420](https://marlinfw.org/docs/gcode/M420.html)
- [M500](https://marlinfw.org/docs/gcode/M500.html)

Credits to [Oscar](https://3dprinting.stackexchange.com/a/15953/27154)
for the idea.

## Configuration

By default, SmartABL **does not change** the behaviour of the
auto bed leveling, user input in settings is required:

**Days**
- **force** (disabled): Force bed mesh update if the `after days`
condition is met.
- **after**(1): Days after last print before forcing mesh update.

**Prints**
- **force** (enabled): Force bed mesh update if the `after prints` condition is met.
- **after**(1): Prints completed before forcing mesh update.

**Events**
- **failed** (disabled): Take into account `PrintFailed` events
in the `prints` counter. Otherwise, only `PrintDone` (successful prints)
are taken into account.

<div align="center">
    <img alt="Screenshot of SmartABL settings panel" src="/assets/img/plugins/SmartABL/settings.png" width="90%">
</div>

## Support me
You find this plugin helpful and want to support me?

<a href="https://ko-fi.com/Zuzumebachi">
    <img alt="Ko-fi link to support me" src="/assets/img/plugins/SmartABL/kofi_button_red.png" width="25%">
</a>
