---
layout: plugin
id: tobecaplugin
title: Tobeca Plugin
description: Plugin for OctoPrint that add commands.
homepage: https://github.com/tobeca/OctoPrint-TobecaPlugin
source: https://github.com/tobeca/OctoPrint-TobecaPlugin
author: Saymtech
license: AGPLv3
archive: 
date: 2017-02-11
tags:
- printing
compatibility:
  octoprint:
  - 1.2.16
---
Adding a Tobeca (French 3D Printer) tab with commands:

- Autotune PID : Sending the M303 Gcode with selecting tool, temperature  (parameter C=8)
- Z-Probe-Offset : Sending the M851 Gcode with selecting the value
- Home XYZ : Sending the G28 Gcode, because Home Z is harzardous with Z-Probe
                        