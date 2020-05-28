---
layout: plugin

id: PrintJobHistory
title: PrintJobHistory
description: The OctoPrint-Plugin stores all print-job informations of a print in a database.
author: Olli
license: AGPLv3

date: 2020-05-28

homepage: https://github.com/OllisGit/OctoPrint-PrintJobHistory
source: https://github.com/OllisGit/OctoPrint-PrintJobHistory
archive: https://github.com/OllisGit/OctoPrint-PrintJobHistory/releases/latest/download/master.zip

follow_dependency_links: false

tags:
- printer
- history

compatibility:
  python: ">=2.7,<4"
  octoprint:
  - 1.3.10
  - 1.4.0
  
screenshots:
- url: https://github.com/OllisGit/OctoPrint-PrintJobHistory/raw/master/screenshots/plugin-tab.png
  alt: History Overview Tab 
  caption: History Overview Tab

- url: https://github.com/OllisGit/OctoPrint-PrintJobHistory/raw/master/screenshots/editPrintJob-dialog.png
  alt: Edit of a Print Job Item
  caption: Edit of a Print Job Item


- url: https://github.com/OllisGit/OctoPrint-PrintJobHistory/raw/master/screenshots/plugin-settings.png
  alt: Plugin Settings
  caption: Plugin Settings

- url: https://github.com/OllisGit/OctoPrint-PrintJobHistory/raw/master/screenshots/missingPlugins-dialog.png
  alt: Optional Plugin Dependencies
  caption: Optional Plugin Dependencies


featuredimage: https://github.com/OllisGit/OctoPrint-PrintJobHistory/raw/master/screenshots/editPrintJob-dialog.png

---

Print Job History-Plugin collects a lot of attributes from OctoPrint itself, like Start/End-Time, Username any many more. But it also grabs informations from other plugins: Thumbnail, Layer-Information, Filament usage...

For a full overview of the latest feature set and planed features, please visit the [Git Hub Homepage]({{ page.homepage | absolute_url }})


#### Support my Efforts

This plugin, as well as my [other plugins](https://github.com/OllisGit/) were developed in my spare time.
If you like it, I would be thankful about a cup of coffee :) 

[![More coffee, more code](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=6SW5R6ZUKLB5E&source=url)



