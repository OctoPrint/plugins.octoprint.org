---
layout: plugin

id: filamentencore
title: Filament Sensor Encore
description: OctoPrint plug-in that detects when printer is out of filament
author: Dragos Costache
license: AGPLv3

date: 2019-06-03

homepage: https://github.com/draagc/OctoPrint-FilamentEncore
source: https://github.com/draagc/OctoPrint-FilamentEncore
archive: https://github.com/draagc/OctoPrint-FilamentEncore/archive/master.zip

tags:
- filament
- sensor

compatibility:
  octoprint:
  - 1.2.6

  os:
  - nix

disabled: There has been a report of OctoPrint crashing on resume. Disabled until this issue has been clarified. See [foosel/OctoPrint#3213](https://github.com/foosel/OctoPrint/issues/3213) and [draagc/OctoPrint-FilamentEncore#3](https://github.com/draagc/OctoPrint-FilamentEncore/issues/3).

---

Pause printing when the 3D printer runs out of filament.

Based on the Filament Sensor Reloaded plugin by kontakt, this plugin adds new features such as the ability to prevent print starting/resuming when no filament detected and offers bug fixes.
