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
- url: /assets/img/plugins/gpiorgbcontroller/wiring_diagram.png
  alt: Wiring diagram
  caption: Wiring diagram

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

A MOSFET must also be used to drive each LED channel since the PI is not capable of providing adequate current to the LED's.  It is a also a good idea to use a separate power supply to drive the LED strip since the PI power supply might not have adequate current to drive the PI + LED strip.  See wiring digram below as an example of how to interface to an LED strip.