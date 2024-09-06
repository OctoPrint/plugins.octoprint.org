---
layout: plugin

id: filamentmotionsensor
title: Octoprint-Filament-Motion-Sensor
description: Filament jam or runout sensor using a photodiode or a smart sensor connected directly to Raspberry pi. 
authors: 
- Tabahi

license: GPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2024-08-11

homepage: https://github.com/tabahi/Octoprint-Filament-Motion-Sensor
source: https://github.com/tabahi/Octoprint-Filament-Motion-Sensor
archive: https://github.com/tabahi/Octoprint-Filament-Motion-Sensor/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- Sensor
- Filament
- Motion
- Jam

screenshots:
- url: /assets/img/plugins/filamentmotionsensor/settings.png
  alt: Screenshot of the plugin in settings
  caption: Filament Motion Sensor's Settings
- url: /assets/img/plugins/filamentmotionsensor/sidebar.png
  alt: Screenshot of the plugin on the sidebar
  caption: Filament Motion Sensor's sidebar view during a print jam
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
  - 1.4.0

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

  python: ">=3.8,<4"

---

# Octoprint-Filament-Motion-Sensor

An [OctoPrint](http://octoprint.org/) plugin for filament motion sensor connected directly to RaspberryPi's GPIO pin.


 This new version supports the latest Raspbian OS and RPi5. This plugin revision is still pretty new and can have issues with untested environments. Try using [other forks](https://github.com/hviet17/Octoprint-Smart-Filament-Sensor) if this one doesn't work especially on RPi3 and older. Initial work based on the [Octoprint-Filament-Reloaded](https://github.com/kontakt/Octoprint-Filament-Reloaded) plugin by kontakt,  [Octoprint-Filament-Revolutions](https://github.com/RomRider/Octoprint-Filament-Revolutions) plugin by RomRider, and is a fork of  [Octoprint-Smart-Filament-Sensor](https://github.com/Royrdan/Octoprint-Smart-Filament-Sensor) by Royrdan.


## Required sensor

To use this plugin a Filament Sensor needs to be sending a toggling digital signal (0-1-0...) during filament movement.
- A ready-made sensor can be used such as BIGTREETECH Smart Filament Sensor.
- You can also make one yourself using a slotted wheel, an LED, and a photo-diode. Connect the output of the photo-diode to a GPIO pin of RPi. Make sure to not input more than 3.3V to raspberry pi. Here is an example (rather complicated) model by [Ludwig3D on Thingiverse](https://www.thingiverse.com/thing:3071723).

## Features
*  Detects filament jams, runrouts, clogs, spool tangles and pauses the print automatically.
* Uses highly responsive GPIO interrupts.
* Can respond within a second of no-filament-motion.
*  Configuration limits and timeouts for pausing.
* Custom GCode on pause.
* Heaters timeout after pause.

## Installation

* Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager).
* Manual install: Scroll down the "Get more" menu in Plugin Manager, Use this URL: https://github.com/tabahi/Octoprint-Smart-Filament-Sensor/archive/master.zip

After installation a restart of Octoprint is required.

## Configuration
### GPIO Pin
* Choose any free GPIO pin you for data usage, but I would recommend to use GPIO pins without special functionalities like e.g. I2C
* Run the sensor only on 3.3V, because GPIO pins don't like 5V for a long time

### Pausing Limits
A print can be paused due to two limits when the filament is not moving:

1. Extrusion distance limit after jam. It's best to set between 5mm (slow) and 20mm (fast) depending on the print speed. With retractions, the filament might not move much triggering this limit therefore a grace-period can be set to override this limit for a couple of seconds.
2. Timeout after jam. Seconds to wait after no-filament-motion before pausing. 5s for very fast print, 120s for very slow prints.

### Octoprint - Firmware & Protocol
If you are not printing by SD card, then the octoprint @pause command is pretty simple and works for most. However, there is a custom GCode option with or without Octoprint's pause if you want to send commands such as M600 for filament change. By default, the custom GCode is just a beep tune.

### Octoprint - GCode Scripts
The custom GCode managed by the plugin is only run when a print is paused due to a suspected jam. You can also add a GCode Script for "After print job is paused" in OctoPrint Settings > GCode Scripts that will run for all pauses. Make sure to not overlap the two. Also adding a GCode script for "Before print job is resumed" might be useful, in the case you hit the heatbed or print head during the change of the filament or removing the blockage.

## Disclaimer
* I and all the previous authors of this plugin are not responsible for any damages on your print or printer. As user you are responsible for a sensible usage of this plugin.
* Be cautious not to damage your Raspberry Pi, because of wrong voltage. I don't take any responsibility for wrong wiring.
* Try custom GCode commands at your own risk.


## Outlook
* Telegram notifications.
* A simplified DIY sensor
* Support of multiple sensors for multiextruders. Depending on the demand.

## Contact
* [Issues](https://github.com/tabahi/Octoprint-Smart-Filament-Sensor/issues)
* [Octoprint Discord](https://discord.octoprint.org/)

