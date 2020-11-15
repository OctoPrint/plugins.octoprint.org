---
layout: plugin

id: smartfilamentsensor
title: Octoprint-Smart-Filament-Sensor
description: A plugin to directly add Smart Filament Sensors like BigTreeTech Smart Filament Sensor to Octoprint.
author: Anni Lange
license: GPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2020-10-16

homepage: https://github.com/maocypher/Octoprint-Smart-Filament-Sensor
source: https://github.com/maocypher/Octoprint-Smart-Filament-Sensor
archive: https://github.com/maocypher/Octoprint-Smart-Filament-Sensor/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- Sensor
- Filament

screenshots:
- url: /assets/img/plugins/smartfilamentsensor/settings.PNG
  alt: Screenshot of the plugin in settings
  caption: Smart Filament Sensor settings
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
  - 1.3.0

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
#  - windows
#  - macos
#  - freebsd

  # Compatible Python version
  #
  # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
  #
  # Plugins that only wish to support Python 3 should set it to ">=3,<4".
  #
  # If your plugin only supports Python 2 (worst case, not recommended for newly developed plugins since Python 2
  # is EOL), leave at ">=2.7,<3"

  python: ">=2.7,<4"

---

# Octoprint-Smart-Filament-Sensor

[OctoPrint](http://octoprint.org/) plugin that lets integrate Smart Filament Sensors like BigTreeTechs SmartFilamentSensor directly to RaspberryPi GPIO pins. This enables that this sensor can also be used on 3D Printers, that do not have a E0-Stop like e.g. Creality 1.1.4 Mainboard of Ender 3.

Initial work based on the [Octoprint-Filament-Reloaded](https://github.com/kontakt/Octoprint-Filament-Reloaded) plugin by kontakt.
Fork of [Octoprint-Filament-Revolutions](https://github.com/RomRider/Octoprint-Filament-Revolutions) plugin by RomRider.

The solution for this plugin is inspired by [Marlin Firmware](https://github.com/MarlinFirmware/Marlin)

## Required sensor

To use this plugin a Filament Sensor is needed that sends a toogling digital signal (0-1-0...) during movement.

This plugin can use the GPIO.BOARD or GPIO.BCM numbering scheme.

## Features

* Configurable GPIO pins.
* Support movement detection sensors, e.g. Smart-Filament-Sensor.
* Detect if filament is not moving anymore (jammed or runout)
    * Detection based on timeout
    * Detection based on filament position returned bei M114 (unfortunately imprecise compared with firmware)

## Installation

* Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager).
* Manually using this URL: https://github.com/maocypher/Octoprint-Smart-Filament-Sensor/archive/master.zip

After installation a restart of Octoprint is recommended.

## Configuration
### GPIO Pin
* Choose any free GPIO pin you for data usage, but I would recommend to use GPIO pins without special functionalities like e.g. I2C
* Run the sensor only on 3.3V, because GPIO pins don't like 5V for a long time

### Detection time
Currently it is necessary to configure a maximum time period no filament movement was detected. This time could be depended on the print speed and maximum print line length. For the beginning - until I figured out how to estimate the best detection time - you can run a test print and messearue your maximum time and configure this value.
The default value 45 seconds was estimated on max. print speed 10mm/s, for faster prints it could be smaller.

### Detection distance
Version 1.1.0 of this plugin detects the movement depending on the moved distance. Therefore it is necessary to configure a distance without movement being detected. In Marlin Firmware the default value is set to 7mm. According to this the value is set for the plugin.

### Sampling time
To reduce the negative effects on the print quality a sampling time must be set. Periodically M114 code is sent to the printer to receive the current filament position. This increases the load on the printer, i.e. if the sampling time is set to small the printer starts stuttering, because it cannot process all commands fast enough. I  assume the value could differ according to the mainboard architecture (8-bit or 32-bit).

### Octoprint - Firmware & Protocol
Since currently GCode command M600 is used to interrupt the print, it is recommended to add M600 to the setting "Pausing commands".

### Octoprint - GCode Scripts
If you do not want that the print is paused right on your print, I recommend to add a GCode Script for "After print job is paused". Also adding GCode script "Before print job is resumed" might be useful, in the case you hit the heatbed or print head during the change of the filament or removing the blockage.

## Disclaimer
* I as author of this plugin am not responsible for any damages on your print or printer. As user you are responsible for a sensible usage of this plugin.
* Be cautious not to damage your Raspberry Pi, because of wrong voltage. I don't take any responsibility for wrong wiring.

## Outlook
Support of multiple sensors for multiextruders like 4 channel kraken hotend

## Contact
* [Issues](https://github.com/maocypher/Octoprint-Smart-Filament-Sensor/issues)
* [Slack](https://maocypher.slack.com/archives/C01DG7C82UW)
