---
layout: plugin

id: print_eta
title: Print ETA
description: An OctoPrint plugin that shows you the time that a print job is estimated to finish.
authors:
- Lewis Bennett
license: APGLv3

date: 2021-05-03

homepage: https://github.com/lewisbennett/OctoPrint-Print-ETA
source: https://github.com/lewisbennett/OctoPrint-Print-ETA
archive: https://github.com/lewisbennett/OctoPrint-Print-ETA/archive/master.zip

tags:
- time
- eta
- finish time

screenshots:
- url: url of a screenshot, /assets/img/plugins/print_eta/screenshot.png
  alt: ETA for current print job.
  caption: ETA for current print job.

featuredimage: /assets/img/plugins/print_eta/screenshot.png

compatibility:

  octoprint:
  - 1.3.6

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=2.7,<4"

---

## Print ETA

Print ETA shows the ETA of your current print job within OctoPrint, and on your printer's screen (if enabled).

The ETA is updated constantly throughout the print. For increased accuracy, use the [PrintTimeGenius plugin](https://plugins.octoprint.org/plugins/PrintTimeGenius/).

### Note

A valid time zone must be configured on the host, otherwise times will be displayed in UTC.
