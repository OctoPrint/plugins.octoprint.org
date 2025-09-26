---
layout: plugin

id: portretry
title: OctoPrint-PortRetry
description: PortRetry retries the serial connection on a configurable interval when the printer disconnects
author: VEhystrix
license: AGPLv3

# today's date in format YYYY-MM-DD
date: 2024-09-15

homepage: https://github.com/vehystrix/OctoPrint-PortRetry
source: https://github.com/vehystrix/OctoPrint-PortRetry
archive: https://github.com/vehystrix/OctoPrint-PortRetry/archive/main.zip

# Set this if your plugin heavily interacts with any kind of cloud services.
#privacypolicy: your plugin's privacy policy URL

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- disconnect
- recovery

#screenshots:
#- url: url of a screenshot, /assets/img/...
#  alt: alt-text of a screenshot
#  caption: caption of a screenshot
#- url: url of another screenshot, /assets/img/...
#  alt: alt-text of another screenshot
#  caption: caption of another screenshot
#- ...

#featuredimage: url of a featured image for your plugin, /assets/img/...

# You only need the following if your plugin requires specific OctoPrint versions or
# specific operating systems to function - you can safely remove the whole
# "compatibility" block if this is not the case.

compatibility:

  # List of compatible versions
  #
  # A single version number will be interpretated as a minimum version requirement,
  # e.g. "1.3.1" will show the plugin as compatible to OctoPrint versions 1.3.1 and up.
  # More sophisticated version requirements can be modelled too by using PEP440
  # compatible version specifiers.
  #
  # You can also remove the whole "octoprint" block. Removing it will default to all
  # OctoPrint versions being supported.

  octoprint:
  - 1.10.0

  # List of compatible operating systems
  #
  # Possible values:
  #
  # - windows
  # - linux
  # - macos
  # - freebsd
  #
  # There are also two OS groups defined that get expanded on usage:
  #
  # - posix: linux, macos and freebsd
  # - nix: linux and freebsd
  #
  # You can also remove the whole "os" block. Removing it will default to all
  # operating systems being supported.

  os:
  - linux
  #- windows
  #- macos
  #- freebsd

  # Compatible Python version
  #
  # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
  #
  # Plugins that only wish to support Python 3 should set it to ">=3,<4".
  #
  # If your plugin only supports Python 2 it will no longer be accepted on the plugin repository.
  #
  # Uncomment the appropriate setting

  #python: ">=2.7,<3" # Python 2 & 3
  python: ">=3,<4" # Python 3 only

# TODO
# If any of the below attributes apply to your project, uncomment the corresponding lines. This is MANDATORY!
    
#attributes:
#  - cloud  # if your plugin requires access to a cloud to function
#  - commercial  # if your plugin has a commercial aspect to it
#  - free-tier  # if your plugin has a free tier
---

When the printer is disconnected, this plugin will try to reconnect the printer on a configurable interval

Comes in handy when running octoprint in an lxc, and the port device is available even if the printer is not connected.

Should also work to solve the issue with Prusa printers that don't remove the serial port from the system when powering down

Caveats: only tested on OctoPrint 1.10.2, python 3 and on linux

## Configuration

In ~/.octoprint/config.yaml, the interval can be configured to something other than the default 5 seconds.
There is also a settings page in the webui
```
plugins:
  portretry:
    interval: 5
```

**This plugin will do nothing if the serial port in Serial Connection > General is set to `AUTO`, you will need to specify a port there for this plugin to work!** Or in ~/.octoprint/config.yaml:
```
serial:
  port: /dev/ttyUSB0
```
When you change the port from `AUTO` to something else, you will need to connect to the printer manually first (or restart the server).