---
layout: plugin

id: cnc_gcodeviewer
title: CNC GCode Viewer
description: GCode Viewer for CNC toolpaths with no extrusions
authors:
- Jamie Kawabata
license: AGPLv3

date: 2022-03-03

homepage: https://github.com/vector76/cnc_gcodeviewer
source: https://github.com/vector76/cnc_gcodeviewer
archive: https://github.com/vector76/cnc_gcodeviewer/archive/main.zip

tags:
- marlin
- cnc

featuredimage: /assets/img/plugins/cnc_gcodeviewer/crown_screen_shot.png

compatibility:
  octoprint:
  - 1.4.1
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=2.7,<4"

---

This viewer adds support for CNC toolpaths, which have no extrusions.  
This plugin is based \(very\) heavily on the native OctoPrint GCode Viewer, which does not show jobs that have no extrusions.
This plugin has been tested primarily with Marlin-flavored gcode.

## Screen Shot

![Crown Screen Shot](/assets/img/plugins/cnc_gcodeviewer/crown_screen_shot.png)

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/vector76/cnc_gcodeviewer/archive/main.zip

Note: this plugin replaces the native Octoprint GCode Viewer within the UI.  Disable this plugin to restore the default behavior.
