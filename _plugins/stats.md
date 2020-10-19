---
layout: plugin

id: stats
title: Printer Statistics
description: Statistics of your 3D Printer
author: Anderson Silva
license: AGPLv3

date: 2015-09-13

homepage: https://github.com/amsbr/OctoPrint-Stats
source: https://github.com/amsbr/OctoPrint-Stats
archive: https://github.com/amsbr/OctoPrint-Stats/archive/master.zip

follow_dependency_links: false

# TODO
tags:
- stats
- power
- usage

screenshots:
- url: /assets/img/plugins/stats/img1.png
  alt: Tab
- url: /assets/img/plugins/stats/img2.png
  alt: Tab
- url: /assets/img/plugins/stats/img3.png
  alt: Tab
- url: /assets/img/plugins/stats/img4.png
  alt: Settings

featuredimage: /assets/img/plugins/stats/img1.png

disabled: The plugin has a dependency that only supports Python 3 now, however it isn't yet marked as Python 3 compatible
    itself, rendering it uninstallable without code modifications. See [this ticket](https://github.com/OctoPrint/plugins.octoprint.org/issues/434).

abandoned: https://github.com/OctoPrint/plugins.octoprint.org/issues/479

---

This plugin is designed to show statistics of your printer and estimate power usage in kWh.

