---
layout: plugin

id: filamentrevolutions
title: Filament Sensor Revolutions
description: Use 1 or 2 filament sensors to pause printing or send GCode commands when filament runs out or is jammed.
author: RomRider
license: AGPLv3
date: 2019-11-20

homepage: https://github.com/RomRider/Octoprint-Filament-Revolutions
source: https://github.com/RomRider/Octoprint-Filament-Revolutions
archive: https://github.com/RomRider/Octoprint-Filament-Revolutions/archive/master.zip
follow_dependency_links: false

tags:
- filament
- sensor

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.6

  os:
  - nix
---
[OctoPrint](http://octoprint.org/) plugin that integrates with 1 or 2 filament sensors hooked up to a Raspberry Pi GPIO pin and allows the filament spool to be changed during a print if the filament runs out or is jammed.

You can pause or send GCode commands when a sensor is tripped. Behaviours can be different between the runout sensor and the jam sensor.

An API is available to check the filament sensors status via a GET method:
* to `/plugin/filamentrevolutions/filament` for the filament sensor
* to `/plugin/filamentrevolutions/jammed` for the jam sensor

- `{status: "-1"}` if the sensor is not setup
- `{status: "0"}` if the sensor is OFF (filament not present/filament not jammed)
- `{status: "1"}` if the sensor is ON (filament present/filament jammed)

Here's the settings page:
![Settings](/assets/img/plugins/filamentrevolutions/settings.png)

Initial work based on the [Octoprint-Filament-Reloaded](https://github.com/kontakt/Octoprint-Filament-Reloaded) plugin by kontakt.
