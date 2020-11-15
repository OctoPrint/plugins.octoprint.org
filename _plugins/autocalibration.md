---
layout: plugin

id: autocalibration
title: Autocalibration
description: Calibrates your printers backlash for the X, Y or Z-axis.
author: Florens Wasserfall (Platsch)
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2015-11-09

homepage: https://github.com/platsch/OctoPrint-Autocalibration
source: https://github.com/platsch/OctoPrint-Autocalibration
archive: https://github.com/platsch/OctoPrint-Autocalibration/archive/master.zip

# set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false

tags:
- repetier
- calibration
- backlash

screenshots:
- url: /assets/img/plugins/autocalibration/screenshot.png
  alt: Settings dialog of the autocalibration plugin.
  caption: Settings dialog of the autocalibration plugin.

featuredimage: /assets/img/plugins/autocalibration/screenshot.png
---

This plugin calibrates your printers [backlash](https://en.wikipedia.org/wiki/Backlash_%28engineering%29) for the X, Y or Z-axis.

## How does it work?

Make sure your printer is running and connected to OctoPrint before you start the calibration process. The axis moves to home to find the endstop and then slowly away from the endstop to find the point where the backlash is compensated by the moving pulley. Do not interrupt the process, otherwise the backlash would remain 0 regardless of the original value and original extruder offsets are not restored!

## Requirements and Pitfalls

* The Firmware must be Repetier based with active EEPROM-option.

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

  pip install https://github.com/platsch/OctoPrint-Autocalibration/archive/master.zip


This work is based on the [OctoPrint-EEprom-Repetier](https://github.com/Salandora/OctoPrint-EEPROM-Repetier) plugin by Salandora.
