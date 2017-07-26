---
layout: plugin

id: costestimation
title: CostEstimation
description: Displays the estimated print cost for the loaded model
author: Sven Lohrmann
license: AGPLv3
date: 2017-07-16
homepage: https://github.com/malnvenshorn/OctoPrint-CostEstimation
source: https://github.com/malnvenshorn/OctoPrint-CostEstimation
archive: https://github.com/malnvenshorn/OctoPrint-CostEstimation/archive/master.zip
compatibility:
  octoprint:
  - 1.2.14
tags:
- cost
- ui
screenshots:
- url: /assets/img/plugins/costestimation/costestimation.png
  alt: Cost
  caption: Sample view of estimated print cost in the sidebar
- url: /assets/img/plugins/costestimation/costestimation.png
  alt: FilamentManager
  caption: Dialog to manage filament profiles
- url: /assets/img/plugins/costestimation/costestimation_settings.png
  alt: Settings
  caption: Settings dialog to configure the print cost
---

This OctoPrint plugin displays the estimated print cost for the loaded model. The print cost includes the price for the used filament and the operating cost for the printer.

**Features**
- Calculation based on the provided length or volume
- Customizable currency symbol
- Support for filament profiles
- Support for multiple extruders
