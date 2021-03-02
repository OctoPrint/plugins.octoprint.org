---
layout: plugin

id: SlicerEstimator
title: Slicer Estimator
description: Slicer Estimator is a generic implemenation to read accurate remaining time to print embedded in the GCODE file by the slicer
author: Nils Hendrik Rottgardt
license: AGPLv3
date: 2021-02-24
homepage: https://github.com/NilsRo/OctoPrint-SlicerEstimator
source: https://github.com/NilsRo/OctoPrint-SlicerEstimator
archive: https://github.com/NilsRo/OctoPrint-SlicerEstimator/archive/master.zip
follow_dependency_links: false

tags:
- helper
- estimator
- estimation
- time
- print time

compatibility:
  python: ">=2.7,<4"

screenshots:
- url: /assets/img/plugins/SlicerEstimator/Gcode.png
  alt: Gcode
  caption: Gcode
- url: /assets/img/plugins/SlicerEstimator/Settings_Basic.png
  alt: OctoPrint selecion of the Slicer
  caption: OctoPrint Basic Settings
- url: /assets/img/plugins/SlicerEstimator/Settings_Custom.png
  alt: OctoPrint Custom Settings
  caption: OctoPrint Custom Settings
- url: /assets/img/plugins/SlicerEstimator/Cura.png
  alt: Cura Settings
  caption: Cura Settings  
---

# Slicer Estimator - for an accurate remaining time to print
With this plugin you can use the more accurate estimation of time remaining of the slicer instead of Octoprints estimations. So it will be very accurate, as the slicer created each command of the GCODE. Thanks to arhi for the idea and first implementation.

The default configuration matches the syntax of the following slicers, but you can change it in the plugins custom settings according your needs.

* Cura
* Cura M117
* Simplify3D
* PrusaSlicer


A more detailed description and manual is available on Github - the plugin's homepage on the right.


More configurations can be added, please request additions via a [Github issue](https://github.com/NilsRo/OctoPrint-SlicerEstimator/issues).