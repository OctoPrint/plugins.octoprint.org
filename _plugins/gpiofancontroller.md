---
layout: plugin

id: gpiofancontroller
title: OctoPrint-GpioFanController
description: Uses PI GPIO pins to control a variable speed fan with PWM
author: Erik Gundersen
license: AGPLv3

date: 2021-07-04

homepage: https://github.com/z4gunn/OctoPrint-GpioFanController
source: https://github.com/z4gunn/OctoPrint-GpioFanController
archive: https://github.com/z4gunn/OctoPrint-GpioFanController/archive/master.zip

follow_dependency_links: false

tags:
- fan
- gpio
- pwm

screenshots:
- url: /assets/img/plugins/gpiofancontroller/featured.png
  alt: Fan speed control
  caption: Fan speed control
- url: /assets/img/plugins/gpiofancontroller/sidebar.png
  alt: Sidebar speed control
  caption: Sidebar speed control
- url: /assets/img/plugins/gpiofancontroller/settings.png
  alt: Pin and PWM frequency settings
  caption: Pin and PWM frequency settings

featuredimage: /assets/img/plugins/gpiofancontroller/featured.png

compatibility:
  octoprint:
  - 1.2.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=3,<4"

---

GPIO FAN Controller
=========================
This is a lightweight plugin dedicated for controlling a fan via Raspberry Pi GPIO pin.  This plugin has the following features:

* Convenient sidebar control
* Adjustable FAN speed
* Pin selection via settings
* M106 / M107 GCODE support
* Independent GCODE control using optional fan index

## IMPORTANT - FAN Compatibility

This plugin is only intended to drive an external brushless DC FAN via MOSFET driver circuit.  A MOSFET must be used to drive the FAN since the PI is not capable of providing adequate current to the FAN.  

This is a great [tutorial](https://create.arduino.cc/projecthub/ejshea/connecting-an-n-channel-mosfet-7e0242) that explains on how to connect a brushless DC FAN to the an Arduino, however the same concept applies to interfacing to a PI.  You can also use a larger MOSFET such as [IRLB8721](https://www.adafruit.com/product/355) to drive fans that require more than  200 mA.