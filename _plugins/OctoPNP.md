---
layout: plugin

id: OctoPNP
title: OctoPNP
description: OctoPrint plugin for camera based pick 'n place operations
author: Florens Wasserfall
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2017-05-19

homepage: https://github.com/platsch/OctoPNP
source: https://github.com/platsch/OctoPNP
archive: https://github.com/platsch/OctoPNP/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- pick and place
- printer
- control
- camera
- external objects

screenshots:
- url: /assets/img/plugins/OctoPNP/screenshot.png
  alt: screenshot of OctoPNP after completing a placing opereation
  caption: Main dialog for SMD placing operations.
- url: /assets/img/plugins/OctoPNP/screenshot_settings.png
  alt: screenshot of OctoPNP settings dialog.
  caption: Camera supported interactive calibration in the settings dialog.

featuredimage: /assets/img/plugins/OctoPNP/screenshot.png
---

OctoPNP is an extension that allows Octoprint to control printers and similar devices with additional hardware for handling of SMD-parts (and potentially arbitrary objects). It currently requires the following hardware extensions:

* A Tray consisting of a grid of boxes to store SMD parts in a defined position
* A head camera to locate the exact part position on the tray
* A (second) bed camera to precisely align the parts during the placing operation
* A vacuum nozzle to grip parts

OpenCV is used for the image processing part to measure exact positions and rotations of objects for accurate placing.

For details and documentation please refer to the project's github [repository](https://github.com/platsch/OctoPNP).

This plugin is developed during a research [project](https://tams.informatik.uni-hamburg.de/research/3d-printing/conductive_printing/index.php) for integrated printing of electronics (wires and SMD-components) with FDM-printers.

The development branch of the Slic3r extensions for routing circuits in a 3D-object by importing EAGLE schematics can be found at [https://github.com/platsch/Slic3r/tree/electronics](https://github.com/platsch/Slic3r/tree/electronics).
