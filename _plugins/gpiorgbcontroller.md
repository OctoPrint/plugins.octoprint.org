---
layout: plugin

id: gpiorgbcontroller
title: OctoPrint-GpioRgbController
description: Uses PI GPIO pins to control a RGB Led strip
author: Erik Gundersen
license: AGPLv3

date: 2021-07-07

homepage: https://github.com/z4gunn/OctoPrint-GpioRgbController
source: https://github.com/z4gunn/OctoPrint-GpioRgbController
archive: https://github.com/z4gunn/OctoPrint-GpioRgbController/archive/master.zip

follow_dependency_links: false

tags:
- led
- rgb
- gpio

screenshots:
- url: /assets/img/plugins/gpiorgbcontroller/featured.png
  alt: Color picker control
  caption: Color picker control
- url: /assets/img/plugins/gpiorgbcontroller/sidebar.png
  alt: Sidebar led color control
  caption: Sidebar led color control
- url: /assets/img/plugins/gpiorgbcontroller/settings.png
  alt: Pin settings
  caption: Pin settings

featuredimage: /assets/img/plugins/gpiorgbcontroller/featured.png

compatibility:
  octoprint:
  - 1.2.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python:  ">=3,<4"

---

GPIO RGB Controller
=========================
This is a lightweight plugin dedicated to the control of an external RGB LED strip via Raspberry Pi GPIO pins.  This plugin has the following features:

* Convenient sidebar control
* Adjustable RGB color picker
* Pin selection via settings
* Optional on/off trigger via input pin
* M150 GCODE support
* Independent GCODE control using optional RGB index

## IMPORTANT - LED Strip Compatibility

This plugin is only intended to drive discrete or strip RGB LED's via independent GPIO control.  This plugin will not work with LED strips that have coontrolers or digital interface such as SPI.  

A MOSFET must also be used to drive each LED channel since the PI is not capable of providing adequate current to the LED's.  This is a great [tutorial](https://learn.adafruit.com/rgb-led-strips) that explains on how to connect an analog RGB LED strip to an Arduino, however the same concept applies to interfacing to a PI.