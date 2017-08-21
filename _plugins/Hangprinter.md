---
layout: plugin

id: Hangprinter
title: OctoPrint-Hangprinter
description: This plugin provides some useful hangprinter control elements. It makes setup and calibration of a Hangprinter less painful. For more iformation about the Hangprinter visit: hangprinter.org
author: Mario Lukas
license: AGPLv3

date: 2017-08-20

homepage: https://github.com/mariolukas/OctoPrint-Hangprinter
source: https://github.com/mariolukas/OctoPrint-Hangprinter
archive: https://github.com/mariolukas/OctoPrint-Hangprinter/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- Hanprinter
- controls
- calibration
- ui

screenshots:
- url: assets/img/plugins/Hangprinter/screenshot.jpg
  alt: Simple Settings Mode
  caption: Hangprinter Controls and Calibration
- url: assets/img/plugins/Hangprinter/screenshot_adv.jpg
  alt: Advanced Calibration Mode
  caption: Advanced Calibration Settings

featuredimage: assets/img/plugins/Hangprinter/screenshot.jpg

The controls can be used to unwind all gears seperatly. The bottom form can be used to enter the measurements for the hangprinter setup. By pressing the "calculate values" Button, all values are calculated. Pressing the "set values to EEPROM" will save the values in the EEPROM of the printer. Keep in mind that EEPROM option is not activated in the Hangprinter Marlin Firmware by default. You need to enable this Option.
http://plugins.octoprint.org/plugin/hangprinter/
