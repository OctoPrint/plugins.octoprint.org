---
layout: plugin

id: prettygcode
title: OctoPrint-PrettyGCode
description: A pretty GCode visualizer for Octoprint
author: Kragrathea
license: AGPLv3

date: 2020-08-17

homepage: https://github.com/Kragrathea/OctoPrint-PrettyGCode
source: https://github.com/Kragrathea/OctoPrint-PrettyGCode
archive: https://github.com/Kragrathea/OctoPrint-PrettyGCode/archive/master.zip

tags:
- Gcode
- visualizer
- WebGL
- progress

screenshots:
- url: /assets/img/plugins/prettygcode/PrettyGcode-Screen1.jpg
  alt: screenshot
  caption: PrettyGCode
- url: /assets/img/plugins/prettygcode/PrettyGcode-Screen2.jpg
  alt: screenshot
  caption: Windows open screenshot
- url: /assets/img/plugins/prettygcode/PrettyGcode-Screen3.jpg
  alt: screenshot
  caption: Tabbed screenshot

featuredimage: /assets/img/plugins/prettygcode/PrettyGcode-Screen1.jpg

compatibility:
  python: ">=2.7,<4"
---
This plugin adds a 3D GCode visualizer tab in Octoprint. It displays colored lines to give you some idea what the printer is doing and animates progress during printing.

![Screenshot](/assets/img/plugins/prettygcode/PrettyGcode-Screen2.jpg)

## Features

* 3D Gcode visualizer
* Sync progress to print job
* Full screen and tabbed interface
* Uses Dashboard plugin from [Dashboard github page](https://github.com/StefanCohen/OctoPrint-Dashboard) when installed
* Customize the UI via CSS injection (see Instructions on tab in OctoPrint)


![Screenshot](/assets/img/plugins/prettygcode/PrettyGcode-Screen3.jpg)


For and configuration details, please see the instructions on the PrettyGcode tab in OctoPrint. Report bugs via the [PrettyGCode github page](https://github.com/Kragrathea/OctoPrint-PrettyGCode).
