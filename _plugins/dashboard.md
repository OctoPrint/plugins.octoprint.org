---
layout: plugin

id: dashboard
title: OctoPrint-Dashboard
description: A dashboard tab for Octoprint
author: Stefan Cohen, j7126, Willmac16
license: AGPLv3

date: 2019-09-10

homepage: https://github.com/j7126/OctoPrint-Dashboard
source: https://github.com/j7126/OctoPrint-Dashboard
archive: https://github.com/j7126/OctoPrint-Dashboard/archive/master.zip

tags:
- dashboard
- status
- overview
- progress

screenshots:
- url: /assets/img/plugins/dashboard/screenshot-2.png
  alt: screenshot
  caption: Dashboard screenshot
- url: /assets/img/plugins/dashboard/screenshot-2-theme.png
  alt: screenshot
  caption: Themed dashboard screenshot
- url: /assets/img/plugins/dashboard/screenshot-2-fullscreen.png
  alt: screenshot
  caption: Dashboard fullscreen screenshot
- url: /assets/img/plugins/dashboard/screenshot.png
  alt: screenshot
  caption: Dashboard screenshot
- url: /assets/img/plugins/dashboard/screenshot-theme.png
  alt: screenshot
  caption: Themed dashboard screenshot
- url: /assets/img/plugins/dashboard/screenshot-theme2.png
  alt: screenshot
  caption: Themed dashboard screenshot

featuredimage: /assets/img/plugins/dashboard/screenshot-2.png

compatibility:
  python: ">=2.7,<4"

---
This plugin adds a  dashboard tab in Octoprint that displays the most relevant info regarding the state of the printer and any on-going print job.

![Screenshot](/assets/img/plugins/dashboard/screenshot-2.png)

## Features

* Adds a new tab first in the list and becomes the default tab when opening OctoPrint
* Widgets for current:
    * RPi host CPU Load, CPU Temp, CPU frequency, Mem Utilization, Storage Utilization.   
    * Printer profile, Connection status, Printer Status
    * Hotend temp(s), Bed Temp, Chamber Temp, Fan speed
    * Temperature/Humidity sensors.
    * Shell command output
    * Printed file, Job Progress, Layer Progress
    * Layer Duration Graph
    * Estimated total time, ETA, Time left, Time since print started
    * Current layer, Total layers
    * Current height, Total height
    * Average layer time
    * WebCam view
* Settings to configure what widgets and info to include in the Dashboard
* Supports multiple hotends as configured in the printer profile
* Supports chamber temperature if configured in the printer profile
* Configurable progress gauge type (Circle, Bar)
* Fullscreen mode including job control buttons (Start, Cancel, Pause/Resume)
* Full page mode by adding `?dashboard=full` parameter at the end of the octoprint url
* Uses Estimates from [PrintTimeGenius](https://plugins.octoprint.org/plugins/PrintTimeGenius/) when installed
* Uses GCode analysis provided by [DisplayLayerProgress](https://plugins.octoprint.org/plugins/DisplayLayerProgress/) to get more accurate layer and fan data
* Theme friendly


Themed screenshot: 

![Screenshot](/assets/img/plugins/dashboard/screenshot-2-theme.png)

Fullscreen mode screenshot: 

![Screenshot](/assets/img/plugins/dashboard/screenshot-2-fullscreen.png)


For installation and configuration details, please visit the [dashboard github page](https://github.com/j7126/OctoPrint-Dashboard)
