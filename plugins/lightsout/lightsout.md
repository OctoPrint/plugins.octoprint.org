---
layout: plugin

id: lightsout
title: OctoPrint-LightsOut
description: Automatically shuts off lights after some delay when printing completes
authors:
- Daniel Miller
license: AGPLv3

date: 2020-11-08

homepage: https://github.com/Peaches491/OctoPrint-LightsOut
source: https://github.com/Peaches491/OctoPrint-LightsOut
archive: https://github.com/Peaches491/OctoPrint-LightsOut/archive/master.zip

tags:
- lights
- timer
- LED
- M150

featuredimage: /assets/img/plugins/lightsout/settings_screenshot.png

compatibility:
  python: ">=2.7,<4"

---

## LightsOut Plugin

Automatically turns out the lights after a set period of time. Automatically
resets the timer when:
 - you use `M150` to turn the lights on manually,
 - a print finishes (completed, stopped, or failed),
 - or the settings are updated
