---
layout: plugin

id: DisplayLayerProgress
title: Display 
description: Displays the current processing layer and the percentage in "Printer-Display" and in top "NavBar"
author: Olli
license: AGPLv3

date: 2018-04-09

homepage: https://github.com/OllisGit/OctoPrint-DisplayLayerProgress
source: https://github.com/OllisGit/OctoPrint-DisplayLayerProgress
archive: https://github.com/OllisGit/OctoPrint-DisplayLayerProgress/archive/master.zip

follow_dependency_links: false

tags:
- display
- lcd
- printer
- progress
- layer

screenshots:
- url: /assets/img/plugins/detailedprogress/example-percent.jpg
  alt: Example of percentage
  caption: Example of percentage
- url: /assets/img/plugins/detailedprogress/example-etl.jpg
  alt: Example of estimated time left
  caption: Example of estimated time left
- url: /assets/img/plugins/detailedprogress/example-eta.jpg
  alt: Example of estimated time of completition
  caption: Example of estimated time of completition

featuredimage: /assets/img/plugins/detailedprogress/example-eta.jpg

---

TODO add screenshots

A OctoPrint-Plugin that sends the current progress of a print via M117 command to the printer-display and also to the top navigation bar.
It shows the percentage, the current layer and the total layer count:

- Printer Display: 50% 60/120
- NavBar: Process: 50% Layer: 60/120

For implementation details please visit the homepage.

ATTENTION: The layer information output only works with Cura generated G-Code, because Cura insert the layer information (layer, layerCount) as comments in the file.