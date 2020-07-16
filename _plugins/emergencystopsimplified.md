---
layout: plugin

id: emergencystopsimplified
title: Emergency Stop Simplified
description: This plugin reacts to a switch or button, if triggered (switch open) it issues M112 command to printer.
author: Mechazawa
license: AGPLv3

date: 2020-04-26

homepage: https://github.com/Mechazawa/Emergency_stop_simplified
source: https://github.com/Mechazawa/Emergency_stop_simplified
archive: https://github.com/Mechazawa/Emergency_stop_simplified/archive/master.zip

follow_dependency_links: false

tags:
- emergency
- stop
- simplified
- simple
- trigger
- button

compatibility:
  python: ">=2.7,<4"

  octoprint:
  - 1.3.0
 
  os:
  - linux
---

#### Description

This plugin reacts to a switch or button, if triggered (switch open) it issues **M112** command to printer.

Let's check some features:
* info pop-up when plugin hasn't been configured
* user-friendly and easy to configure
* runs on OctoPrint 1.3.0 and higher

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/Mechazawa/Emergency_stop_simplified

## Configuration

Configuration couldn't be simpler, all you need is to configure listening board pin (board mode) and if the second switch terminal is connected to ground or 3.3V.

Default pin is -1 (not configured) and ground (as it is safer, read below).

**WARNING! Never connect the switch input to 5V as it could fry the GPIO section of your Raspberry!**
