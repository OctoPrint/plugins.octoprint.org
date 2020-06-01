---
layout: plugin

id: lametric
title: Lametric
description: Display progress of your Octoprint instance on your LaMetric.
author: Thijs Bekke
license: AGPLv3

date: 2020-06-01

homepage: https://github.com/thijsbekke/Octoprint-LaMetric/
source: https://github.com/thijsbekke/Octoprint-LaMetric/
archive: https://github.com/thijsbekke/Octoprint-LaMetric/archive/master.zip

follow_dependency_links: false

tags:
- notification
- notifications
- lametric

compatibility:
  python: ">=2.7,<4"

screenshots:
- url: /assets/img/plugins/lametric/settings.png
  alt: Settings
  caption: You must configure two settings so that OctoPrint can communicate to your LaMetric. An API key and Host/Ip of you LaMetric
- url: /assets/img/plugins/lametric/screenshot_2.png
  alt: LaMetric
  caption: An example of the notification on your LaMetric

featuredimage: /assets/img/plugins/lametric/screenshot_1.png

---

This plugin adds support for your [LaMetric](https://lametric.com/) to OctoPrint.

When you start printing OctoPrint will send the current temperature or progress to your LaMetric.

The following notifications will be send to your LaMetric:

* Temperature of Tool and Bed
* Percentage complete 
* Job is Failed
* Job is completed
