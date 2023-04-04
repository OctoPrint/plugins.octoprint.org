---
layout: plugin
id: psucontrol_fhem
title: PSU Control - FHEM
description: Adds FHEM support to OctoPrint-PSUControl as a sub-plugin
authors:
- Nils Andresen
license: AGPLv3
date: 2023-04-04
homepage: https://github.com/nils-org/OctoPrint-PSUControl-FHEM
source: https://github.com/nils-org/OctoPrint-PSUControl-FHEM
archive: https://github.com/nils-org/OctoPrint-PSUControl-FHEM/archive/main.zip
tags:
- power
- psu
- control
- psucontrol
- psucontrol subplugin
- fhem
screenshots:
- url: /assets/img/plugins/psucontrol_fhem/fhem-view.png
  alt: View of a switch-like device in FHEM
  caption: View of a switch-like device in FHEM
- url: /assets/img/plugins/psucontrol_fhem/fhem-settings.png
  alt: Screenshot of plugin settings page
  caption: Screenshot of plugin settings page
featuredimage: /assets/img/plugins/psucontrol_fhem/fhem-settings.png
compatibility:
  python: ">=2.7,<4"
---

This plugin makes an FHEM device usable for PSU Control. Currently this is targeted at switch-like devices, i.e. sending
`set <device> on` and `set <device> off`. While there is a certain amount of configuration available, I have only tested it
using switches like the above.

**Please check the [github repo](https://github.com/nils-org/OctoPrint-PSUControl-FHEM/) for up to date information and more details**
