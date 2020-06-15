---
layout: plugin

id: z_probe_offset
title: Z Probe Offset Control
description: Control the z probe offset on marlin based printers. Warning: this plugin is on its early stage of developpement. Use with caution and please report any issues on the git repository. Improvement suggestions are welcome as well.
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

Add input to the control tab for z probe offset value change.
Needs Marlin firmware (1.x or 2.x) with z probe capability enabled.
Warning: this plugin is on its early stage of developpement. Use with caution and please report any issues on the git repository. Improvement suggestions are welcome as well.

![screenshot](/assets/img/plugins/z_probe_offset/z_probe_offset_control.png)
