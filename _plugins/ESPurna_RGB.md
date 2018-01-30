---
layout: plugin

id: ESPurna_RGB
title: Espurna RGB
description: Controll Epurna RGB LED device wirelessly
author: Imon Daneshmand
license: AGPLv3


date: 2018-01-30

homepage: https://github.com/pokeimon/OctoPrint-ESPurnaRGB
source: https://github.com/pokeimon/OctoPrint-ESPurnaRGB
archive: https://github.com/pokeimon/OctoPrint-ESPurnaRGB/archive/master.zip

tags:
- rgb
- rgbw
- rgbww
- led
- conroller
- espurna
- wifi
- wireless
- network

compatibility:
  octoprint:
  - 1.3.1

---

OctoPrint plugin for controling Epurna RGB LED device via REST API over the network using M150 GCODE

        M150: Set Status LED Color - Use R-U-B for R-G-B
        M150 R255       ; Turn LED red
        M150 R255 U127  ; Turn LED orange
        M150            ; Turn LED off
        M150 R U B      ; Turn LED white
