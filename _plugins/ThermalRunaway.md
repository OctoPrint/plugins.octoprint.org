---
layout: plugin

id: ThermalRunaway
title: Thermal Runaway
description: An Octoprint Plugin to provide some basic Thermal Runaway protection
author: Alex Verrico
license: AGPLv3

# TODO
date: 2020-06-24

homepage: https://github.com/AlexVerrico/Octoprint-ThermalRunaway
source: https://github.com/AlexVerrico/Octoprint-ThermalRunaway
archive: https://github.com/AlexVerrico/Octoprint-ThermalRunaway/archive/master.zip

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

# TODO
tags:
- thermal runaway
- temperature
- temp

# TODO
screenshots:
- url: /assets/img/plugins/ThermalRunaway/ThermalRunaway-config.png
  alt: configuration
  caption: Configuration

# TODO
featuredimage: /assets/img/plugins/ThermalRunaway/ThermalRunaway-config.png

# TODO
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

  #octoprint:
  #- 1.4.0

  # List of compatible operating systems
  #
  # Valid values:
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

  #os:
  #- linux
  #- windows
  #- macos
  #- freebsd
  
  # Compatible Python version
  #
  # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
  #
  # Plugins that only wish to support Python 3 should set it to ">=3,<4". 
  #
  # If your plugin only supports Python 2 (worst case, not recommended for newly developed plugins since Python 2
  # is EOL), leave at ">=2.7,<3"
  
  python: ">=3,<4"

---


__What this plugin does:__ <br/>
Sends the configured GCode command when a heater on the printer is outside of configured maximum/minimum temperatures and not heading towards the set temperature<br/><br/>

__What this plugin _does not_ do:__<br/>
This plugin does not stop a thermal runaway, it just sends a GCode command, and it is up to you to find a way to handle that GCode command appropriately. As such, *I strongly recommend that you __watch your printer at all times__*
<br/><br/>
For more details, see [https://github.com/AlexVerrico/Octoprint-ThermalRunaway](https://github.com/AlexVerrico/Octoprint-ThermalRunaway)
### Disclaimer:  
I, the plugin author, strongly recommend that you __NEVER__ leave you printer unattended while powered. This plugin is not a replacement for [firmware thermal runaway detection](https://3dprinting.stackexchange.com/a/8467). I, the plugin author, __cannot__ be held responsible for any damage to equipment or injuries that may arise from leaving your 3D Printer unattended. I, the plugin author, make no guarantees that this plugin will work or continue to work.
