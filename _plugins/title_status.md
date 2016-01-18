---
layout: plugin

id: title_status
title: Title Status
description: Show printers status in window title
author: ovidiu
license: AGPLv3
date: 2016-01-18

homepage: https://github.com/MoonshineSG/OctoPrint-TitleStatus
source: https://github.com/MoonshineSG/OctoPrint-TitleStatus
archive: https://github.com/MoonshineSG/OctoPrint-TitleStatus/archive/master.zip
follow_dependency_links: false

tags:
- title
- status

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.6
  
---
Shows the status of the printer (offline, operational, connecting, paused, error... ) in the title of the browser as
- Connecting...
- Paused...
- ERROR !! 
- * = Offline
- △ = Printing
- ? = Unknown
