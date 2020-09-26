---
layout: plugin

id: octoprint_hd44780
title: Octoprint-LCD-HD44780
description: Output status information on a 20x4 LCD screen
author: Kunsi
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2020-09-26

source: https://git.kunsmann.eu/kunsi/Octoprint-LCD-HD44780
archive: https://git.kunsmann.eu/kunsi/Octoprint-LCD-HD44780/archive/main.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- status
- gpio
- lcd

compatibility:
  # Only tested on python3, so requires 1.4.0
  octoprint:
  - 1.4.0

  os:
  - linux

  python: ">=3,<4"
---
This Plugin allows you to connect a HD44780-compatible LCD screen to your Raspberry Pi running OctoPrint.

Currently, the screen size is fixed to 20x4 characters. The used GPIO pins are fixed, too.
