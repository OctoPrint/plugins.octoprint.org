---
layout: plugin

id: active_filters
title: Active Filters
description: Save terminal filters status
author: ovidiu
license: AGPLv3
date: 2016-01-01

homepage: https://github.com/MoonshineSG/OctoPrint-ActiveFilters
source: https://github.com/MoonshineSG/OctoPrint-ActiveFilters
archive: https://github.com/MoonshineSG/OctoPrint-ActiveFilters/archive/master.zip
follow_dependency_links: false

tags:
- filters
- regex
- terminal

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.6

---
This plugin will save the status, active/inactive, of the regex filters in the terminal tab. 
The save is done local, so if you access OctoPrint on multiple computers, the settings, might vary.  

