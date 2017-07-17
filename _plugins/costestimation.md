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
---

This OctoPrint plugin displays the estimated print cost for the loaded model. The print cost includes the price for the used filament and the operating cost for the printer.

The cost for the filament is calculated from the price per gramm and the provided volume needed for the print.

The operating cost is calculated from the power consumtion of the printer, the price per kWh and the estimated print time of the model.
