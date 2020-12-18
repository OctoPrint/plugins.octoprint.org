---
layout: plugin

id: hueCommands
title: Add GCODE like HUE commands to OctoPrint
description: Illuminate your print job and signal its status using a Philips Hue light. Enter a GCODE equivalent anywhere you want.
author: LMS0815
license: AGPLv3
date: 2020-03-18
homepage: https://github.com/LMS0815/OctoPrint-hueCommands
source: https://github.com/LMS0815/OctoPrint-hueCommands
archive: https://github.com/LMS0815/OctoPrint-hueCommands/archive/master/OctoPrint-hueCommands.zip
tags:
- hue
- philips
- philips hue
- gcode
- automation
- lights
- status
compatibility:
  python: ">=2.7,<4"
  octoprint: 1.5
screenshots:
- url: /assets/img/plugins/hueCommands/huecommands_settings_bridge.png
  alt: Plugin Settings - Bridge Parameter
- url: /assets/img/plugins/hueCommands/huecommands_settings_examples.png
  alt: Plugin Settings - Examples
- url: /assets/img/plugins/hueCommands/huecommands_settings_preset.png
  alt: Plugin Settings - Presets
- url: /assets/img/plugins/hueCommands/huecommands_settings_usage.png
  alt: Plugin Settings - Usage documentation
featuredimage: /assets/img/plugins/hueCommands/huecommands_settings_feature.png

---

This plugin enables you to control Philips hue lighting by adding commands to your GCODE script(s).
A command like `HUE L15 on` added to you start print GCODE would switch on light 15 before printing.
Sending `HUE L15 off` via console (or widget window, script) would switch it off.

## Support My Efforts
I programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and support me.

[![paypal](/assets/img/plugins/hueCommands/PayPal_Logo.jpg)](https://paypal.me/stonehome/5 "PayPal.me")
