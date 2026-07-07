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
  - 1.4.0
  python: ">=3.7,<4"

---

This plugin adds a 3D GCode visualizer tab in Octoprint. It displays colored lines to give you some idea what the printer is doing and animates progress during printing.

## Features

- 3D G-code visualizer
- Paths color-coded by slicer feature (perimeters, infill, support, skirt…)
- Layer slider to scrub through the model
- Syncs to the print job with an animated nozzle
- Temperature status bar
- Tabbed, maximized and fullscreen views
- Resizable webcam inset and [Dashboard](https://plugins.octoprint.org/plugins/dashboard/) plugin window (if installed)
- Many view options, e.g. dark mode, mirror reflection on bed's plate, antialiasing and idle auto-orbit

## Bugs reporting

Report bugs via the [GitHub Issues tab](https://github.com/jacopotediosi/OctoPrint-PrettyGCode/issues).

## Support the project

This project is distributed for free and maintained entirely by volunteers, who do their best to develop it in their spare time, gather feedback and reports from users, and fix issues.

If you'd like to support the maintainers of this project, you can donate via the [GitHub Sponsor page](https://github.com/sponsors/jacopotediosi) ❤️.
