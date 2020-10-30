---
layout: plugin

id: filamentsensorsimplified
title: Filament Sensor Simplified
description: This plugin reacts to filament sensor output. If triggered it issues desired gcode to printer.
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
- url: https://github.com/LuckyX182/Filament_sensor_simplified/blob/master/screenshots/settings.png
  alt: Settings page
  caption: Settings page
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
  alt: Waiting for user input pop-up
  caption: Waiting for user input pop-up
  
featuredimage: https://github.com/LuckyX182/Filament_sensor_simplified/raw/master/screenshots/settings.png

compatibility:
  python: ">=2.7,<4"

  octoprint:
  - 1.3.0
 
  os:
  - linux
---

#### Description

This plugin reacts to short lever microswitch output like [this](https://chinadaier.en.made-in-china.com/product/ABVJkvyMAqcT/China-1A-125VAC-on-off-Kw10-Mini-Micro-Mouse-Switch.html)
If triggered it issues configured command to printer.

Let's check some features:
* pop-up notification when printer runs out of filament
* very handy pop-up when printer requires user input while changing filament
* test button so you know if your sensor really works or not
* filament check at the start of the print - if no filament present it won't start printing, again pop-up will appear
* filament check at the end of filament change - just to be sure you won't start printing with no filament
* check if printer supports M600 when printer connected and gcode starts with M600 - if not user will be notified through pop-up
* info pop-up when plugin hasn't been configured
* filament runouts can be repeatable which didn't work with other plugins I tried
* user-friendly and easy to configure
* pin validation so you don't accidentally save wrong pin number
* detection of used GPIO mode - this makes it compatible with other plugins
* runs on OctoPrint 1.3.0 and higher

**NOTE: this plugin won't work if you use OctoPrint only to start printing from SD card**

#### Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/luckyx182/Filament_sensor_simplified/archive/master.zip

#### Configuration

Configuration consists of these parameters:
1. **GPIO mode** - BOARD or BCM mode, **BOARD mode** - referring to the pins by the number, **BCM mode** - referring to the pins
by the "Broadcom SOC channel", if this is selected by 3rd party, this option will be disabled with note on GUI
2. **pin number** - pin number based on selected mode
3. **gcode** to send to printer on filament runout - default is M600 X0 Y0
4. **power input to sensor** - input is connected to **ground or 3.3 V**
5. **switch type** - switch should be **triggered when opened** (input of the sensor doesn't transfer to its output) or **triggered
when closed** (input of the sensor is transferred to its output)

Default pin is -1 (not configured) and ground (as it is safer, read below).

**WARNING! Never connect the switch input to 5V as it could fry the GPIO section of your Raspberry!**

**WARNING! When using test button on input pin used by other application it will reset internal pull up/down resistor**

#### Advice

You might experience the same problem as I experienced - the sensor was randomly triggered. Turns out that if running sensor wires along motor wires, it was enough to interfere with sensor reading.

To solve this connect a shielded wire to your sensor and ground the shielding, ideally on both ends.

If you are unsure about your sensor being triggered, check [OctoPrint logs](https://community.octoprint.org/t/where-can-i-find-octoprints-and-octopis-log-files/299)

#### Support me

This plugin was developed in my spare time.
If you find it useful and like it, you can support me by clicking the button below :)

[![More coffee, more code](https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=5L758LYSUGHW4&source=url)