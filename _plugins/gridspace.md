---
layout: plugin

id: gridspace
title: OctoPrint-GridSpace
description: Allows for direct printing from GridSpace's Kiri:Moto slicer
author: Stewart Allen
license: MIT

date: 2020-07-04

homepage: https://github.com/GridSpace/OctoPrint-GridSpace
source: https://github.com/GridSpace/OctoPrint-GridSpace
archive: https://github.com/GridSpace/OctoPrint-GridSpace/archive/master.zip

follow_dependency_links: false

tags:
- gcode
- spooler
- browser
- network
- slicer
- slicer print
- remote print
- print export
- print spooler

screenshots:
- url: assets/img/plugins/gridspace/Kiri-In-OctoPrint.png
  alt: Kiri:Moto Tab in OctoPrint
  caption: Kiri:Moto Tab in OctoPrint

featuredimage: assets/img/plugins/gridspace/Kiri-In-OctoPrint.png

compatibility:

  octoprint:
  - 1.3.1

  python: ">=3,<4"

---

This plugin allows for direct printing from GridSpace's Kiri:Moto slicer
to any OctoPrint servers on your local network with zero configuration.

It also adds an iframe tab to OctoPrint's interface that embeds the
Kiri:Moto web-based slicer. In addition to being a full-blown slicer,
Kiri:Moto includes gcode visualization.
