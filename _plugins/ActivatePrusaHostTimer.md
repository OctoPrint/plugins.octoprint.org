---
layout: plugin

id: ActivatePrusaHostTimer
title: Activate Prusa HostTimer
description: OctoPrint plugin to activate Prusa host features.
author: sarusani
license: AGPLv3

date: 2023-12-01

homepage: https://github.com/sarusani/OctoPrint-ActivatePrusaHostTimer
source: https://github.com/sarusani/OctoPrint-ActivatePrusaHostTimer
archive: https://github.com/sarusani/OctoPrint-ActivatePrusaHostTimer/archive/master.zip

follow_dependency_links: false

tags:
- prusa
- prusa buddy
- prusa mk3s
- prusa mini
- prusa mk4
- prusa xl
- m79

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

OctoPrint plugin to activate Prusa host features.

### Main Features
- Sends M79 S"OP" to the printer in configurable intervals (5, 10, 15, 20 or 25 seconds)
- Interval ping can be paused
- Intercept action commands intended for PrusaLink and trigger corresponding OctoPrint features (if available)
- Printer notifications

Supported printer models:<br />
[MK3S/+](https://github.com/prusa3d/Prusa-Firmware/releases) (Firmware 3.14.0 and newer)

Check out the [Homepage](https://github.com/sarusani/OctoPrint-ActivatePrusaHostTimer) to find out more about the use cases and upcoming features this plugin will allow you to use.
<br />
<br />
___
## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/sarusani/OctoPrint-ActivatePrusaHostTimer/archive/master.zip
