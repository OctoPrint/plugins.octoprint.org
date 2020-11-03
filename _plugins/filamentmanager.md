---
layout: plugin

id: filamentmanager
title: FilamentManager
description: Filament Manager for OctoPrint
author: Sven Lohrmann, Olli
license: AGPLv3
date: 2017-08-22
homepage: https://github.com/OllisGit/OctoPrint-FilamentManager
source: https://github.com/OllisGit/OctoPrint-FilamentManager
archive: https://github.com/OllisGit/OctoPrint-FilamentManager/releases/latest/download/master.zip
compatibility:
  python: ">=2.7,<4"
  octoprint:
  - 1.3.6
  - 1.4.0

tags:
- ui
- filament
- manager
screenshots:
- url: /assets/img/plugins/filamentmanager/filamentmanager_sidebar.png
  alt: Sidebar
  caption: Sample view of filament weight in the sidebar
- url: /assets/img/plugins/filamentmanager/filamentmanager_settings_profile.png
  alt: Profiles
  caption: View of filament profile editor
- url: /assets/img/plugins/filamentmanager/filamentmanager_settings_spool.png
  alt: Spool
  caption: View of filament spool editor
- url: /assets/img/plugins/filamentmanager/filamentmanager_settings.png
  alt: Settings
  caption: Settings dialog to manage the filament


---

This OctoPrint plugin helps to manage your filament spools.

#### Features

* Replacing filament volume with weight in sidebar
* Software odometer to measure used filament
* Warn if print exceeds remaining filament on spool
* Assign temperature offset to spools
* Automatically pause print if filament runs out
* Import & export of spool inventory
* Support for PostgreSQL as database for multiple instances
