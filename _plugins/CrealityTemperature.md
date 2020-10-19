---
layout: plugin

id: CrealityTemperature
title: Creality Temperature Fix
description: Fix to parse correctly temperatures from Creality printer
author: Romain Odeval, Jean-Christophe Heger
license: AGPLv3

date: 2019-10-28

homepage: https://github.com/RomainOdeval/OctoPrint-CrealityTemperature/
source: https://github.com/RomainOdeval/OctoPrint-CrealityTemperature/
archive: https://github.com/RomainOdeval/OctoPrint-CrealityTemperature/releases/latest/download/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- creality
- temperature

featuredimage: 

compatibility:
  octoprint:
  - 1.3.0
  os:
  - linux
  - windows
  - macos
  - freebsd

---

Fix to parse correctly temperatures from Creality printers.
Originally created by Jean-Christophe Heger on https://community.octoprint.org/t/temperature-info-not-parsed-correctly/3557/12

Tested on :
* CR-10S Pro
* CR-X
