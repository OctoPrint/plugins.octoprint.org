---
layout: plugin

id: stats
title: Printer Statistics
description: Statistics of your 3D Printer
authors:
- Alex Verrico
- Anderson Silva
license: AGPLv3

date: 2015-09-13

homepage: https://github.com/AlexVerrico/octoprint-stats
source: https://github.com/AlexVerrico/octoprint-stats
archive: https://github.com/AlexVerrico/octoprint-stats/archive/master.zip

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

compatibility:
  python: ">=3.5,<4"

---

This plugin is designed to show statistics of your printer and estimate power usage in kWh.  

#### Important! You may need to install the system package libatlas-base-dev for this plugin to work by running `sudo apt install libatlas-base-dev`.

### Installing on Python 3:
Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:
```
https://github.com/AlexVerrico/octoprint-stats/archive/master.zip
```
### Installing on Python 2:
Install manually using this URL:
```
https://github.com/AlexVerrico/octoprint-stats/archive/py2.zip
```
Please note that the Python 2 version will no longer receive updates, it is strongly recommended that you switch your octoprint install to Python 3

