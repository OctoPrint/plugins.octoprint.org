---
layout: plugin

id: gcodeleveling
title: OctoPrint-GcodeLeveling
description: Leveling of Z values in Gcode using manually measured positions
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
compatibility:
  python: '>=2.7,<4'
---

# OctoPrint-GcodeLeveling

This plugin creates a model of the work surface (using the least squares method on user provided points), allowing for leveling of machines through gcode that otherwise cannot be leveled (e.g. for a grbl machine). A user just needs to measure some z values at a variety of x and y values (e.g. with the paper test), then configure a couple of settings, and the plugin will handle the leveling on file upload.

This plugin really only makes sense it you have no other way of leveling out stuff (i.e. your firmware doesn't offer that feature or you are working on a warped material).

## Gcode Support

* This plugin should be fine with most gcode since it only changes movement commands; however, for movement commands and commands that change how movement commands function (e.g. changes in relative/absolute movement) support needs to be added to the plugin.

### Supported Commands
+ `G0`
+ `G1`
+ `G2`/`G3`
    - See the note on `G17-19`
+ `M82`/`M83`

### Monitored Commands
+  `G90` `G91`
    - the plugin will not change any values in relative positioning mode
+ `G17` `G18` `G19`
    - the plugin only modifies arcs in XY workspace mode
+ `G92`
    - extruder position resets will be respected, any other position resets will stop the plugin from changing any future values on a file

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/willmac16/OctoPrint-GcodeLeveling/archive/master.zip

+ The plugin depends on numpy, so it will need to install this (if it is not already installed), which can take some time on a raspberry pi.
    - Numpy in a python3 environment requires libatlas3-base, so some instances may need to run the following to install properly
```bash
sudo apt install libatlas3-base libopenblas-dev
```

## Configuration

See the [GitHub page](https://github.com/Willmac16/OctoPrint-GcodeLeveling#configuration) for up-to-date configuration information.
