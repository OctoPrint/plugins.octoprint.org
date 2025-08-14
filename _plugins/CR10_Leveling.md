---
layout: plugin

id: CR10_Leveling
title: Manual Bed Tramming
description: Adds bed tramming buttons to the controls tab
authors:
- lsellens
- AvanOsch
- electr0sheep
license: AGPLv3
date: 2018-02-26
homepage: https://github.com/lsellens/octoprint-manual_bed_tramming
source: https://github.com/lsellens/octoprint-manual_bed_tramming
archive: https://github.com/lsellens/octoprint-manual_bed_tramming/archive/master.zip
tags:
- ui
- bed tramming
screenshots:
- url: /assets/img/plugins/CR10_Leveling/control.png
  alt: Control Tab
- url: /assets/img/plugins/CR10_Leveling/settings.png
  alt: Settings
featuredimage: /assets/img/plugins/CR10_Leveling/control.png
compatibility:
  python: '>=2.7, <4'
---

This plugin adds buttons to apply heat to the bed, nozzle, chamber, and move the
printing head to each of the four corners, as well as the center of
the bed.

The coordinates and temperatures can all be customized in the plugin's settings.
