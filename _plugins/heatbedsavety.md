---
layout: plugin

id: heatbedsavety
title: OctoPrint-HeatBedSavety
description: HighPower HeatBedSavety Plugin
author: linux-paul
license: AGPLv3

date: 2020-08-14

homepage: https://github.com/linux-paul/OctoPrint-Heatbedsavety
source: https://github.com/linux-paul/OctoPrint-Heatbedsavety
archive: https://github.com/linux-paul/OctoPrint-Heatbedsavety/archive/master.zip

follow_dependency_links: false


tags:
- heat
- bed
- heatbed

screenshots:
- url: /assets/img/plugins/heatbedsavety/sidebar.png
  alt: sidebar button
  caption: Sidebar Button
- url: /assets/img/plugins/heatbedsavety/settings.png
  alt: settings
  caption: Settings


compatibility:
  octoprint:
  - 1.3.6+

  os:
  - all
 
  python:
  - ">=2.7,<4"

---

This plugin is able to control a relais in serial connection to a solid state relais of a high power heatbes solution.
Solid state relais some times getting shorted when they are damaged and will heat up to ~200°C out of conrtol of the printer.
This plugin cut the solid state from power when a configured temperature is reached or an error is thrown by the printer.

In some countries, not everybody is allowed to create or change 230V/130V electrical cicuits.
In this case you'll do the changes !! AT YOUR OWN RISK !! and no insurence will pay a damage.


