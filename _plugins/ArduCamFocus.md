---
layout: plugin

id: ArduCamFocus
title: ArduCamFocus
description: Plugin to control ArduCam with motorized focus control on octopi
author: moof, jneilliii
license: AGPLv3

date: 2020-07-04

homepage: https://github.com/moof-src/ArduCamFocus
source: https://github.com/moof-src/ArduCamFocus
archive: https://github.com/moof-src/ArduCamFocus/archive/master.zip

tags:
- ArduCam
- camera
- focus

featuredimage: /assets/img/plugins/ArduCamFocus/ControlScreenShot.png

compatibility:
  octoprint:
  - 1.4.0
  os:
  - linux
  python: ">=2.7,<4"

---

# ArduCamFocus

Here is a simple plugin to control an ArduCam motorized focus camera using the OctoPrint Control tab. It uses I2C and it is expected the user followed the ArduCam installation instructions and enabled I2C support.

![screenshot](/assets/img/plugins/ArduCamFocus/ControlScreenShot.png)

It utilizes these custom commands from your slicer to adjust focus while printing:
  `@ARDUCAMFOCUS <RELATIVE-FOCUS>` to adjust focus 
  `@ARDUCAMFOCUSSET <ABS-FOCUS>` to specify an absolute focus. This command is handy to reset the focus when starting a new print after a power failure.

Example: `@ARDUCAMFOCUSSET 100` will move the focus to 100.

## Pre-Installation Requirements

Please follow the instructions [here](https://github.com/moof-src/ArduCamFocus#pre-installation-requirements) in order for this plugin to properly operate. Without these steps the plugin will not be able to control the I2C camera on your Pi and as a result the focus will not change.

## Settings

This plugin has no configurable settings.

### Disclaimer

Although I use this plugin and it works for me without issues, I take no resposiblity for any damage caused by using this plugin. Your camera version, i2c address, or system configuration may be different from mine.  Please make sure to do your reseach and understand the dangers and please be careful.

