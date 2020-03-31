---
layout: plugin

id: dashboard
title: OctoPrint-Dashboard
description: A dashboard tab for Octoprint
author: Stefan Cohen
license: AGPLv3

date: 2019-09-10

homepage: https://github.com/StefanCohen/OctoPrint-Dashboard
source: https://github.com/StefanCohen/OctoPrint-Dashboard
archive: https://github.com/StefanCohen/OctoPrint-Dashboard/archive/master.zip

tags:
- dashboard
- status
- overview
- progress

screenshots:
- url: https://github.com/StefanCohen/OctoPrint-Dashboard/raw/master/screenshot.png
  alt: screenshot
  caption: caption of a screenshot
- url: https://github.com/StefanCohen/OctoPrint-Dashboard/raw/master/screenshot-theme.png
  alt: screenshot
  caption: themed screenshot
- url: https://github.com/StefanCohen/OctoPrint-Dashboard/raw/master/screenshot-theme2.png
  alt: screenshot
  caption: themed screenshot

featuredimage: https://github.com/StefanCohen/OctoPrint-Dashboard/raw/master/screenshot.png

compatibility:
  python: ">=2.7,<4"

---
This plugin adds a  dashboard tab in Octoprint that displays the most relevant info regarding the state of the printer and any on-going print job.

![Screenshot](https://github.com/StefanCohen/OctoPrint-Dashboard/raw/master/screenshot.png)

## Features

* Shows stats for:
    * Printer profile, Connection status, Printer Status
    * Hotend temp(s), Bed Temp, Chamber Temp, Fan speed
    * Printed file, Progress
    * Estimated total time, Elapsed time, Estimated time left
    * Current layer, Total layers
    * Current height, Total height
    * Average layer time
* Supports multiple hotends as configured in the printer profile
* Supports chamber temperature if configured in the printer profile
* Configurable progress gauge type (Circle, Bar)
* Uses Estimates from [PrintTimeGenius](https://plugins.octoprint.org/plugins/PrintTimeGenius/) when installed
* Uses GCode analysis provided by [DisplayLayerProgress](https://plugins.octoprint.org/plugins/DisplayLayerProgress/) to get more accurate layer and fan data
* Theme friendly:

![Screenshot](https://github.com/StefanCohen/OctoPrint-Dashboard/raw/master/screenshot-theme.png)


For installation and configuration details, please visit the [dashboard github page](https://github.com/StefanCohen/OctoPrint-Dashboard) 
