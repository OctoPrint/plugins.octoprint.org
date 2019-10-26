---
layout: plugin

id: CrealityTemperature
title: Creality Temperature Fix
description: Fix to parse correctly temperatures from Creality printer
author: Jean-Christophe Heger, Romain Odeval
license: AGPLv3

date: 201-10-26

homepage: your plugin's homepage
source: your plugin's source repository
archive: archive link to install your plugin via pip, e.g. from github: https://github.com/username/repository/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- creality
- temperature

screenshots:
- url: url of a screenshot, /assets/img/...
  alt: alt-text of a screenshot
  caption: caption of a screenshot
- url: url of another screenshot, /assets/img/...
  alt: alt-text of another screenshot
  caption: caption of another screenshot
- ...

featuredimage: url of a featured image for your plugin, /assets/img/...

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
Originally created by Jean-Christophe Heger on https://community.octoprint.org/t/temperature-info-not-parsed-correctly/3557/11

Tested on :
* CR-10S Pro
* CR-X
