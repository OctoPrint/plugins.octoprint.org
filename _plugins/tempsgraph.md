---
layout: plugin

id: tempsgraph
title: OctoPrint-Tempsgraph
description: Replaces the temperature graph with an interactive and zoomable one
author: Robin Vanhove
license: MIT

date: 2017-03-29

homepage: https://github.com/1r0b1n0/OctoPrint-Tempsgraph
source: https://github.com/1r0b1n0/OctoPrint-Tempsgraph
archive: https://github.com/1r0b1n0/OctoPrint-Tempsgraph/archive/master.zip

follow_dependency_links: false

tags:
- interactive graph
- temperature plot
- zoom
- ui

# TODO
screenshots:
- url: /assets/img/plugins/tempsgraph/hover.png
  alt: hover
- url: /assets/img/plugins/tempsgraph/zoom.png
  alt: zoom

# TODO
featuredimage: /assets/img/plugins/tempsgraph/zoom.png

compatibility:
  octoprint:
  - 1.3.2

---

This plugin adds some functionaly to the temperature graph :
* exact values on hover
* zooming
* panning
* export

## Usage :
* hover over the graph to show date and temperatures under the cursor
* drag to zoom
* shift + drag to pan
* double click to reset axes / autoscale
