---
layout: plugin

id: CooldownNotification
title: CooldownNotification
description: A plugin to execute gcode commands when the print bed cools to a certain temperature
author: George McCauley
license: AGPLv3

date: 2020-05-26

homepage: https://github.com/gmccauley/OctoPrint-CooldownNotification
source: https://github.com/gmccauley/OctoPrint-CooldownNotification
archive: https://github.com/gmccauley/OctoPrint-CooldownNotification/archive/master.zip

tags:
- gcode
- heated bed
- notification
- cooldown

featuredimage: /assets/img/plugins/CooldownNotification/settings.png

compatibility:
  octoprint:
  - 1.4.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=3,<4"

---

# CooldownNotification

This plugin is designed to execute gcode commands when the print bed cools to a certain temperature.

The intended usage is to utilize the M300 gcode to alert that the bed has cooled and it's safe to remove prints printed in PETG.

## Settings

![CooldownNotification Settings](/assets/img/plugins/CooldownNotification/settings.png)