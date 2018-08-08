---
layout: plugin

id: shutdownprinter
title: ShutdownPrinter
description: Plugin for shutdown printer after finishing a print job
author: devildant
license: AGPLv3

date: 2018-06-18

homepage: https://github.com/devildant/OctoPrint-ShutdownPrinter
source: https://github.com/devildant/OctoPrint-ShutdownPrinter
archive: https://github.com/devildant/OctoPrint-ShutdownPrinter/archive/master.zip

follow_dependency_links: false

tags:
- shutdown
- shutdown printer
- tplink

screenshots:
- url: /assets/img/plugins/shutdownprinter/sidebar.JPG
  alt: shutdown printer sidebar plugin
  caption: shutdown printer sidebar plugin
- url: /assets/img/plugins/shutdownprinter/settings.JPG
  alt: shutdown printer settings plugin
  caption: shutdown printer settings plugin

featuredimage: /assets/img/plugins/shutdownprinter/sidebar.JPG

compatibility:
  # list of compatible versions, for example 1.3.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.3.8

---

This OctoPrint plugin enables the system to be automatically shut down printer after a print is finished (works with tplink plugs and OctoPrint-TPLinkSmartplug plugins).
The user can enable shutdown print for each print by using a checkbox in the sidebar.
This plugin was inspired by the work of "Nicanor Romero Venier" on the plugin: AutomaticShutdown (https://plugins.octoprint.org/plugins/automaticshutdown/)
Once the print is finished, a popup will appear with a countdown which lets the user abort the shutdown.
