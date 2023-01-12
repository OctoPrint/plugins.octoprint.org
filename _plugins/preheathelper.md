---
layout: plugin

id: preheathelper
title: OctoPrint-PreheatHelper
description: A little helper to automate your printer pre-heating!
authors:
- RoboMagus
license: AGPLv3

# TODO
date: 2022-05-07

homepage: https://github.com/RoboMagus/OctoPrint-PreheatHelper
source: https://github.com/RoboMagus/OctoPrint-PreheatHelper
archive: https://github.com/RoboMagus/OctoPrint-PreheatHelper/archive/master.zip

tags:
- preheat
- helper
- parser

compatibility:

  octoprint:
  - 1.4.0

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=3,<4"

---

A little helper to automate your printer pre-heating!

You can have it automatically pre-heat your printer as soon as it connects to Octoprint.
Or when you (pre-)load a file this plugin can scan for the temperature setpoints in the GCode and use those to pre-heat the printer before you hit play.
