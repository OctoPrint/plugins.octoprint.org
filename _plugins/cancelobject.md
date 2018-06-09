---
layout: plugin

id: cancelobject
title: OctoPrint-Cancelobject
description: Cancel single objects during a print based on gcode comment lines
author: Paul Paukstelis
license: AGPLv3

date: 2018-06-08

homepage: https://github.com/paukstelis/OctoPrint-Cancelobject
source: https://github.com/paukstelis/OctoPrint-Cancelobject
archive: https://github.com/paukstelis/OctoPrint-Cancelobject/archive/master.zip


tags:
- server
- control
- navbar
- ui

screenshots:
- url: /assets/img/plugins/cancelobject/cancelobject.png
  alt: Screenshot example
  caption: Screenshot example

featuredimage: /assets/img/plugins/cancelobject/cancelobject.png


---

This plugin allows the user cancel single objects (or groups of objects) during a print while
allowing the remaining objects to print normally. Currently, this functionality is limited to gcode
sliced with Simplify3D using a unique process for each object (or group of objects). Regular expression
settings will allow this to be used with other slicers if/when they include object-specific comments in gcode.
