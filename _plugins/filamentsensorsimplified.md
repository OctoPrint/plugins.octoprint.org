---
layout: plugin

id: filamentsensorsimplified
title: Filament Sensor Simplified
description: This plugin reacts to filament sensor output. If triggered it issues M600 X0 Y0 command to printer.
author: Lukáš Malatinský
license: AGPLv3

date: 2020-04-23

homepage: https://github.com/LuckyX182/Filament_sensor_simplified
source: https://github.com/LuckyX182/Filament_sensor_simplified
archive: https://github.com/LuckyX182/Filament_sensor_simplified/archive/master.zip

follow_dependency_links: false

tags:
- filament
- sensor
- simplified
- simple
- trigger
- runout

screenshots:
- url: https://github.com/LuckyX182/Filament_sensor_simplified/raw/master/screenshots/no_conf_popup.png
  alt: No configuration pop-up
  caption: No configuration pop-up
- url: https://github.com/LuckyX182/Filament_sensor_simplified/raw/master/screenshots/M600_disabled.png
  alt: Pop-up for M600 disabled
  caption: Pop-up for M600 disabled
- url: https://github.com/LuckyX182/Filament_sensor_simplified/raw/master/screenshots/no_filament.png
  alt: No filament when starting print pop-up
  caption: No filament when starting print pop-up
- url: https://github.com/LuckyX182/Filament_sensor_simplified/raw/master/screenshots/filament_runout.png
  alt: Filament runout pop-up
  caption: Filament runout pop-up
- url: https://github.com/LuckyX182/Filament_sensor_simplified/raw/master/screenshots/waiting_for_user_input.png
  alt: Waiting for user input pop-up:
  caption: Waiting for user input pop-up:
  
featuredimage: https://github.com/LuckyX182/Filament_sensor_simplified/raw/master/screenshots/settings.png

compatibility:
  python: ">=2.7,<4"

  octoprint:
  - 1.3.0
 
  os:
  - linux
---

#### Description

This plugin reacts to filament sensor output. If triggered it issues M600 X0 Y0 command to printer. 
It is based on Octoprint-Filament-Reloaded by kontakt but the logic behind is different.

This was only tested on my printer running Marlin 2.0.4.4 so sorry if any bugs present.

#### Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/luckyx182/Filament_sensor_simplified/archive/master.zip

#### Configuration

Configuration couldn't be simpler, all you need is to configure listening board pin (board mode) and if the second switch terminal is connected to ground or 3.3V.

Default pin is -1 (not configured) and ground (as it is safer, read below).

**WARNING! Never connect the switch input to 5V as it could fry the GPIO section of your Raspberry!**

#### Support me

This plugin was developed in my spare time.
If you find it useful and like it, you can support me by clicking the button below :)

[![More coffee, more code](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=5L758LYSUGHW4&source=url)