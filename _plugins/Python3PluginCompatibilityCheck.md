---
layout: plugin

id: Python3PluginCompatibilityCheck
title: Python 3 Check
description: Checks installed plugins for Python 3 compatibility based on their entry in Plugin Repository.
author: jneilliii
license: AGPLv3

date: 2020-03-28

homepage: https://github.com/jneilliii/OctoPrint-Python3PluginCompatibilityCheck
source: https://github.com/jneilliii/OctoPrint-Python3PluginCompatibilityCheck
archive: https://github.com/jneilliii/OctoPrint-Python3PluginCompatibilityCheck/archive/master.zip

compatibility:
  octoprint:
  - 1.2.0
  os:
  - linux
  - windows
  - macos
  - freebsd  
  python: ">=2.7,<3"

---

# Python 3 Check

This plugin simply adds a section in settings that allows you to check your installed plugins against the OctoPrint Plugin Repository list to see which ones are not yet Python 3 compatible.

## Checking Compatibility

After installing, open OctoPrint's settings and click `Python 3 Check` in the plugins section. Press the `Check Compatibility` button and a list of links to the plugin's homepages will be generated. Click the link and open a new issue in the plugin's repository requesting for Python 3 compatibility.
