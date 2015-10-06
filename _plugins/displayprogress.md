---
layout: plugin

id: displayprogress
title: DisplayProgress
description: Displays the print progress on the printer's display
author: Gina Häußge
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
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.0

  # list of compatible operating systems, valid values are linux, windows, macos, leaving empty defaults to all
  os:
  - linux
  - windows
  - macos
---

A plugin that sends `M117` commands to the printer to display the progress
of the print job being currently streamed. The message to display can be
configured (some placeholders included). By default, an ASCII progress bar
is rendered with the percentage of the job's progress.
