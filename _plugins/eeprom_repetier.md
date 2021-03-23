---
layout: plugin

id: eeprom_repetier
title: EEPROM Repetier Editor
description: Makes it possible to change the EEPROM values of Repetier Firmware through OctoPrint
author: Marc Hannappel (Salandora)
license: AGPLv3

date: 2015-07-28

homepage: https://github.com/Salandora/OctoPrint-EEprom-Repetier
source: https://github.com/Salandora/OctoPrint-EEprom-Repetier
archive: https://github.com/Salandora/OctoPrint-EEprom-Repetier/archive/master.zip

follow_dependency_links: false

tags:
- repetier
- eeprom
- editor
- eeprom editor
- eeprom config
- helper

featuredimage: /assets/img/plugins/eeprom_repetier/eeprom_values.png

compatibility:
  python: ">=2.7,<4"
  octoprint: 
  - 1.5.x

---

This plugin is designed to get, change and save the values in the EEPROM of your Repetier Firmware based Machine

## Features

- Load and edit the values stored EEPROM from the printer firmware.
- Save changes to the EEPROM on the printer.
- Backup and restore snapshot copies of the EEPROM data (new in V0.1.4).

## Setup

Find it in the plugin manager or install manually using the archive URL

## Firmware requirements

This plugin only supports Repetier firmware, version 0.92 and later.  Use caution when restoring data from an older firmware version.  

## Screenhots

EEPROM Values Editor
![EEPROM Values](/assets/img/plugins/eeprom_repetier/eeprom_values.png)

Changed Values Display
![Changed Values Displayed](/assets/img/plugins/eeprom_repetier/eeprom_changed_values.png)

EEPROM Backups
![Backups](/assets/img/plugins/eeprom_repetier/eeprom_values.png)
