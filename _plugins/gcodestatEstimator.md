---
layout: plugin
    
id: gcodestatEstimator
title: GcodeStat Estimator
description: uses data put in to g-code by gcodestat to estimate time to finish print
author: Bogdan Kecman
license: unlicence
date: 2018-07-05
homepage: https://github.com/arhi/OctoPrint-gcodestatEstimator
source: https://github.com/arhi/OctoPrint-gcodestatEstimator
archive: https://github.com/arhi/OctoPrint-gcodestatEstimator/archive/master.zip
follow_dependency_links: false

tags:
- helper
- estimator
- estimation
- time
- print time

compatibility:

  octoprint:
  - 1.3.9

---

This plugin will read the M117 data put into G-Code by gcodestat ( https://github.com/arhi/gcodestat ) in format 

M117 ###% Remaining ( HH:MM:SS )

and use this data for displaying proper progress report

requires OctoPrint 1.3.9
