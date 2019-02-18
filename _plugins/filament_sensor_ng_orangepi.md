---
layout: plugin

id: filament_sensor_ng_orangepi
title: FilamentSensor OrangePi
description: A filament monitor that pauses the print when your filament runs out and lets you restart it.
author: Deadly667
license: GPLv3
date: 2019-02-18

homepage: https://github.com/deadly667/Octoprint-Filament-Sensor-ng-OrangePi
source: https://github.com/deadly667/Octoprint-Filament-Sensor-ng-OrangePi
archive: https://github.com/deadly667/Octoprint-Filament-Sensor-ng-OrangePi/archive/master.zip
follow_dependency_links: false

tags:
- filament
- sensor
- orangePi

screenshots:
- url: /assets/img/plugins/filament_sensor_ng_orangepi/configuration.png
  alt: Sensor Configuration
  caption: Sensor Configuration

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.3.9

  os:
  - nix
---
## Overview

Pause printing when the 3D printer runs out of filament.

**Credits:**

Inspired by and based on the work by

OctoPrint-FilamentSensor-ng plugin by Red-M found [here](https://github.com/Red-M/Octoprint-Filament-Sensor-ng)

## Configuration

After installation, configure the plugin via OctoPrint Settings interface.

**The pin being used needs to be entered by name (e.g. PA01, PC07).**

![screenshot](/assets/img/plugins/filament_sensor_ng_orangepi/configuration.png)

## OrangePI OS Configuration

Since we are accessing the GPIO as a non root user we need to configure the OS to allow this. Here's the copy of the library documentation on how to do it:

 If you want to be able to use the library as a non root user, you will need to setup a `UDEV` rule to grant you permissions first. 
 This can be accomplished as follows: 
 ```
 $ sudo usermod -aG gpio <current_user>
 $ sudo nano /etc/udev/rules.d/99-gpio.rules
 ```
 That should add your user to the GPIO group, create a new ``UDEV`` rule, and open it in the Nano text editor. 
 Enter the following into Nano
 ```
   SUBSYSTEM=="gpio", KERNEL=="gpiochip*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys/class/gpio/export /sys/class/gpio/unexport ; chmod 220 /sys/class/gpio/export /sys/class/gpio/unexport'" 
   SUBSYSTEM=="gpio", KERNEL=="gpio*", ACTION=="add", PROGRAM="/bin/sh -c 'chown root:gpio /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value ; chmod 660 /sys%p/active_low /sys%p/direction /sys%p/edge /sys%p/value'"
 ```   
 press ``ctrl-x``, ``Y``, and ``ENTER`` to save and close the file. 
 Finally, reboot and you should be ready to use ``OPi.GPIO`` as a non root user. 


## Issues with OPI GPIO library

https://github.com/rm-hull/OPi.GPIO/pull/28 solves the issues with PI GPIO library and the race condition that was preventing normal operations. It is available in release v0.3.4 and up so make sure you have latest OPI GPIO library. To upgrade to latest OPI GPIO library login to your octoprint server as user ``pi`` and execute:

```
 $ cd OctoPrint/ 
 $ venv/bin/pip install --upgrade OPi.GPIO
```

