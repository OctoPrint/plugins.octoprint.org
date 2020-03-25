---
layout: plugin

id: HeaterTimeout
title: HeaterTimeout
description: Automatically shut off heaters if no print has been started.
author: Uriah Welcome
license: Apache 2

date: 2017-09-25

homepage: https://github.com/google/OctoPrint-HeaterTimeout
source: https://github.com/google/OctoPrint-HeaterTimeout
archive: https://github.com/google/OctoPrint-HeaterTimeout/archive/master.zip

follow_dependency_links: false

tags:
- temperature
screenshots:
- url: /assets/img/plugins/heatertimeout/configuration.png
  alt: Configuration Screen
  caption: Configure HeaterTimeout

compatibility:
  octoprint:
  - 1.3.1
  python: ">=2.7,<4"
---

Ever accidentally preheat your hotend or bed and then forget to start a print? Then this is the plugin for you.

This plugin will automatically disable your printers heaters after a specified timeout if no print has been started.
