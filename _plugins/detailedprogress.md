---
layout: plugin

id: detailedprogress
title: Detailed Progress
description: Displays detailed progress on the LCD screen
author: Dattas Moonchaser
license: AGPLv3

date: 2016-09-02

homepage: https://github.com/dattas/OctoPrint-DetailedProgress
source: https://github.com/dattas/OctoPrint-DetailedProgress
archive: https://github.com/dattas/OctoPrint-DetailedProgress/archive/master.zip

follow_dependency_links: false

tags:
- display
- lcd
- printer
- progress

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

A plugin that sends M117 commands to the printer to display the progress of the print job being currently streamed. The message to display can be configured (some placeholders included).

By default, It rotates the display every 10 seconds with the following information:

- Percentage of the job's progress
- ETL - Estimated time left
- ETA - Estimated time of completion
