---
layout: plugin

id: octolight
title: OctoLight
description: A simple plugin, that add's a button to the navbar, toggleing GPIO on the RPi. It can be used for turning on and off a light.
authors:
- Steven Thomson, previously Žiga Kralj
#- second autor name
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2023-09-16

homepage: https://github.com/thomst08/OctoLight
source: https://github.com/thomst08/OctoLight
archive: https://github.com/thomst08/OctoLight/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- raspberry pi
- gpio

screenshots:
- url: /assets/img/plugins/octolight/screenshoot.png 

featuredimage: /assets/img/plugins/octolight/screenshoot.png

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

A simple plugin that adds a button to the navigation bar for toggling a GPIO pin on the Raspberry Pi. This plugin has the function to turn on or off based on a printer event or manually through a user interaction. Printer events can also trigger a light turn off after a specified time.

![WebUI interface](img/screenshoot.png)


## Configuration
![Settings panel](img/settings.png)

Curently, you can configure settings:
- `Light PIN`: The pin on the Raspberry Pi that the button controls.
	- Default value: 13
	- The pin number is saved in the **board layout naming** scheme (gray labels on the pinout image below).
	- **!! IMPORTANT !!** The Raspberry Pi can only control the **GPIO** pins (orange labels on the pinout image below)
	![Raspberry Pi GPIO](img/rpi_gpio.png)

- `Inverted output`: If true, the output will be inverted
	- Usage: if you have a light, that is turned off when voltage is applied to the pin (wired in negative logic), you should turn on this option, so the light isn't on when you reboot your Raspberry Pi.

- `Setup Delay Turn off time`: This sets a time out for when the light will automatically turn its self off in an event
	- Default value: 5
	- Note: This value is in minutes

- `Setup Printer Events`: This allows you to select what you would like the light to do on a printer event
	- Default is nothing
	- Set the light to do nothing, turn on, turn off, or turn on then turn itself off after the delay time value