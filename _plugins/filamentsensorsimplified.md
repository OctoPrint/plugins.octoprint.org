---
layout: plugin

id: filamentsensorsimplified
title: Filament Sensor Simplified
description: This plugin reacts to filament sensor output. If triggered it issues M600 X0 Y0 command to printer.
author: Lukáš Malatinský
license: AGPLv3

date: 2020-04-14

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

compatibility:
  python: ">=2.7,<4"

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

Configuration couldn't be simpler, all you need is to configure listening board pin (board mode) and if the switch is normally open or closed.

Default pin is -1 (not configured) and normally closed.

#### Support me

This plugin was developed in my spare time.
If you like it, you can support me by clicking the button below :) 

[![More coffee, more code](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=5L758LYSUGHW4&source=url)