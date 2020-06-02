---
layout: plugin

id: detailedprogress
title: Detailed Progress
description: Displays detailed progress on the LCD screen
author: tpmullan
license: AGPLv3

date: 2016-09-02

homepage: https://github.com/tpmullan/OctoPrint-DetailedProgress
source: https://github.com/tpmullan/OctoPrint-DetailedProgress
archive: https://github.com/tpmullan/OctoPrint-DetailedProgress/archive/master.zip

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
  python: ">=2.7,<4"

---

A plugin that sends M117 commands to the printer to display the progress of the print job being currently streamed. The message to display can be configured (some placeholders included).

By default, It rotates the display every 10 seconds with the following information:

- Percentage of the job's progress
- ETL - Estimated time left
- ETA - Estimated time of completion
