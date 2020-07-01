---
layout: plugin

id: displayz
title: DisplayZ
description: Brings back the current Z display in the state sidebar panel
author: Gina Häußge
license: AGPLv3

date: 2015-09-22

homepage: https://github.com/foosel/OctoPrint-DisplayZ
source: https://github.com/foosel/OctoPrint-DisplayZ
archive: https://github.com/foosel/OctoPrint-DisplayZ/archive/master.zip

follow_dependency_links: false

tags:
- ui
- addon

screenshots:
- url: /assets/img/plugins/displayz/displayz.png
  alt: Screenshot of DisplayZ plugin
  caption: Screenshot of the plugin

featuredimage: /assets/img/plugins/displayz/displayz.png

compatibility:
  python: ">=2.7,<4"
  octoprint:
  - 1.2.0
  
abandoned: https://github.com/foosel/OctoPrint-DisplayZ/issues/7
  
---

OctoPrint's state sidebar display panel used to display the current Z height
of the printer's nozzle.

That information is sadly inaccurate - it stems not from [actual position information](https://github.com/foosel/OctoPrint/wiki/FAQ#why-doesnt-octoprint-show-me-the-current-hotend-position-anywhere)
from the printer's firmware but instead from an attempt at tracking the height
information by OctoPrint, which can lag behind, be inaccurate or not work 
at all in case of prints from SD cards.

However, people demanded to get this piece of  information back, inaccurate or
not, so here it is as plugin.
