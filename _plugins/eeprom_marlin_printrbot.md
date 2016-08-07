---
layout: plugin

id: eeprom_marlin
title: EEPROM Printrbot variant of Marlin Editor
description: Makes it possible to change the EEPROM values of Printrbot variant of Marlin Firmware through OctoPrint
author: Ryan Neufeld
license: AGPLv3

date: 2015-12-26

homepage: https://github.com/ryanneufeld/OctoPrint-EEprom-Marlin
source: https://github.com/ryanneufeld/OctoPrint-EEprom-Marlin
archive: https://github.com/ryanneufeld/OctoPrint-EEprom-Marlin/archive/master.zip

follow_dependency_links: false

# TODO
tags:
- marlin
- helper

screenshots:
- url: /assets/img/plugins/eeprom_marlin/img1.png
  alt: Settings
- url: /assets/img/plugins/eeprom_marlin/img2.png
  alt: Settings

featuredimage: /assets/img/plugins/eeprom_marlin/img2.png

compatibility:
  octoprint:
  - 1.2.0

  os:
  - linux
  - windows
  - macos
---

This plugin is designed to get, change and save the values in the EEPROM of your Printrbot variant of Marlin Firmware based Machine
