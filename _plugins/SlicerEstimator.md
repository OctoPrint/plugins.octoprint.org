---
layout: plugin

id: SlicerEstimator
title: Slicer Estimator
description: Slicer Estimator - add accurate remaining time to print and other custom metadata to OctoPrint
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
- url: /assets/img/plugins/SlicerEstimator/Printer_Estimation.png
  alt: OctoPrint shows that Slicer information is detected and accurate
  caption: Slicer information detected
- url: /assets/img/plugins/SlicerEstimator/File_Metadata_1.png
  alt: Update of file metadata after upload (1)
  caption: Updates estimation on upload from slicer (1)
- url: /assets/img/plugins/SlicerEstimator/File_Metadata_2.png
  alt: Update of file metadata after upload (2)
  caption: Updates estimation on upload from slicer (2)
- url: /assets/img/plugins/SlicerEstimator/File_Metadata_Custom.png
  alt: Custom metadata in filelist
  caption: Slicer information detected
- url: /assets/img/plugins/SlicerEstimator/Printer_Estimation.png
  alt: Estimation for current print
  caption: Estimation for current print
- url: /assets/img/plugins/SlicerEstimator/Printer_Metadata.png
  alt: Custom metadata for current print
  caption: Metadata for current print

  
---

# Slicer Estimator - for an accurate remaining time to print and custom metadata in OctoPrint
With this plugin you can use the more accurate estimation of the slicer instead of OctoPrints estimations. So it will be very accurate, as the slicer created each command of the GCODE.
Also it is possible to add custom metadata to the GCODE and make it visible in OctoPrints filelist or printer state view. For example the material the GCODE is created for become visible inside OctoPrint.

The default configuration matches the syntax of the following slicers, but you can change it in the plugins custom settings according your needs.

* Cura
* Cura M117
* Simplify3D
* PrusaSlicer


A more detailed description and manual is available on Github - the plugin's homepage on the right.


More configurations can be added, please request additions via a [Github issue](https://github.com/NilsRo/OctoPrint-SlicerEstimator/issues).