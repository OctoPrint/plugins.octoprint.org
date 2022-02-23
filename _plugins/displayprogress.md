---
layout: plugin

id: displayprogress
title: DisplayProgress
description: Displays the print progress on the printer's display
authors:
- jneilliii
- Gina Häußge
license: AGPLv3

date: 2015-08-03

homepage: https://github.com/OctoPrint/OctoPrint-DisplayProgress
source: https://github.com/OctoPrint/OctoPrint-DisplayProgress
archive: https://github.com/OctoPrint/OctoPrint-DisplayProgress/archive/master.zip

tags:
- printer
- display
- lcd
- progress

screenshots:
- url: /assets/img/plugins/displayprogress/example.jpg
  alt: Example of operation
  caption: Example of operation

featuredimage: /assets/img/plugins/displayprogress/example.jpg

compatibility:
  python: ">=2.7,<4"

---

A plugin that sends `M117` commands to the printer to display the progress
of the print job being currently streamed. The message to display can be
configured (some placeholders included). By default, an ASCII progress bar
is rendered with the percentage of the job's progress.
