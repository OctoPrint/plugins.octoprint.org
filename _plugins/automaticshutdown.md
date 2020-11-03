---
layout: plugin

id: automaticshutdown
title: AutomaticShutdown
description: Plugin to enable automatic system shutdown after finishing a print job
author: Nicanor Romero Venier
license: AGPLv3

date: 2015-09-22

homepage: https://github.com/OctoPrint/OctoPrint-AutomaticShutdown
source: https://github.com/OctoPrint/OctoPrint-AutomaticShutdown
archive: https://github.com/OctoPrint/OctoPrint-AutomaticShutdown/archive/master.zip

follow_dependency_links: false

tags:
- automatic
- shutdown

screenshots:
- url: /assets/img/plugins/automaticshutdown/sidebar.png
  alt: Automatic Shutdown Plugin
  caption: Automatic Shutdown Plugin

featuredimage: /assets/img/plugins/automaticshutdown/sidebar.png

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.5

abandoned: https://github.com/OctoPrint/plugins.octoprint.org/issues/646

---

This OctoPrint plugin enables the system to be automatically shut down after a print is finished.
The user can enable automatic shutdown for each print by using a checkbox in the sidebar.
Once the print is finished, a popup will appear with a countdown which lets the user abort the shutdown.
