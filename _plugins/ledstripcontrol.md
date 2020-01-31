---
layout: plugin

id: LEDStripControl
title: LEDStripControl
description: Control RGB LED Strips via your Raspberry Pi and GCode.
author: Uriah Welcome
license: Apache 2

date: 2017-03-10

homepage: https://github.com/google/OctoPrint-LEDStripControl
source: https://github.com/google/OctoPrint-LEDStripControl
archive: https://github.com/google/OctoPrint-LEDStripControl/archive/master.zip

follow_dependency_links: false

tags:
- raspberry pi
- led
- rgb
- gcode
screenshots:
- url: /assets/img/plugins/ledstripcontrol/configuration.png
  alt: Configuration Screen
  caption: Configure GPIOs

compatibility:
  octoprint:
  - 1.3.1
  python: ">=2.7,<4"
---

OctoPrint Plugin that intercepts M150 GCode commands and controls local GPIOs on your Pi.

Implements the M150 command syntax from the latest Marlin.

    M150: Set Status LED Color - Use R-U-B for R-G-B
    M150 R255       ; Turn LED red
    M150 R255 U127  ; Turn LED orange
    M150            ; Turn LED off
    M150 R U B      ; Turn LED white


