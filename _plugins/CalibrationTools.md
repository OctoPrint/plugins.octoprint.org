---
layout: plugin

id: CalibrationTools
title: Calibration Tools
description: Marlin Calibration Tools
authors: 
  - Sergiu Toporjinschi
license: GNUv3

date: 2022-02-09

homepage: https://github.com/SergiuToporjinschi/OctoPrint-CalibrationTools
source: https://github.com/SergiuToporjinschi/OctoPrint-CalibrationTools
archive: https://github.com/SergiuToporjinschi/OctoPrint-CalibrationTools/archive/main.zip

tags:
  - marlin
  - calibration
  - cube
  - pid
  - axes
  - printer
  - tools
  - extrusion
  
featuredimage: /assets/img/plugins/CalibrationTools/featuredimage.png

compatibility:
  octoprint: 
   - 1.2.0
  os:
    - linux
    - windows
    - macos
    - freebsd
  python: ">=2.7,<4"

---

A set of tools to help users with calibration process.
Supported tunings:

- E Steps - calibrating number of steps/mm for E extruder;
- XYZ Steps - calibrating number of steps/mm for axes X, Y and Z;
- PID Auto-tune - calibration Proportional gain, Integral gain and Derivative values for hot-end and heated bed;

Before start using this plugin I strongly recommend reading some documentation about tunning [teachingtechyt.github.io](https://teachingtechyt.github.io/calibration.html){:target="_blank"}

## Supported frameworks

- Marlin 2.x

## Screens

![E-Steps](/assets/img/plugins/CalibrationTools/eSteps.png)

![X-Y-Z Steps](/assets/img/plugins/CalibrationTools/featuredimage.png)

![PID Autotune](/assets/img/plugins/CalibrationTools/PID-autotune.png)

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/SergiuToporjinschi/OctoPrint-CalibrationTools/archive/main.zip

## Configuration

You can set the default values for each tuning process.
