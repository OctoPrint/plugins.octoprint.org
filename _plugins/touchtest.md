---
layout: plugin

id: touchtest
title: Touchtest Bed Leveling
description: A simple tool to move the extruder to different touch points around the perimeter of the print bed. Useful for bed leveling.
author: Daniel Miller
license: AGPLv3

date: 2017-03-05

homepage: https://github.com/Peaches491/OctoPrint-Touchtest
source: https://github.com/Peaches491/OctoPrint-Touchtest
archive: https://github.com/Peaches491/OctoPrint-Touchtest/archive/master.zip

follow_dependency_links: false

tags:
- ui
- control
- calibration
- leveling
- sidebar

screenshots:
- url: /assets/img/plugins/touchtest/example.png
  alt: Screenshot of Touchtest sidebar panel
  caption: Touchtest sidebar panel
  
compatibility:
  python: ">=2.7,<4"

featuredimage: /assets/img/plugins/touchtest/example.png
---

Touch Test plugin for OctoPrint adds a new sidebar panel, essential for manual bed leveling.
A simple 3x3 grid of buttons allows the user to move the printhead to all 4 corners and edges of the printbed, where you can perfotm "the paper test".

More info at: https://github.com/Peaches491/OctoPrint-Touchtest
