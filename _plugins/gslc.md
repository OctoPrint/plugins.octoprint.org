---
layout: plugin

id: gslc
title: GcodeSuperLaserController
description: A plugin for Laser engraving add
author: Skiepp
license: Apache License 2.0

date: 2019-09-05

homepage: https://github.com/Skiepp/GCodeSuperLaserController
source: https://github.com/Skiepp/GCodeSuperLaserController
archive: https://github.com/Skiepp/GC

tags:
- gcode
- laser
- engraver
- marlin

compatibility:

  os:
  - linux
  - raspbian

---

GCodeSuperLaserController
=========================
This is a basic plugin to work with a Laser Engraver.
Printing from the OctoPrint interface with this plugin can turn your 3D printer into a laser engraver!

Commands
--------
- **M3 <p>**:   Turns ON the laser with power <p>
- **M4** / **M5**:  Turn OFF the laser

The laser power can go from 1 (min) to 255 (MAX)
**NOTE:** It's highly suggested to add an [**M400** - Finish Moves](http://marlinfw.org/docs/gcode/M400.html) before the M3 and M4/M5 commands.

How to Use
----------

Step 0) Install the plugin
Step 1) Connect the Laser driver to pins GPIO18 and GND
Step 2) Create a GCode using the described commands
Step 3) Print **using Octoprint**

**Have fun :)**
Oh, almost forgot, I'm not responsible for you hurting yourself with your cool laser, but please use it with caution.
