---
layout: plugin
    
id: cost
title: Cost estimator
description: When a file is loaded to be printed, it will display the estimated cost of printing.
author: Jan Szumiec
license: MIT
date: 2016-06-11
homepage: https://github.com/jasiek/OctoPrint-Cost
source: https://github.com/jasiek/OctoPrint-Cost
archive: https://github.com/jasiek/OctoPrint-Cost/archive/master.zip
follow_dependency_links: false
tags:
- helper
- cost
screenshots: 
- url: /assets/img/plugins/cost/screenshot.png
  alt: Screenshot.
  caption: Sample view.
compatibility:
  octoprint:
  - 1.2.0
---

This plugin will display the estimated cost of the print based on filament cost per meter, and
expected printing time.

These variables can be set via settings from an admin account. Estimating how much a meter of
filament costs, is trivial. For hourly running costs, refer to your printer's manual, or use
a power meter to estimate power consumption in kWh and then simply multiply by the cost of
1kWh as billed to you by your electricity provider.
