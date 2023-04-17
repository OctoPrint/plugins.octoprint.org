---
layout: plugin
id: psucontrol_opigpio
title: PSUControl - OPi.GPIO
description: Adds OPi.GPIO to OctoPrint-PSUControl as a sub-plugin for OrangePi Zero and other SBCs supported by OPi.GPIO.
authors:
- Blue-Beaker
license: AGPLv3
date: 2022-04-27
homepage: https://github.com/Blue-Beaker/OctoPrint-PSUControl-OPi.GPIO
source: https://github.com/Blue-Beaker/OctoPrint-PSUControl-OPi.GPIO
archive: https://github.com/Blue-Beaker/OctoPrint-PSUControl-OPi.GPIO/archive/master.zip
tags:
- power
- psu
- control
- psucontrol
- psucontrol subplugin
- gpio
- orangepi
compatibility:
  os:
  - linux
  python: ">=2.7,<4"

---

This is a fork of Shawn Bruce's [PSU Control - RPi.GPIO](https://plugins.octoprint.org/plugins/psucontrol_rpigpio/) that uses [OPi.GPIO](https://github.com/rm-hull/OPi.GPIO) instead of RPi.GPIO.  
SUNXI naming is supported additionally, so you can use pin numbers on the board like "PA12" directly in this plugin.  
See <https://github.com/Blue-Beaker/OctoPrint-PSUControl-OPi.GPIO> for information on configuration.  
