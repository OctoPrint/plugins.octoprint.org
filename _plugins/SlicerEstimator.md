---
layout: plugin

id: SlicerEstimator
title: Slicer Estimator
description: Slicer Estimator - read accurate remaining time to print and other custom metadata embedded in the GCODE file by the slicer
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
- metadata
- progress
- eta
- analysis
- cura
- prusaslicer
- finish time
- filament
- file manager
- gcode

compatibility:
  python: ">=2.7,<4"
  octoprint:
  - 1.3.9

screenshots:
- url: /assets/img/plugins/SlicerEstimator/OctoPrint-estimator_dot.png
  alt: OctoPrint shows that Slicer information is detected and accurate
  caption: Slicer information detected
- url: /assets/img/plugins/SlicerEstimator/file_metadata1.png
  alt: Update of file metadata after upload (1)
  caption: Updates estimation on upload from slicer (1)
- url: /assets/img/plugins/SlicerEstimator/file_metadata2.png
  alt: Update of file metadata after upload (2)
  caption: Updates estimation on upload from slicer (2)
- url: /assets/img/plugins/SlicerEstimator/file_custom_metadata.png
  alt: Custom metadata in filelist
  caption: Slicer information detected
- url: /assets/img/plugins/SlicerEstimator/Settings_Basic.png
  alt: OctoPrint selection of the Slicer
  caption: OctoPrint Basic Settings
- url: /assets/img/plugins/SlicerEstimator/Settings_Custom.png
  alt: OctoPrint Custom Settings
  caption: OctoPrint Custom Settings
- url: /assets/img/plugins/SlicerEstimator/Gcode.png
  alt: Gcode
  caption: Gcode
---

# Slicer Estimator - for an accurate remaining time to print and custom metadata shown in the filelist
With this plugin you can use the more accurate estimation of time remaining of the slicer instead of Octoprints estimations. So it will be very accurate, as the slicer created each command of the GCODE.
Also it is possible to add custom metadata to the GCODE and make it visible in Octoprints filelist like material type provided by Cura.

The default configuration matches the syntax of the following slicers, but you can change it in the plugins custom settings according your needs.

* Cura
* Cura M117
* Simplify3D
* PrusaSlicer


A more detailed description and manual is available on Github - the plugin's homepage on the right.


More configurations can be added, please request additions via a [Github issue](https://github.com/NilsRo/OctoPrint-SlicerEstimator/issues).