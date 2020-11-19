---
layout: plugin

id: hardwarepwm
title: OctoPrint-Hardwarepwm
description: Plugin for true hardware PWM on the Raspberry Pi
author: Daria Rostirolla
license: AGPLv3

date: 2019-02-08

homepage: https://github.com/pastapojken/OctoPrint-Hardwarepwm
source: https://github.com/pastapojken/OctoPrint-Hardwarepwm
archive: https://github.com/pastapojken/OctoPrint-Hardwarepwm/archive/master.zip

tags:
- hardware pwm
- control
- pwm
- leds

screenshots:
- url: /assets/img/plugins/hardwarepwm/settingsPage.png
  alt: settings page
  caption: Settings page
- url: /assets/img/plugins/hardwarepwm/tabPage.png
  alt: tab page
  caption: Tab page

featuredimage: /assets/img/plugins/hardwarepwm/settingsPage.png

compatibility:

  octoprint:
  - 1.2.0

  os:
  - linux

  python: ">=2.7,<4"

---

Plugin that uses the PIGPIO library for hardware PWM, thus creating a flicker free pwm signal for LED strip dimming. Requires you to install pigpio through apt-get and to start/enable the pigpiod daemon.
