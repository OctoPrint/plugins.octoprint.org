---
layout: plugin

id: EasyServo
title: Easy Servo
description: Plugin to control two servos attached to a camera gimbal to control motion.
author: iFrostizz, jneilliii
license: AGPLv3

date: 2020-05-21

homepage: https://github.com/iFrostizz/OctoPrint-EasyServo
source: https://github.com/iFrostizz/OctoPrint-EasyServo
archive: https://github.com/iFrostizz/OctoPrint-EasyServo/archive/master.zip

tags:
- GPIO
- servos
- PWM

featuredimage: /assets/img/plugins/EasyServo/screenshot_easyservo.png

compatibility:
  octoprint:
  - 1.2.0
  os:
  - linux
  python: ">=2.7,<4"

---

# Easy Servo

Here is a simple plugin to control two servos using the OctoPrint Control tab. It has been programmed in conjuction with a camera gimbal mount design I published on Thingiverse [here](https://www.thingiverse.com/thing:4381240).

![Easy Servo](/assets/img/plugins/EasyServo/screenshot_easyservo.png)

It utilizes a custom `@EASYSERVO <GPIO NUMBER> <RELATIVE ANGLE DIFFERENCE>` command that can be incorporated within your slicer to automatically move while printing. 

Example: `@EASYSERVO 12 10` will move the servo attached to GPIO 12 10 degrees in the positive direction from the current position. `@EASYSERVO 13 -10` will move the servo attached to GPIO 13 10 degrees in the negative direction from the current position. 

**Note:** The servos will initialize at 90 degrees on OctoPrint start up and is limited to a 90 degree rotation in either direction.

## Pre-Installation Requirements

Please follow the instructions [here](https://github.com/iFrostizz/OctoPrint-EasyServo#pre-installation-requirements) in order for this plugin to properly operate. Without these steps the plugin will not be able to control the GPIO pins on your Pi and as a result the servos will not move.

## Settings

The plugin supports the ability to configure the GPIO number used for controlling the servos for the X and Y axes.

![Easy Servo Settings](/assets/img/plugins/EasyServo/screenshot_settings_easyservo.png)

### Disclaimer

Although I, iFrostizz, use this plugin and it works for me without issues, I take no resposiblity for any damage caused by using this plugin or connecting servos to your Pi. Please make sure to do your reseach and understand the dangers and please be careful.


