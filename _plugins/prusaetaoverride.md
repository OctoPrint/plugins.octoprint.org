---
layout: plugin

id: prusaetaoverride
title: Slicer M73 ETA override Plugin (Prusa; Marlin 2)
description: Plugin that overrides OctoPrint ETA/progress to values from last M73 gcode response received from printer
author: Anton Skorochod
license: AGPLv3

date: 2019-08-25

homepage: https://github.com/arekm/octopi_eta_override
source: https://github.com/arekm/octopi_eta_override
archive: https://github.com/arekm/octopi_eta_override/archive/master.zip

follow_dependency_links: false

tags:
- progress
- eta
- estimation
- m73
- prusa
- marlin2

compatibility:
  python: ">=2.7,<4"

---

## About
The best ETA in 3d printing is ETA coming from slicer software. Slicer adds M73 commands with estimations of print progress, time, time until next pause etc.

This plugin uses firmware reports issued to serial output and coming from M73 g-code commands. Supported firmware issues M73 Reports for SD-card and USB printing.

Data used by plugin:

* time until end of printing
* time progress reflected in OctoPrint web UI progress bar (but due to OctoPrint limitations not in API, see OctoPrint/OctoPrint#4663)

Also this plugin queries for position (M114) when every M73 command parsing happens and fires z-change event (to support sending status message every X millimeters via telegram).

## Supported firmware
Supported firmware list:

* Prusa Firmware (v3.3.0+)
* Marlin 2 (v2.1.2+)

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.
