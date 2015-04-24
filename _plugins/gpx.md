---
layout: plugin
id: gpx
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
featuredimage: https://markwal.github.io/OctoPrint/gpx.png
---

GPX was created by Dr. Henry Thomas in April 2013.  It is a post processing
utility that converts gcode into x3g files for printing on MakerBots or their
clones.

This plugin wraps the serial communication layer and uses GPX to translate between
gcode and x3g on the fly to make the printer appear to OctoPrint as if it speaks
gcode.

###Configuration
After installing, you need to tell gpx about your printer.  The easiest way is to
copy the gpx.ini you've been using with your slicer to the octoprint plugin folder.
There's a sample gpx.ini included in the plugin that you can edit if you like.

    mkdir ~/.octoprint/plugins
    cp gpx.ini ~/.octoprint/plugins

It's my intention to allow most of those settings to be set via OctoPrint settings
UI, but haven't got there yet.

###Caveats and Known Issues
Please see the [README](https://github.com/markwal/OctoPrint-GPX/blob/master/README.md)
on github for the latest info.

###Pic
![GPX](https://markwal.github.io/OctoPrint/gpx.png)
