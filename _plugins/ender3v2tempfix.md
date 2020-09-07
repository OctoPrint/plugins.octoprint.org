---
layout: plugin

id: ender3v2tempfix
title: Ender-3 v2 Temperature Fix
description: Fixes the temperature reporting from the Creality Ender-3 v2 printer
author: Albert MN. @ SimplyPrint, b-morgan
license: MIT

# today's date in format YYYY-MM-DD, e.g.
date: 2020-09-07

homepage: https://github.com/SimplyPrint/OctoPrint-Ender3V2TempFix
source: https://github.com/SimplyPrint/OctoPrint-Ender3V2TempFix
archive: https://github.com/SimplyPrint/OctoPrint-Ender3V2TempFix/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- creality
- ender-3 v2
- temperature

compatibility:
  os:
  - linux
  - windows
  - macos
  - freebsd
      
  python: ">=2.7,<3"
      
---

Fix to correctly parse temperatures received from the Creality Ender-3 v2 printer.
Originally created by b-morgan Heger at https://community.octoprint.org/t/temperature-reporting-now-working-with-new-ender-3-v2/21053

Tested on multiple Ender-3 v2 printers, firmware version 1.0.1