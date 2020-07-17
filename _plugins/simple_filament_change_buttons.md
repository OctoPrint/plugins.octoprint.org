---
layout: plugin

id: simple_filament_change_buttons
title: Simple Filament Change Buttons
description: Simply adds some buttons to send the filament load/unload/change commands for Marlin, so you don't have to use the LCD menu
author: Gareth Martin
license: mit

date: 2020-06-12

homepage: https://github.com/TheThief/Octoprint_Simple_Filament_Change_Buttons/
source: https://github.com/TheThief/Octoprint_Simple_Filament_Change_Buttons/
archive: https://github.com/TheThief/Octoprint_Simple_Filament_Change_Buttons/archive/master.zip

tags:
- filament

screenshots:
- url: /assets/img/plugins/simple_filament_change_buttons/sfc_buttons.png
  alt: Screenshot showing Park/Unload/Load/Change buttons
  caption: Filament Change Buttons

featuredimage: /assets/img/plugins/simple_filament_change_buttons/sfc_buttons.png

---

# Simple Filament Change Buttons

This plugin simply adds some buttons to send the filament load/unload/change commands for Marlin, so you don't have to use the LCD menu.

## Use

To use automated filament change (M600):

* Click **Change Filament** to automatically park the head and then unload filament.
* When new filament is ready to load, click the LCD button or the **Resume** button in Octoprint.

To manually unload/load (M702/M701):

* Make sure the nozzle is heated
* On the Control tab, click **Unload** to unload the old filament
* Feed in the new filament to the extruder gear. Then click **Load** to load the new filament

## Configuration

Enable ADVANCED_PAUSE_FEATURE in your Marlin firmware, along with PARK_HEAD_ON_PAUSE and FILAMENT_LOAD_UNLOAD_GCODES. I also recommend having EMERGENCY_PARSER enabled.
