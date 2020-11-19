---
layout: plugin

id: costestimation
title: CostEstimation
description: Displays the estimated print cost for the loaded model
authors:
- Sven Lohrmann
- Olli
license: AGPLv3
date: 2017-07-16
homepage: https://github.com/OllisGit/OctoPrint-CostEstimation
source: https://github.com/OllisGit/OctoPrint-CostEstimation
archive: https://github.com/OllisGit/OctoPrint-CostEstimation/releases/latest/download/master.zip
compatibility:
  python: ">=2.7,<4"
  octoprint:
  - 1.2.14
  - 1.3.6
  - 1.4.0
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

This OctoPrint plugin displays the estimated print cost for the loaded model. The print cost includes the price for the used filament the maintenance and operating cost for the printer as well as the depreciation of the printer.

#### Features

- Calculation based on the provided filament length
- Customizable currency symbol
- Hide cost if not logged in (optional)
- Support for multiple extruders
- Support for filament profiles with [Filament Manager Plugin](/plugins/filamentmanager)
