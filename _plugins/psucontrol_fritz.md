---
layout: plugin
id: psucontrol_fritz
title: PSU Control - FRITZ!Box
description: Adds FRITZ!Dect Smart Plug support to OctoPrint-PSUControl as a sub-plugin
archive: https://github.com/not-na/OctoPrint-PSUControl-Fritz/archive/master.zip
homepage: https://github.com/not-na/OctoPrint-PSUControl-Fritz
source: https://github.com/not-na/OctoPrint-PSUControl-Fritz
author: not-na
license: AGPLv3
date: 2022-04-28
tags:
- power
- psu
- control
- psucontrol
- psucontrol subplugin
- fritz
- fritz dect
compatibility:
  os:
  - posix
  - windows
  python: ">=3,<4"
---

![Screenshot of settings](/assets/img/plugins/psucontrol_fritz/psucontrol_fritz_settings.png "Settings")

This sub-plugin adds support for switching FRITZ!Dect Smart Plugs directly from the Octoprint Web Interface.

To use this plugin, you'll also have to install the PSU Control plugin. Without that plugin, this plugin will not function.

For security reasons, it is recommended to create a dedicated user account on your FRITZ!Box with *only* Smart Home privileges.

The AIN in the settings should be taken from the FRITZ!Box Smart Home settings, it should be five digits followed by seven digits.
Of course, the FRITZ!Dect smart home device should be paired with the FRITZ!Box before configuring this plugin. Please refer to
the instructions provided with the device for further details.
