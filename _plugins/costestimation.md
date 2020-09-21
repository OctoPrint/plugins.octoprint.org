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
- url: /assets/img/plugins/costestimation/costestimation_settings.png
  alt: Settings
  caption: Settings dialog to configure the print cost

abandoned: https://github.com/OctoPrint/plugins.octoprint.org/issues/623
  
---

This OctoPrint plugin displays the estimated print cost for the loaded model. The print cost includes the price for the used filament the maintenance and operating cost for the printer as well as the depreciation of the printer.

#### Features

- Calculation based on the provided filament length
- Customizable currency symbol
- Hide cost if not logged in (optional)
- Support for multiple extruders
- Support for filament profiles with [Filament Manager Plugin](/plugins/filamentmanager)
