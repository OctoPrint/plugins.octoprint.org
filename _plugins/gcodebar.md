---
layout: plugin

id: gcodebar
title: GCodeBar
description: Send GCode from the sidebar
author: Markus Towara
license: AGPLv3

date: 2016-09-01

homepage: https://github.com/mtowara/OctoPrint-Gcodebar
source: https://github.com/mtowara/OctoPrint-Gcodebar
archive: https://github.com/mtowara/OctoPrint-Gcodebar/archive/master.zip

follow_dependency_links: false

tags:
- gcode
- control
- sidebar

screenshots:
- url: /assets/img/plugins/gcodebar/gcodebar.png
  alt: Screenshot
  caption: Send Custom GCodes

featuredimage: /assets/img/plugins/gcodebar/gcodebar.png

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

# GcodeBar

Plugin for Octoprint to allow sending GCode commands from the sidebar.

## Features:
- Hooks into the Terminal Tab and uses same history (scrollable with up / down keys)
- Send multiple commands seperated by semicolons
- User needs to be logged in and connected to printer to send commands

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/mtowara/OctoPrint-Gcodebar/archive/master.zip
