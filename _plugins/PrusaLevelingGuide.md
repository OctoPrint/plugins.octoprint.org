---
layout: plugin

id: PrusaLevelingGuide
title: Prusa Leveling Guide
description: Plugin that helps walk you through adjusting the Prusa MK3 heatbed using the nylock mod
author: Scott Rini
license: AGPLv3

date: 2019-12-18

homepage: https://github.com/scottrini/OctoPrint-PrusaLevelingGuide
source: https://github.com/scottrini/OctoPrint-PrusaLevelingGuide
archive: https://github.com/scottrini/OctoPrint-PrusaLevelingGuide/archive/master.zip

follow_dependency_links: false

tags:
- prusa
- bed level
- mesh
- nylock


screenshots:
- url: /assets/img/plugins/PrusaLevelingGuide/table.png
  alt: Table view
  caption: Table view
- url: /assets/img/plugins/PrusaLevelingGuide/bed.png
  alt: Heatbed view
  caption: Heatbed view
featuredimage: /assets/img/plugins/PrusaLevelingGuide/bed.png

compatibility:
  python: ">=2.7,<4"

---

## About

**Start here**
[Bed Leveling without Wave Springs](https://github.com/PrusaOwners/prusaowners/wiki/Bed_Leveling_without_Wave_Springs)

This plugin is to help guide you through the fine adjustments of the nylock bed leveling method for Prusa MK3 printers, which is described in the above guide.  Make sure you start there and already have the nylocks applied to your bed before beginning.  This plugin allows you to select a profile for preheating, then begin adjustment.  For each round of adjustment, the plugin will send the configured mesh level code and gcode for retrieving values (generally G80; G81).  Once values are received, you can view how to adjust your bed in a number of ways.  You click continue to proceed with another round of leveling or click finish to finish up.

You have the option of viewing the values in a table view or overlayed on a photo of the heatbed.  You can also customize whether you view raw values, degrees, decimal turns, or factional turns.

