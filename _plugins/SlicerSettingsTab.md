---
layout: plugin

id: SlicerSettingsTab
title: OctoPrint-SlicerSettingsTab
description: Adds tab which displays slicer settings of selected gcode file.
authors:
- Larsjuhw
- T6
license: AGPLv3

date: 2018-12-22

homepage: https://github.com/larsjuhw/OctoPrint-SlicerSettingsTab
source: https://github.com/larsjuhw/OctoPrint-SlicerSettingsTab
archive: https://github.com/larsjuhw/OctoPrint-SlicerSettingsTab/archive/master.zip

tags:
- gcode
- analysis
- slicer settings

screenshots:
- url: /assets/img/plugins/SlicerSettingsTab/main.png
  alt: Picture of tab
- url: /assets/img/plugins/SlicerSettingsTab/filtered.png
  alt: Picture of filtered tab

featuredimage: /assets/img/plugins/SlicerSettingsTab/main.png

compatibility:

  # Untested on previous versions

  octoprint:
  - 1.3.10

  # Doesn't work on Windows
  # Unsure about MacOS

  os:
  - nix

---

This plugin requires also installing [SlicerSettingsParser](/plugins/SlicerSettingsParser)
or another plugin that adds a metadata dict under `slicer_settings`.

You can pin a setting to the top by clicking on the setting text.