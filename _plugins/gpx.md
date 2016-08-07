---
layout: plugin
id: GPX
title: GPX
description: Use OctoPrint with s3g/x3g printers (like FlashForge and older MakerBot)
archive: https://markwal.github.io/OctoPrint/OctoPrint-GPX.tar.gz
homepage: https://github.com/markwal/OctoPrint-GPX
source: https://github.com/markwal/OctoPrint-GPX
author: Mark Walker
license: AGPLv3
date: 2015-04-23
tags:
- printer
- protocol
screenshots:
- alt: GPX
  url: https://markwal.github.io/OctoPrint/gpx.png
featuredimage: https://markwal.github.io/OctoPrint/gpx.png
compatibility:
  octoprint:
  - 1.2.0
  os:
  - linux
---

GPX was created by Dr. Henry Thomas in April 2013.  It is a post processing
utility that converts gcode into x3g files for printing on MakerBots or their
clones.

This plugin wraps the serial communication layer and uses GPX to translate between
gcode and x3g on the fly to make the printer appear to OctoPrint as if it speaks
gcode.

###Configuration
After installing, you need to tell gpx about your printer. In OctoPrint, GPX
adds a settings panel. Two settings are important to set: the type of
printer and the gcode flavor.

The type of printer determines the steps per mm. Gcode is generally in
millimeters and x3g is in stepper motor steps.

Gcode flavor means the flavor that your slicer produces. Makerbot Desktop and
RepG only produce MakerBot flavor. Slic3r produces either (you can choose in
its settings) and Cura produces RepRap flavor.

If you have a MakerBot clone then you have a Replicator 1 or Replicator 1 Dual
clone. Your printer might look more like a Replicator 2 because it is black and
metal, but its steps per mm is Replicator 1.

###Caveats and Known Issues
Please see the [README](https://github.com/markwal/OctoPrint-GPX/blob/master/README.md)
on github for the latest info.
