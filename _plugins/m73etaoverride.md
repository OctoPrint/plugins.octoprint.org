---
layout: plugin

id: m73etaoverride
title: M73 ETA Override
description: Plugin that overrides OctoPrint ETA to values from last M73 gcode sent to the printer
author: Jakub Furman
license: AGPLv3

date: 2018-09-18

homepage: https://github.com/sysadminsh/OctoPrint-M73ETAOverride
source: https://github.com/sysadminsh/OctoPrint-M73ETAOverride
archive: https://github.com/sysadminsh/OctoPrint-M73ETAOverride/archive/master.zip

follow_dependency_links: false

abandoned: https://github.com/OctoPrint/plugins.octoprint.org/issues/619

tags:
- progress
- eta
- estimation
- m73
---

## About
The last Sli3cr Prusa Edition implemented M73 gcode injecting to the generated gcodes. This M73 estimations works a much better for Prusa printers than normal OctoPrint ETA estimator. M73 are displayed on Prusa LCD already directly after receiving gcode so there is nothing to change but I think that it will be good to make this better estimation available also on other OctoPrint sources (web/mobile etc) so this plugin will override OctoPrint estimation with estimation from last M73 gcode sended.

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.
