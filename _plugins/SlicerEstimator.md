---
layout: plugin

id: SlicerEstimator
title: Slicer Estimator
description: Slicer Estimator - adds accurate remaining time to print, remaining time to filament changes and other custom metadata like filament brand, etc. to OctoPrint
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
- mmu
- m600
- m73

compatibility:
  python: ">=2.7,<4"
  octoprint:
  - 1.3.9

screenshots:
- url: /assets/img/plugins/SlicerEstimator/Printer_Metadata.png
  alt: OctoPrint shows that Slicer information is detected and available metadata
  caption: Slicer information detected
- url: /assets/img/plugins/SlicerEstimator/File_Metadata_Custom.png
  alt: Slicer estimation and metadata available in filelist
  caption: Slicer estimation and metadata available in filelist
- url: /assets/img/plugins/SlicerEstimator/Filament_Change.png
  alt: Filament Changes are visible in Filebrowser and actual print
  caption: Filament Changes are visible in Filebrowser and actual print
  
---

# Slicer Estimator - for an accurate remaining time to print and custom metadata in OctoPrint
With this plugin you can use the more accurate estimation of the slicer instead of OctoPrints estimations. So it will be very accurate, as the slicer created each command of the GCODE.
Also it is possible to add custom metadata to the GCODE and make it visible in OctoPrints filelist or printer state view. For example the material the GCODE is created for becomes visible inside OctoPrint. 
And if you like to know when a M600 filament change is expected or a MMU tool switch it is also shown.

The the syntax of the following slicers is known and selected automatically:

* Cura
* Simplify3D
* Creality Slicer
* PrusaSlicer
* SuperSlicer
* OctoSlicer
* Bambu Studio
* Snapmaker Luban


A more detailed description and manual is available on Github - the plugin's homepage on the right.

For plugin developers an [API description is available](https://github.com/NilsRo/OctoPrint-SlicerEstimator/blob/master/API_DOC.md) to add metadata also in other plugins.


More configurations can be added, please request additions via a [Github issue](https://github.com/NilsRo/OctoPrint-SlicerEstimator/issues).