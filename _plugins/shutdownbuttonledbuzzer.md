---
layout: plugin

id: shutdownbuttonledbuzzer
title: ShutdownButtonLEDBuzzer
description: It implements a shutdown physical button for the Raspberry Pi, with a buzzer and a status LED.

authors:
- danieleborgo
#- second author name
license: GPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2022-01-08

homepage: https://github.com/danieleborgo/OctoPrint-ShutdownButtonLEDBuzzer
source: https://github.com/danieleborgo/OctoPrint-ShutdownButtonLEDBuzzer
archive: https://github.com/danieleborgo/OctoPrint-ShutdownButtonLEDBuzzer/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- raspberry
- raspberrypi
- raspbian
- linux
- gpio
- shutdown
- shutdownbutton
- button
- led
- buzzer


screenshots:
- url: /assets/img/plugins/shutdownbuttonledbuzzer/circuit.png
  alt: circuit.png
  caption: Circuit scheme
- url: /assets/img/plugins/shutdownbuttonledbuzzer/settings1.png
  alt: settings1.png
  caption: Settings page
- url: /assets/img/plugins/shutdownbuttonledbuzzer/settings2.png
  alt: settings2.png
  caption: Settings page
- url: /assets/img/plugins/shutdownbuttonledbuzzer/settings3.png
  alt: settings3.png
  caption: Settings page

featuredimage: /assets/img/plugins/shutdownbuttonledbuzzer/circuit.png

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
  - 1.7.2

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
  # If your plugin only supports Python 2 it will no longer be accepted on the plugin repository.
  #
  # Uncomment the appropriate setting

  #python: ">=2.7,<3" # Python 2 & 3
  python: ">=3,<4" # Python 3 only

---

# ShutdownButtonLEDBuzzer

This OctoPrint plugin implements a shutdown physical button
for the Raspberry Pi. It offers also a status LED to know when
OctoPrint is ready and a buzzer to signal the startup and
the shutdown. Remember that these signals may vary of few
seconds.

By default, this plugin shuts down the Raspberry without
checking of there are ongoing jobs. In settings, there is
a flag to disable the button when printing.

## Notes

To shut down the Raspberry, it uses the command configured in
OctoPrint settings.

This plugin supports both active and passive buzzers. By default,
it assumes to have an active one.

## Setup

Install via the bundled
[Plugin Manager](
https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/danieleborgo/OctoPrint-ShutdownButtonLEDBuzzer/archive/master.zip


## Circuit

The circuit hereafter exposed is just the one set by default,
since the plugin allows to edit each of these pin:

- Button: by default directly on pin GPIO26
- LED: by default on pin GPIO6
- Buzzer: by default on pin GPIO13

In case one of these features is not needed, it can be
deactivated by the apposite settings section.

Always remember to properly check each connection, using
the official datasheet, before turning on the Raspberry.

![circuit](/assets/img/plugins/shutdownbuttonledbuzzer/circuit.png)

## Configuration

This plugin offers several configuration parameters,
accessible in the apposite OctoPrint section in setting:

![settings1](/assets/img/plugins/shutdownbuttonledbuzzer/settings1.png)
![settings2](/assets/img/plugins/shutdownbuttonledbuzzer/settings2.png)
![settings3](/assets/img/plugins/shutdownbuttonledbuzzer/settings3.png)

## FAQ

#### _What resistor does it need to use?_

There is no a precise resistor needed, since it depends on how much
light is needed. Despite this, it is suggested to use a value at
least of few thousands of ohms. Always remember to check the
connections and the datasheet.

#### _Which buzzer does it need?_

The plugin supports both active that passive buzzer, but it is
necessary to configure them by the settings panel.

#### Which LED does it need?

A 5 mm LED is a good option, and it is usually in Arduino kits.
In case a different one is attached, check that the current it needs
is lower than the one a Raspberry pin can give.

## License

This software is distributed on GPLv3.0, more information
available in [LICENSE.md](
https://github.com/danieleborgo/OctoPrint-ShutdownButtonLEDBuzzer/blob/master/LICENSE.md).

