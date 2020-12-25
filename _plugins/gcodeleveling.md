---
layout: plugin

id: gcodeleveling
title: OctoPrint-GcodeLeveling
description:  Leveling of Z values in Gcode using manually measured positions
authors:
- Will MacCormack
license: AGPLv3

date: 2020-11-29

homepage: https://github.com/willmac16/OctoPrint-GcodeLeveling
source: https://github.com/willmac16/OctoPrint-GcodeLeveling
archive: https://github.com/willmac16/OctoPrint-GcodeLeveling/archive/master.zip


tags:
- leveling
- gcode
- manual bed leveling
- grbl
- cnc

screenshots:
- url: /assets/img/plugins/gcodeleveling/point-entry.png
  alt: the point entry in settings
  caption: Gcode Leveling Point Entry

featuredimage: /assets/img/plugins/gcodeleveling/point-entry.png
---

# Gcode Leveling

This plugin creates a model of the work surface (using the least squares method on user provided points), allowing for leveling of machines through gcode that otherwise cannot be leveled (e.g. for a grbl machine). A user just needs to measure some z values at a variety of x and y values (e.g. with the paper test), then configure a couple of settings, and the plugin will handle the leveling on file upload.

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/willmac16/OctoPrint-GcodeLeveling/archive/master.zip

+ The plugin depends on numpy, so it will need to install this (if it is not already installed), which can take some time on a raspberry pi.
    - Numpy in a python3 environment requires libatlas3-base, so some instances may need to run ```sudo apt install libatlas3-base``` to install properly.

## Configuration

See the [GitHub page](https://github.com/Willmac16/OctoPrint-GcodeLeveling#configuration) for up-to-date configuration information.
