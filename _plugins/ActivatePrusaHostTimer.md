---
layout: plugin

id: ActivatePrusaHostTimer
title: Activate Prusa HostTimer
description: Plugin for Octoprint to activate Prusa host features
author: sarusani
license: AGPLv3

date: 2023-12-01

homepage: https://github.com/sarusani/OctoPrint-ActivatePrusaHostTimer
source: https://github.com/sarusani/OctoPrint-ActivatePrusaHostTimer
archive: https://github.com/sarusani/OctoPrint-ActivatePrusaHostTimer/archive/master.zip

follow_dependency_links: false

tags:
- prusa

compatibility:
  # List of compatible versions
  octoprint:
  - 1.3.0

  # List of compatible operating systems
  os:
  - linux
  - windows
  - macos
  - freebsd

  # Compatible Python version
  python: ">=3.7,<4"
---

# Activate Prusa HostTimer

Plugin for Octoprint to activate Prusa host features.

Features:
- Sends M79 S"OP" to printer every x seconds
- Interval is configurable (5,10,15,20 or 25 seconds)
- Interval can be paused

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/sarusani/OctoPrint-ActivatePrusaHostTimer/archive/master.zip
