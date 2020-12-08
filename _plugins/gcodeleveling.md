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

The Polynomial Degree determines how detailed and curvy the model of the surface will be.
The degree should be kept as low as possible to avoid issues between test points.

The Minimum and Maximum z values are used to check for positions that could damage your machine.
These values should be safe to move to with a <code>G0</code> command.
If the plugin detects that a movement would fall outside this range, then the file upload will display an error and you should consider changing the configuration.

The invert option determines how the original positions and the gcode positions should be combined.
If you want positive gcode values to move the toolhead up and the toolhead is at the work surface at a negative, then do not enable the invert option.
If positive movement moves the toolhead down, but you want a positive value in the gcode to move up then enable the invert option.

The Line break up option breaks up long moves into shorter ones that follow the height model.
Set the distance to 0.0 to disable this feature; otherwise, all moves longer than the specified length will be broken into smaller moves.

The calibration points are used to create a model of the surface.
Enter the x and y coordinate, then the observed z coordinate.
