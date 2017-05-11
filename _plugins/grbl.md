---
layout: plugin

id: octoprint-grbl-plugin
title: Grbl support for OctoPrint
description: Support Grbl style GCODE for using CNCs and Laser engravers with OctoPrint.
author: mic159
license: MIT

# today's date in format YYYY-MM-DD, e.g.
date: 2017-05-11

homepage: https://github.com/mic159/octoprint-grbl-plugin
source: https://github.com/mic159/octoprint-grbl-plugin
archive: https://github.com/mic159/octoprint-grbl-plugin/archive/1.0.0.zip

tags:
- grbl
- CNC
- Laser
- GCODE
- protocol

featuredimage: /assets/img/plugins/grbl/Grbl_logo.png

compatibility:
  octoprint:
  - 1.3.0

---

This plugin modifies the gcode sent and recieved to translate what is needed.

**NOTE** Additional configuration required:

- _Serial Connection_ > _Advanced options_ > _"Hello" command_ = **M5**
- _Features_ > _Send a checksum with the command_ > **Never**
