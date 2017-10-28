---
layout: plugin

id: octoplug
title: OctoPlug
description: Plugin for OctoPrint that turns on an Edimax SP-1101W SmartPlug at a certain layer.
author: Tobias Viertmann
license: MIT

date: 2015-09-30

homepage: https://github.com/tobbi007/OctoPrint-OctoPlug
source: https://github.com/tobbi007/OctoPrint-OctoPlug
archive: https://github.com/tobbi007/OctoPrint-OctoPlug/archive/master.zip

follow_dependency_links: false

tags:
- fan
- power
- powerplug
- remote

screenshots:
- url: /assets/img/plugins/octoplug/powerplug.png
  alt: Edimax SP-1101W
  caption: Edimax SP-1101W
- url: /assets/img/plugins/octoplug/config.png
  alt: OctoPlug Config
  caption: OctoPlug Config
  
featuredimage: /assets/img/plugins/octoplug/powerplug.png

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.5

  # list of compatible operating systems, valid values are linux, windows, macos, leaving empty defaults to all
  os:
  - linux
  - windows
  - macos
---

OctoPlug is a plugin for OctoPrint, which switches on an Edimax SmartPlug at a certain layer while printing. It also stops it when the printer finished printing.
Use this to trigger your additional active cooling fan, which is not directly connected to the board of the printer.
This plugin has only been testet with the Edimax SP1101W SmartPlug (http://www.edimax.com/edimax/merchandise/merchandise_detail/data/edimax/au/home_automation_smart_plug/sp-1101w/)
