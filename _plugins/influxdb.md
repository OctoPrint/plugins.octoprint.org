---
layout: plugin

id: influxdb
title: OctoPrint-InfluxDB
description: Writes temperatures and events to an Influx database.
author: Aaron Griffith
license: AGPLv3

date: 2019-11-02

homepage: https://github.com/agrif/OctoPrint-InfluxDB
source: https://github.com/agrif/OctoPrint-InfluxDB
archive: https://github.com/agrif/OctoPrint-InfluxDB/archive/master.zip

#follow_dependency_links: false

tags:
- data
- events

screenshots:
- url: /assets/img/plugins/influxdb/settings.png
  alt: Plugin Settings
  caption: Plugin Settings

featuredimage: /assets/img/plugins/influxdb/settings.png

compatibility:
  # blocking on
  # https://github.com/foosel/OctoPrint/pull/2978
  octoprint:
  - 1.3.11

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=2.7,<4"

---

An [InfluxDB](https://www.influxdata.com/) data gathering plugin for
OctoPrint. Track your printer's progress and temperature in InfluxDB!

See the plugin settings page to set InfluxDB server, target database,
field prefix, and poll interval.
