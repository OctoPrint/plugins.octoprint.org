---
layout: plugin

id: z_probe_offset
title: Z Probe Offset Control
description: "Add input to the control view for editing the z probe offset on marlin based printers"
author: razer
license: AGPLv3

date: 2020-06-14

homepage: https://framagit.org/razer/octoprint_z_probe_offset
source: https://framagit.org/razer/octoprint_z_probe_offset
archive: https://framagit.org/razer/octoprint_z_probe_offset/-/archive/latest/octoprint_z_probe_offset-latest.zip

featuredimage: /assets/img/plugins/z_probe_offset/z_probe_offset_control.png

tags:
- probe
- marlin

compatibility:
  octoprint:
  - 1.3.9
  os:
  - linux
  - freebsd
  python: ">=2.7,<4"
---

# Z Probe Offset Control

Add input to the control view for editing the z probe offset on marlin based printers.

Needs Marlin firmware with z probe capability enabled.

Currently, firmwares that have been tested are:
 - Stock Marlin v1.x and v2.x
 - Creality3D Marlin fork (Ver 1.70.0 BL)
 - Prusa Marlin fork (Prusa-Firmware 3.9.0)

Note:

If your firmware is a marlin derivate and is not listed as tested, [please report it as a working one](https://framagit.org/razer/octoprint_z_probe_offset/-/issues) in order to add it to the list, or [report any issues](https://framagit.org/razer/octoprint_z_probe_offset/-/issues)

![screenshot](/assets/img/plugins/z_probe_offset/z_probe_offset_control.png)
