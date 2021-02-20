---
layout: plugin

id: gcodestatEstimator_Cura
title: GcodeStat Estimator Cura
description: uses data put in to gcode by Cura to estimate remaining printtime
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

---

# Estimator is based on Arhi Script and changed to needs of Cura
With this plugin and active Post Processing in Cura you will get an excact estimation of time remaining as it will set from information analysed in the slicer (Cura). So it will be very accurate.

## Requirement
 * Needs M73 and M117 codes in your G-Code in Cura format. M73 contains percentage done and M117 remaining time.
 * You have to add Cura Post Processing Script "Display Progress On LCD" and activate "Time Remaining" and "Percentage" to add necessary information to G-Code file. 
## Notes
 * In case there are no M117 codes that can be recognised the original estimator from OctoPrint will be used
 * In case SDCARD print is used the original estimator from OctoPrint will be used
 * The Plugin does not have anything to configure simply install and activate Post Processing. If no corresponding commands are found standard estimation is used.
