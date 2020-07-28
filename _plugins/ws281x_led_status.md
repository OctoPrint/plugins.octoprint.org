---
layout: plugin

id: ws281x_led_status
title: WS281x LED Status
description: Add some WS281x type RGB LEDs to your printer for a quick status update
author: Charlie Powell
license: AGPLv3

date: 2020-07-28

homepage: https://github.com/cp2004/OctoPrint-WS281x_LED_Status
source: https://github.com/cp2004/OctoPrint-WS281x_LED_Status
archive: https://github.com/cp2004/OctoPrint-WS281x_LED_Status/archive/master.zip

follow_dependency_links: false

tags:
- rgb led
- status
- progress
- neopixel
- ws281x
- ws2811
- ws2812

screenshots:
- url: /assets/img/plugins/ws281x_led_status/settings_overview.png
  alt: settings-overview-screenshot
  caption: Settings Overview Screenshot
- url: /assets/img/plugins/ws281x_led_status/printing_effects.png
  alt: settings-printing-screenshot
  caption: Printing Settings Screenshot
- url: /assets/img/plugins/ws281x_led_status/wizard.png
  alt: setup-wizard-screenshot
  caption: Setup Wizard Screenshot

featuredimage: /assets/img/plugins/ws281x_led_status/settings_overview.png

compatibility:

  octoprint:
  - 1.4.0

  os:
  - linux

  python: ">=2.7,<4"

---

Supporting effects for various printing states as well as print and heating progress,
you will always know what your printer is doing without needing to look at the web interface all the time.

Configurable options include turning on and off each event, customising the effect and colours, tracking print and heatup progress, enable a timer so you can have the LEDs on at certain times and a button in the navbar to turn them on and off

### Configuration options
[See here](https://github.com/cp2004/OctoPrint-WS281x_LED_Status/wiki/Configuration-options) for details of the various configuration options available for the plugin, and have a look at the screenshots below

### Get help
Please open an issue on the [Github Repository](https://github.com/cp2004/OctoPrint-WS281x_LED_Status) if you run into a bug, or if you just have a general question post on the [OctoPrint community forum](https://community.octoprint.org) and tag me [@Charlie_Powell](https://community.octoprint.org) and I'll try and respond.

### Setting up SPI
[See here](https://github.com/cp2004/OctoPrint-WS281x_LED_Status/wiki/SPI-Setup-Running-without-root) for details of how to setup SPI so you can use your LEDs. There is also a configuration wizard that will do this for you on the first install, if you ask it nicely.

### Wiring your LEDs
[See here](https://github.com/cp2004/OctoPrint-WS281x_LED_Status/wiki/Wiring-LEDS-to-your-Raspberry-Pi) for details of how to wire your LED strips to a Raspberry Pi.


