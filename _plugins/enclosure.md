---
layout: plugin

id: enclosure
title: OctoPrint-Enclosure
description: Control printer environment (Temperature control / Lights / Fans and Filament Sensor) using Raspberry Pi GPIO
author: Vitor Henrique
license: GPLv3

date: 2017-03-15

homepage: https://github.com/vitormhenrique/OctoPrint-Enclosure
source: https://github.com/vitormhenrique/OctoPrint-Enclosure
archive: https://github.com/vitormhenrique/OctoPrint-Enclosure/archive/master.zip

follow_dependency_links: false

tags:
- filament
- sensor
- temperature
- humidity
- control
- fan
- lights
- DHT22
- DHT11
- AM2302
- DS18B20
- GCODE
- NEOPIXEL
- ws2812b
- SI7021
- BME280
- TMP102

screenshots:
- url: /assets/img/plugins/enclosure/Plugin_Tab.png
  alt: OctoPrint enclosure main screen.
  caption: OctoPrint enclosure main screen.
- url: /assets/img/plugins/enclosure/Input_Configuration.png
  alt: OctoPrint enclosure setting screen.
  caption: OctoPrint enclosure setting screen.
- url: /assets/img/plugins/enclosure/Output_Configuration.png
  alt: OctoPrint enclosure setting screen.
  caption: OctoPrint enclosure setting screen.
- url: /assets/img/plugins/enclosure/Advanced_Section.png
  alt: OctoPrint enclosure setting screen.
  caption: OctoPrint enclosure advanced setting screen.

featuredimage: /assets/img/plugins/enclosure/Plugin_Temperature_Control.png

compatibility:
  os:
  - nix
---

This plugin is intended to control your printer enclosure using raspberry pi GPIO (At the moment this plugin only support raspberry pi).

A list of things that you can do:
* Add temperature sensors on your enclosure or near your printer
* Add active heaters on your enclosure and keep the temperature nice and high for large ABS
* Use custom Gcode to control rapsberry pi GPIO
* Use custom Gcode to control neopixel
* Use custom Gcode to control enclosure temperature
* PWM controlled outputs
* PWM controlled outputs based on temperature sensor
* Active cooling for good PLA printing
* Schedule GPIO's to turn on and off with a fixed period of time during printing.
* Mechanical buttons to pause and resume printer jobs
* Mechanical buttons to send GCODE to the printer
* Mechanical buttons to control raspberry pi GPIO
* Multiple filament sensors for dual or more extruders
* Alarm when enclosure temperature reaches some sort of value
* Notifications using IFTTT when events happen (temperature trigger / print events / etc)
* Add sub-menus on navbar to quick access outputs and temperature sensors

There is also an API that can be used to interact with the plugin with other software


