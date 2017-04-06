---
layout: plugin

id: enclosure
title: OctoPrint-Enclosure
description: Control printer environment (Temperature control / Lights / Fans and Filament Sensor) using Raspberry Pi GPIO
author: Vitor Henrique
license: AGPLv3

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

screenshots:
- url: /assets/img/plugins/enclosure/ScreenShot.png
  alt: OctoPrint enclosure main screen.
  caption: OctoPrint enclosure main screen.
- url: /assets/img/plugins/enclosure/ScreenShot_Settings_1.png 
  alt: OctoPrint enclosure setting screen.
  caption: OctoPrint enclosure setting screen.
- url: /assets/img/plugins/enclosure/ScreenShot_Settings_2.png 
  alt: OctoPrint enclosure setting screen.
  caption: OctoPrint enclosure setting screen.

featuredimage: /assets/img/plugins/enclosure/ScreenShot.png

compatibility:
  os:
  - nix
---

This plugin is intended to control your printer enclosure using raspberry pi GPIO (At the moment this plugin only support raspberry pi).

You can control lights, fans, heaters and filament sensors of your enclosure. To use the heater you need to have a temperature sensor added to your enclosure connected to your raspberry pi.

This plugin can support DHT11, DHT22, AM2302 and DS18B20 temperature sensors.

You can use relays connected to the raspberry pi to control my heaters, fan and lights.

For heating my enclosure I got a $15 lasko inside my encosure. I opened it and added a relay to the mains wire.

Check the github page for instructions on how to configure the plugin.


