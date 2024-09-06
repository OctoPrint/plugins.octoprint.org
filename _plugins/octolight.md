---
layout: plugin

id: octolight
title: OctoLight
description: A simple plugin to toggle a GPIO pin on a RPi. This can be toggled through a onscreen button, external button, printer events or custom GCODE.
authors:
- Steven Thomson
- Žiga Kralj
#- second autor name
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2021-01-18

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

A simple plugin that allows for the toggling of a GPIO pin on the Raspberry Pi. The user can toggle the pin through a button in the navigation bar, an external button, OctoPrint events and through custom GCODE commands. Printer events also allow the pin to be toggled on then off after a period of time.

![WebUI interface](/assets/img/plugins/octolight/screenshoot.png)


## Configuration
![Settings panel](/assets/img/plugins/octolight/settings_main.png)

### Main Light Settings
Currently, you can configure settings:
- `Light PIN`: The pin on the Raspberry Pi that the button controls.
	- Default value: 13
	- The pin number is saved in the **board layout naming** scheme (gray labels on the pinout image below).
	- **!! IMPORTANT !!** The Raspberry Pi can only control the **GPIO** pins (orange labels on the pinout image below)
	- **!! IMPORTANT !!** OctoLight will detect if the GPIO mode is set by another plugin, if not, the GPIO will be set to ``BOARD`` mode, else it will use ``BCM`` mode.  If the GPIO's are in BCM mode, you will need to use the GPIO number instead of the pin number, for example, pin 13 is GPIO 27, so the pin should be set to 27.
	![Raspberry Pi GPIO](/assets/img/plugins/octolight/rpi_gpio.png)

- `Inverted output`: If true, the output will be inverted.
	- Usage: If you have a light, that is turned off when voltage is applied to the pin (wired in negative logic), you should turn on this option, so the light isn't on when you reboot your Raspberry Pi.

- `Treat light pin as a button`: If true, the output will be treated as a button press.
	- Usage: This function allows OctoLight to toggle the Raspberry Pi pin on and off with a small delay to allow for lights that require a button press to change states.

- `Button Press delay (ms)`: This sets a time out for how long a button press is, this is only used if `Light is a button` is enabled.
	- Default value: 200
	- Note: This value is in micro seconds.

- `Delay Light Off (mins)`: This sets a time out for when the light will automatically turn its self-off in an event.
	- Default value: 5
	- Note: This value is in minutes.

<br />

![Settings panel](/assets/img/plugins/octolight/settings_button.png)

### External Button Settings

- `Enable External button`: This allows the use of an external button to change the state of the light.
	- This setting is not enabled by default, this setting must be on to use an external button

- `Button PIN`: The pin on the Raspberry Pi used to detect a button press.
	- Default value: 15
	- The pin number is saved in the **board layout naming** scheme (gray labels on the pinout image).
	- **!! IMPORTANT !!** The Raspberry Pi can only control the **GPIO** pins (orange labels on the pinout image)
	- **!! IMPORTANT !!** OctoLight will detect if the GPIO mode is set by another plugin, if not, the GPIO will be set to ``BOARD`` mode, else it will use ``BCM`` mode.  If the GPIO's are in BCM mode, you will need to use the GPIO number instead of the pin number, for example, pin 15 is GPIO 22, so the pin should be set to 22.

- `Button pin is connected to v5`: This sets the button pin to detect when the pin receives a current
	- The default is disabled
	- If you button pin is connected to a button that is connected to a ground pin, this setting should be disabled.  However, if you connect the button to a v5 pin, this setting must be enabled.

<br />

![Settings panel](/assets/img/plugins/octolight/settings_event.png)

### Event Settings

- `Setup Printer and OctoPrint Events`: This allows you to select what you would like the light to do on a printer event.
	- There are multiple events, these can each be tweaked based on your desired preference.
	- Default is set to 'Nothing'.
	- Set the light to do nothing, turn on, turn off, or turn on then turn itself off after the delay time value.

<br />

![Settings panel](/assets/img/plugins/octolight/settings_gcode.png)

### Custom GCODE Settings

- `Enable Custom GCODE Detection`: This must be enabled for GCODE to be read and toggle the light.
	- If this option is disabled, then the custom GCODE bellow this option will not function.

- `Setup Custom GCODE`: This allows you to select what you would like the light to do when a set GCODE command is sent to the printer.
	- Default is 'OCTOLIGHT ON', 'OCTOLIGHT OFF' and 'OCTOLIGHT DELAY OFF' for on, off and on with a delayed turn off respectively.
	- These commands can be any command the user enters, these could be event commands for the printer (e.g.: M600) or custom commands.


## API

**Note:** OctoLight supports API calls, please go to the following link to check the latest information: https://github.com/thomst08/OctoLight#api