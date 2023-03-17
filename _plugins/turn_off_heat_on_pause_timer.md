---
layout: plugin

id: turn_off_heat_on_pause_timer
title: OctoPrint-TurnOffHeatOnPauseTimer
description: Enables setting a timer for how long after the printer is paused that it should turn off hotend, heatbed and/or chamber.
authors:
- Per Åstrand
license: AGPLv3

date: 2023-03-16

homepage: https://github.com/Argon2000/OctoPrint-TurnOffHeatOnPauseTimer
source: https://github.com/Argon2000/OctoPrint-TurnOffHeatOnPauseTimer
archive: https://github.com/Argon2000/OctoPrint-TurnOffHeatOnPauseTimer/archive/master.zip

tags:
- temperature
- hotend
- hotbed
- chamber
- pause
- shutdown
- timer

screenshots:
- url: /assets/img/plugins/turn_off_heat_on_pause_timer/settings.png
  alt: Settings
  caption: Available settings

featuredimage: /assets/img/plugins/turn_off_heat_on_pause_timer/settings.png

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
  - 1.4.0

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

  os:
  - linux
  - windows
  - macos
  - freebsd

  # Compatible Python version
  #
  # It is recommended to only support Python 3 for new plugins, in which case this should be ">=3,<4"
  #
  # Plugins that wish to support both Python 2 and 3 should set it to ">=2.7,<4".
  #
  # Plugins that only support Python 2 will not be accepted into the plugin repository.

  python: ">=3,<4"

---

# OctoPrint-TurnOffHeatOnPauseTimer

A plugin for OctoPrint that shuts off hotend, hotbed and/or chamber after a set amount of seconds following a pause.
Useful when just pausing to switch filament, and don't want the printer to cool down. Or when an AI (like Gadget) automatically pauses and you want to either resume shortly thereafter (no waiting for things to heat up), or shut down since you can't attend to the 3d-printer at the moment.

It can also be used to restore temperatures when later resuming, but I recommend using a GCODE script (see example on GitHub) instead for that, since the plugin needs to pause the print again, heat up and then resume. Can possibly also cause issues with other plugins listening for a pause event.

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/Argon2000/OctoPrint-TurnOffHeatOnPauseTimer/archive/master.zip

# Configuration
## Timer (in seconds)
Set to desired time after the printer has paused that hotends/heatbed/chamber should turn off

Default: 600 (10 minutes)
## Turn off hotend
Wether or not hotend(s) should turn off

Default: ON (Will shut off hotend(s))
## Turn off heatbed
Wether or not heatbed should turn off

Default: ON (Will shut off heatbed)
## Turn off chamber
Wether or not chamber should turn off (If set to true and no chamber is present, this results in a error pop-up)

Default: OFF (Will NOT shut off chamber)

## Restore temperatures on resume (Better to use GCODE script)
If this plugin should handle restoring temperatures when a print resumes.

Default: OFF (Will NOT handle restoring temperatures)
