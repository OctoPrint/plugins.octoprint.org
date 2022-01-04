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
featuredimage: /assets/img/plugins/networkhealth/logo.png
date: 2021-04-20

tags:
- network
- wifi
- ethernet

compatibility:

  os:
  - linux

  python: ">=2.7,<4"
---

# Network Health

Monitors the health of the Network connection by pinging the default gateway at a periodic interval. If the check fails, the plugin will restart the network adapter(s) as necessary.

This plugin does not modify the UI in any way. You can confirm the plugin is running from octoprint.log


## Configuration

By default the `ip` command used to restart the network interfaces requires sudo permissions. 

To allow OctoPrint to manage this for us, we need to update sudoers using the below command:
```
echo 'pi ALL=NOPASSWD:/sbin/ip' | sudo tee /etc/sudoers.d/octoprint-ip
```

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/jonfairbanks/OctoPrint-NetworkHealth/archive/master.zip


## Change Notes:
v 1.0.4
- Error Handling

v 1.0.3
- Proper Versioning

v 1.0.2
- Bug Fixes

v 1.0.1
- Usability Improvements

v 1.0.0
- Initial Commit