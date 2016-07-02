---
layout: plugin

id: filament
title: Filament Sensor
description: Use a filament sensor to pause printing when filament runs out.
author: ovidiu
license: AGPLv3
date: 2016-06-29

homepage: https://github.com/MoonshineSG/OctoPrint-Filament
source: https://github.com/MoonshineSG/OctoPrint-Filament
archive: https://github.com/MoonshineSG/OctoPrint-Filament/archive/master.zip
follow_dependency_links: false

tags:
- filament
- sensor
- api

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.6

  os:
  - linux
---
Pause print on GPIO filament runout sensor

The following needs to be added to the config.yaml:

```
  octoprint_filament:
    pin: XX
    bounce: 400
```
where XX represent the GPIO pin where your sensor is connected.

An API is available to check the filament sensor status via a GET method to `/plugin/filament/status` which returns a JSON

- `{status: "-1"}` if the sensor is not setup
- `{status: "0"}` if the sensor is OFF (filament not present)
- `{status: "1"}` if the sensor is ON (filament present)

The status 0/1 depends on the type of sensor, and it might be reversed if using a normally closed switch.

A build using an optical switch can be found at [http://www.thingiverse.com/thing:1646220](http://www.thingiverse.com/thing:1646220)

Note: Needs RPi.GPIO version greater than 0.6.0 to allow access to GPIO for non root and `chmod a+rw /dev/gpiomem`.
This requires a failry up to date system.
