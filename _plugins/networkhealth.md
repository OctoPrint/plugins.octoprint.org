---
layout: plugin
id: networkhealth
title: Network Health
description: Monitors the health of the Network connection and restarts it if necessary
archive: https://github.com/jonfairbanks/OctoPrint-NetworkHealth/archive/master.zip
homepage: https://github.com/jonfairbanks/OctoPrint-NetworkHealth
source: https://github.com/jonfairbanks/OctoPrint-NetworkHealth
authors:
- Jon Fairbanks
license: AGPLv3
featuredimage: https://raw.githubusercontent.com/jonfairbanks/OctoPrint-NetworkHealth/master/logo.png
date: 2021-04-20

tags:
- network
- wifi
- ethernet

compatibility:

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=2.7,<4"
---

# Plugin for OctoPrint - monitors network health

Monitors the health of the Network connection by pinging the default gateway at a periodic interval. If the check fails, the plugin will restart the network adapter(s) as necessary.

This plugin does not modify the UI in any way. You can confirm the plugin is running from octoprint.log


## Setup

Install the plugin using Plugin Manager from Settings

No further configuration is required


## Change notes:
v 1.0.0
- Initial commit
