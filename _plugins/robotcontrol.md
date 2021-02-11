---
layout: plugin

id: robotcontrol
title: Robot Control
description: Plugin to control a robot over i2c
author:
- Louis Sarwal
license: AGPLv3

date: 2021-02-11

homepage: https://github.com/Zinc-OS/octoprint-robot-plugin
source: https://github.com/Zinc-OS/octoprint-robot-plugin
archive: https://github.com/Zinc-OS/octoprint-robot-plugin/archive/master.zip

tags:
- robot
- servo
- GPIO
-i2c
-robotics
-automation
-i2cbus

featuredimage: /assets/img/plugins/robotcontrol/screnshat.png

compatibility:
  octoprint:
  - 1.5.0
  os:
  - linux
  python: ">=2.7,<4"
---

# Robot Control Plugin

Plugin for controling my robot via the i2c bus.


## Configuration

Currently For a four servo robot(I plan to add support for more).

You will also need to enable i2c bus via ```sudo raspi-cofig``` throught the terminal, accessible through ```ssh pi@octopi.local:22```

then
```interface options>enable i2c>yes>finish```

For the raspi, addresses cannot be lower than 3, and the arduino only use addresses higher than 8, so the address must be an integer 8-127, and must be the same for the adruino and the raspi.

There are sliders in the robot control tab, and gcodes can be used with the format ```@servo[1..4]:[ANGLE]```, such as ```@servo2:90``` or ```@servo4:12```.

## Screenshot

![screenshot](/assets/img/plugins/robotcontrol/screnshat.png)
