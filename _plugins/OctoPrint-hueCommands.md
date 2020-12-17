---
layout: plugin

id: hueCommands
title: Add GCODE like HUE commands to OctoPrint
description: Illuminate your print job and signal its status using a Philips Hue light. Enter a GCODE equivalent anywhere you want.
author: LMS0815
license: AGPLv3
date: 2020-12-17

homepage: https://github.com/LMS0815/OctoPrint-hueCommands
source: https://github.com/LMS0815/OctoPrint-hueCommands
archive: https://github.com/LMS0815/OctoPrint-hueCommands/archive/master/OctoPrint-hueCommands.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- hue
- gcode
- automation
- lights
- philips hue
- status
- philips

compatibility:
 octoprint: ">=1.3.9,<1.6"
 python: ">=2.7,<4"

screenshots:
- url: https://raw.githubusercontent.com/LMS0815/OctoPrint-hueCommands/master/screenshots/huecommands_settings.png
- alt: Plugin Settings

featuredimage: https://raw.githubusercontent.com/LMS0815/OctoPrint-hueCommands/master/screenshots/huecommands_settings.png
---

The plugin enables you to control Philips hue lighting by adding commands to your GCODE script(s). 
A command like `HUE L15 on` added to you start print GCODE would switch on light 15 before printing.
Sending `HUE L15 off` via console (or widget window, script) would switch it off.

## Support My Efforts
I programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and support me.

[![paypal](https://www.paypalobjects.com/digitalassets/c/website/marketing/emea/de/de/logo-center/M2_Logo_02.jpg)](https://paypal.me/stonehome/5 "PayPal.me")

