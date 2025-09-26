---
layout: plugin

id: SkipTo
title: OctoPrint-SkipTo
description: Allows to start printing a GCODE file from/at a specific layer or z-height
authors:
- awesrc
license: AGPLv3

date: 2024-08-27

homepage: https://github.com/awe-source/OctoPrint-SkipTo
source: https://github.com/awe-source/OctoPrint-SkipTo
archive: https://github.com/awe-source/OctoPrint-SkipTo/archive/master.zip

follow_dependency_links: false


tags:
- gcode
- utility
- ui
- print
- free

screenshots:
- url: /assets/img/plugins/SkipTo/screen1.png
  alt: basic screen ui changes
  caption: Plugin adds ">>" to the buttons on each file, and shows the current layer/z-height as it prints for reference purposes.
- url: /assets/img/plugins/SkipTo/screen2.png
  alt: basic screen dialog of user input
  caption: Plugin allows user to set the target height/layer to skip to.

featuredimage: /assets/img/plugins/SkipTo/skipto.png


compatibility:

  octoprint:
  - 1.4.0


  os:
  - linux
  - windows
  - macos
  - freebsd


  python: ">=3,<4"



attributes:
#  - cloud  # if your plugin requires access to a cloud to function
#  - commercial  # if your plugin has a commercial aspect to it
#  - free-tier  # if your plugin has a free tier

---

# SkipTo plugin

The SkipTo plugin for OctoPrint eases the burden of mucking around with GCODE files for the simple purpose of "restart on existing model, that failed/ran out of filament/blockage".
Enabling users to skip movements to a specific layer or Z-height within a G-code file. This functionality is particularly useful for resuming prints from a certain point, avoiding the need to start a print job from scratch if an interruption occurs. By providing a user-friendly interface to input desired layers or heights, the plugin offers a flexible and efficient way to manage and resume prints.

Tested with output from Cura, Slicer3d and PrusaSlicer.

## Questions, Comments, Or Feedback?

Contact us at [info@awesrc.com.au](info@awesrc.com.au).

![screenshot](/assets/img/plugins/SkipTo/skipto.png)
