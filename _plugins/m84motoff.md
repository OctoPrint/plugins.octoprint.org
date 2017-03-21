---
layout: plugin
    
id: m84motoff
title: M84 Motors Off
description: Changes the "Motors Off" command from M18 to M84 for compatibility with Repetier Firmware.
author: ntoff
license: AGPLv3

date: 2017-03-21
    
homepage: https://github.com/ntoff/Octoprint-M84MotOff
source: https://github.com/ntoff/Octoprint-M84MotOff
archive: https://github.com/ntoff/Octoprint-M84MotOff/archive/master.zip
    
follow_dependency_links: false
    
tags:
- repetier firmware
- repetier
- motors off
- disable motors
- disable stepper hold
- M84


compatibility:
  octoprint:
  - 1.2.0


  os:
  - linux
  - windows
  - macos
---
    
A plugin to intercept the gcode command M18 during the queueing stage and rewrite it as M84 before sending it to the printer (for compatibility with the Repetier line of firmware).

Note: Because this plugin intercepts the code during the queueing stage, that also includes manual gcode entry. Entering M18 in the terminal tab will also result in it being send to the printer as M84.