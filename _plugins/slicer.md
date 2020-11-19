---
layout: plugin

id: slicer
title: Full-featured Slicer
description: A full-blown GUI-based slicer. Rotate and scale model; slice multiple STL files at a time; set layer height and other slicing settings.
author: Kenneth Jiang
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2016-09-22

homepage: https://github.com/kennethjiang/OctoPrint-Slicer
source: https://github.com/kennethjiang/OctoPrint-Slicer
archive: https://github.com/kennethjiang/OctoPrint-Slicer/archive/master.zip

# set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false

tags:
- slicer
- gcode
- stl

screenshots:
- url: /assets/img/plugins/slicer/screenshot1.png
  alt: Move, Rotate, Scale
  caption: Move, Rotate, Scale
- url: /assets/img/plugins/slicer/screenshot2.png
  alt: Overhang and lay flat
  caption: Overhang and lay flat
- url: /assets/img/plugins/slicer/screenshot3.png
  alt: Basic settings
  caption: Basic settings
- url: /assets/img/plugins/slicer/screenshot4.png
  alt: Advanced settings
  caption: Advanced settings

featuredimage: /assets/img/plugins/slicer/screenshot1.png

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.14

abandoned: https://github.com/OctoPrint/plugins.octoprint.org/issues/572

---

Slicer plugin offers useful features that OctoPrint's built-in slicer doesn't have:

- Rotate, scale, and move STL models.
- Slice multiple STLs at a time. Split 1 STL into unconnected parts.
- Circular print bed support (do you have a delta printer?).
- High-light overhang areas. Automatically orient the model for better result ("lay flat").
- Slice based on Cura profiles you upload to OctoPrint.
- Customizable slicing settings, including Basic (layer height, bed temperature ...) and Advanced (print speed, start/end G-code ...).
- Slic3r support (when Slic3r plugin is installed).
- More is coming...
