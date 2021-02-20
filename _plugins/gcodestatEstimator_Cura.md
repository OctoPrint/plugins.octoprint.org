---
layout: plugin

id: gcodestatEstimator_Cura
title: GcodeStat Estimator Cura
description: uses data put in to gcode by Cura to estimate time to finish print
author: Nils Hendrik Rottgardt, Based on Bogdan Kecman
license: unlicence
date: 2021-02-20
homepage: https://github.com/NilsRo/OctoPrint-gcodestatEstimator
source: https://github.com/NilsRo/OctoPrint-gcodestatEstimator
archive: https://github.com/NilsRo/OctoPrint-gcodestatEstimator/archive/master.zip
follow_dependency_links: false

tags:
- helper
- estimator
- estimation
- time
- print time
- cura

compatibility:

  octoprint:
  - 1.3.9

  python: ">=2.7,<4"
---

# Estimator is based on Arhi Script but adapted to needs of Cura

## Requirement
 * Needs M73 and M117 codes in your G-Code in Cura format. M73 contains percentage done and M117 remaining time.
 * You have to add Cura Post Processing Script "Display Progress On LCD" and activate "Time Remaining" and "Percentage" to add necessary information to G-Code file. 
## Notes
 * In case there are no M117 codes that can be recognised the original estimator from OctoPrint will be used
 * In case SDCARD print is used the original estimator from OctoPrint will be used
 * The Plugin does not have anything to configure simply install and activate Post Processing. If no corresponding commands are found standard estimation is used.
