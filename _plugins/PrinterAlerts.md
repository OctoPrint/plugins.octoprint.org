---
layout: plugin

id: PrinterAlerts
title: OctoPrint-PrinterAlerts
description: Alert the user when their printer is waiting for interaction.
author: Patrick Leiser
license: aGPLv3

date: 2019-06-08

homepage: https://github.com/Patronics/OctoPrint-PrinterAlerts
source: https://github.com/Patronics/OctoPrint-PrinterAlerts
archive: https://github.com/Patronics/OctoPrint-PrinterAlerts/archive/master.zip


tags:
- printer
- alert
- waiting
- notification
- multimaterial

screenshots:
- url: /assets/img/plugins/PrinterAlerts/screenshot.png
  alt: A demonstration of 'Print paused for user' alert
  caption: An example alert
- url: /assets/img/plugins/PrinterAlerts/settings.png
  alt: The settings page, allowing configurable alert urgency, auto-closing, and spoken alerts
  caption: the settings page

featuredimage: /assets/img/plugins/PrinterAlerts/screenshot.png

compatibility:
  python: ">=2.7,<4"

---

# PrinterAlerts

This plugin detects ``echo:busy: paused for user`` messages from the printer and uses OctoPrint's built in alert system to notify the user that the printer needs their attention.

This is especially useful for Prusa's printers with MultiMaterial Units installed, as the printer prompts you to select the filament to use on the LCD when printing in Single Material Mode.
## Screenshots

![screenshot](/assets/img/plugins/PrinterAlerts/screenshot.png)

![settings](/assets/img/plugins/PrinterAlerts/settings.png)

## Features
* Will bring up a standard alert in octoprint when the printer is waiting for your input.
* Configurable alert severity, from "Error" and "Warning", to "Info", and "Sucess"
* Set alerts to auto-hide, or to stay on screen
 * Note: For printer like the Prusas that repeatedly give the same message while waiting, I strongly recommend leaving this set to Auto Close.
* Optionally can speak the alerts as well (not supported in all browsers)

## Compatibility
* This plugin was designed to work with the Prusa i3 Mk3s MMU2 3D printer, and will likely work with other Prusa printers as well.
* It will work with any non-prusa printers that output the same message``echo:busy: paused for user`` when waiting for user input
* For other printers that have a different waiting for user message, create an issue on github, and I'll be happy to try to implement it for those messages as well
* this plugin might not work with files on the SD card. (Untested)
