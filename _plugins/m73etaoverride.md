---
layout: plugin

id: m73etaoverride
title: M73 ETA Override
description: Plugin that overrides OctoPrint ETA to values from last M73 gcode sent to the printer
authors:
- Jakub Furman
- Gaston Dombiak
license: AGPLv3

date: 2018-09-18

homepage: https://github.com/gdombiak/OctoPrint-M73ETAOverride
source: https://github.com/gdombiak/OctoPrint-M73ETAOverride
archive: https://github.com/gdombiak/OctoPrint-M73ETAOverride/archive/master.zip

follow_dependency_links: false

tags:
- progress
- eta
- estimation
- m73

compatibility:
  python: ">=2.7,<4"

---

## About
PrusaSlicer is able to calculate print estimates very accurately. Those estimates get injected into generated gcode as [M73 gcode](https://marlinfw.org/docs/gcode/M073.html) commands. This plugin reads the injected information to override what OctoPrint uses as default to calculate estimates. Improved estimates are displayed in OctoPrint, your printer display and in your favorite OctoPrint client.

This plugin will also work with other slicers that inject M73 gcode commands while slicing your STL files to produce gcode.

## Firmware

Prusa printers will display M73 estimates without any modifications. Printers that run on Marlin firmware might require their firmware to be properly configured to display M73 ETA on the printer display. If you are using Marlin 2.0.x then you will need to:
1. Uncomment #define SHOW_REMAINING_TIME in Configuration_adv.h
1. Uncomment #define USE_M73_REMAINING_TIME in Configuration_adv.h

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.
