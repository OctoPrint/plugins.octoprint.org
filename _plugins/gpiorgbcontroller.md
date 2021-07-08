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
  python: ">=2.7,<3"

---

This is a plugin to control an external RGB LED strip via Raspberry Pi GPIO pins.  This plugin allows you to set the pin numbers in the settings and control the LED color and on/off state via sidebar control.
