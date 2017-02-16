---
layout: plugin
    
id: lani
title: Lani
description: Lani integration for OctoPrint
author: Michael Rybka
license: None
    
# today's date in format YYYY-MM-DD, e.g.
date: 2017-02-15
    
homepage: https://lanilabs.com
source: https://github.com/mikerybka/OctoPrint-Lani
archive: https://github.com/mikerybka/OctoPrint-Lani/archive/master.zip
    
# set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false
    
tags:
- ui
- administration
- notification

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
    
This plugin allows people using Lani to control their OctoPrint printers alongside their other devices.
Lani is an order management system specifically designed for 3D printing. You can manage users, payment and
print jobs on all of your printers.

Features:
- Control multiple instances of OctoPrint remotely
- Report on status to any device with internet
- Be controlled by a manager anywhere
- Create reports on usage, sales, ROI
- Allow other people to submit jobs
- Payment system (coming soon)

To find out more, go to [lanilabs.com](https://lanilabs.com)