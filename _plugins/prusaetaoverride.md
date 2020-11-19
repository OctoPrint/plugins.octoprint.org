---
layout: plugin

id: prusaetaoverride
title: Prusa (M73 response) ETA Override
description: Plugin that overrides OctoPrint ETA to values from last M73 gcode response received from printer
author: Anton Skorochod
license: AGPLv3

date: 2019-08-25

homepage: https://github.com/kanocz/octopi_eta_override
source: https://github.com/kanocz/octopi_eta_override
archive: https://github.com/kanocz/octopi_eta_override/archive/master.zip

follow_dependency_links: false

tags:
- progress
- eta
- estimation
- m73

compatibility:
  python: ">=2.7,<4"

---

## About
The last Sli3cr Prusa Edition implemented M73 gcode injecting to the generated gcodes. This M73 sends "NORMAL MODE: Percent done: 0; print time remaining in mins: 3" to serial with perfect time estimation. This plugin overrides ETA to this value.

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.
