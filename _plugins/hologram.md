---
layout: plugin

id: hologram
title: OctoPrint-Hologram
description: A simple OctoPrint plugin to display a render based on the preloaded G-code.
authors:
- MarkSlat
license: AGPLv3

date: 2024-05-17

homepage: https://github.com/MarkSlat/OctoPrint-Hologram
source: https://github.com/MarkSlat/OctoPrint-Hologram
archive: https://github.com/MarkSlat/OctoPrint-Hologram/archive/main.zip

tags:
- ui
- Gcode
- visualizer

screenshots:
- url: /assets/img/plugins/hologram/demo.jpeg
  alt: Example preview of Benchy
  caption: Example preview of Benchy
- url: /assets/img/plugins/hologram/setup_1.gif
  alt: Example setup step 1
  caption: Example setup step 1
- url: /assets/img/plugins/hologram/setup_2.gif
  alt: Example setup step 2
  caption: Example setup step 2


featuredimage: /assets/img/plugins/hologram/demo.jpeg


compatibility:
  octoprint:
  - 1.4.0
  os:
  - linux
  - windows
  - macos
  python: ">=3.7,<4"

---
This plugin allows a user to an accurate preview of their print projected onto the build plate. Designed for cameras mounted on the build plates.

## Example Usage
Generate a render by loading the print file, clicking the render button and it overlays a render onto the build plate.

![demo](/assets/img/plugins/hologram/demo.jpeg)

## Setup
In the settings page, enter the physical X and Y dimensions of the build plate (not the print volume).

Position the box over the build plate and secure it to initiate the calibration process.

![setup_1](/assets/img/plugins/hologram/setup_1.gif)

Make any necessary adjustments. Ensure the arrow points towards the origin.

![setup_2](/assets/img/plugins/hologram/setup_2.gif)

Navigate to the hologram tab and select a file to render and preview

## Raspberry Pi
Since this plugin depends on Numpy you many have to run the following.
- sudo apt-get install libopenblas-base
- sudo ldconfig

See: https://numpy.org/devdocs/user/troubleshooting-importerror.html

## Future plans
To automatically detect failures and defects in real-time by cross comparing the rendered model with the actual print, layer by layer. If a certain confidence level is met, the print will be paused. Check the pre-releases for more information.

## Acknowledgments
I would like to give credit Yaqi Zhang’s for using their script for part of the Gcode rendering function.
https://github.com/zhangyaqi1989/Gcode-Reader
