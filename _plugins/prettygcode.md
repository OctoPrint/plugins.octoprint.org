---
layout: plugin

id: prettygcode
title: OctoPrint-PrettyGCode
description: A 3D G-code visualizer
authors:
    - Jacopo Tediosi
    - Kragrathea
license: AGPLv3

date: 2020-08-17

homepage: https://github.com/jacopotediosi/OctoPrint-PrettyGCode
source: https://github.com/jacopotediosi/OctoPrint-PrettyGCode
archive: https://github.com/jacopotediosi/OctoPrint-PrettyGCode/archive/master.zip

privacypolicy: https://github.com/jacopotediosi/OctoPrint-PrettyGCode/blob/master/PRIVACY.md

tags:
- 3d
- gcode
- monitor
- monitoring
- preview
- print status
- printing
- progress
- visualization
- visualizer
- webgl

screenshots:
- url: /assets/img/plugins/prettygcode/screen_1.jpg
  alt: PrettyGCode
  caption: PrettyGCode

featuredimage: /assets/img/plugins/prettygcode/screen_1.jpg

compatibility:
  octoprint:
  - 1.9.0
  python: ">=3.7,<4"

---

This plugin adds a 3D GCode visualizer tab in Octoprint. It displays colored lines to give you some idea what the printer is doing and animates progress during printing.

## Features

### 3D Visualization
- Interactive 3D G-code visualizer, with a view cube to orient the camera and perspective/orthographic projection
- Paths colored by slicer feature (perimeters, infill, support, skirt...), with built-in presets for popular slicers, or your own custom colors
- Layer and segment sliders to scrub through the model
- Belt printers are supported too, with a customizable gantry angle

### Print monitoring
- While printing, the view syncs to the print job with an animated nozzle
- Temperature status bar
- Resizable webcam inset

### Interface & appearance
- Tabbed, maximized and fullscreen views
- Many view options, e.g. dark mode, customizable nozzle marker, mirror reflection on the bed, antialiasing...

### Other plugin integrations
- [Exclude Region](https://plugins.octoprint.org/plugins/excluderegion/) and [Cancel Object](https://plugins.octoprint.org/plugins/cancelobject/): to grey-out or hide the excluded parts of your model
- [Dashboard](https://plugins.octoprint.org/plugins/dashboard/): to show the Dashboard in a resizable inset within the 3D view

## Bugs reporting

Report bugs via the [GitHub Issues tab](https://github.com/jacopotediosi/OctoPrint-PrettyGCode/issues).

## Support the project

This project is distributed for free and maintained entirely by volunteers, who do their best to develop it in their spare time, gather feedback and reports from users, and fix issues.

If you'd like to support the maintainers of this project, you can donate via the [GitHub Sponsor page](https://github.com/sponsors/jacopotediosi) ❤️.
