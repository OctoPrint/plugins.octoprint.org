---
layout: plugin

id: filamentbuddy
title: FilamentBuddy
description: This plugin implements three features, filament change buttons, filament sensor manager and filament remover when the print is completed.

authors:
- danieleborgo
#- second author name
license: GPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2024-01-21

homepage: https://github.com/danieleborgo/OctoPrint-FilamentBuddy
source: https://github.com/danieleborgo/OctoPrint-FilamentBuddy
archive: https://github.com/danieleborgo/OctoPrint-FilamentBuddy/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- gpio
- raspberry
- raspberrypi
- raspbian
- linux
- filamentbuddy
- filament-changer
- filament-sensor
- filament-remover
- sensor

screenshots:
- url: /assets/img/plugins/filamentbuddy/fc_simplified.png
  alt: Filament Changer settings
  caption: Filament Changer settings
- url: /assets/img/plugins/filamentbuddy/fs_polling.png
  alt: Filament Sensor settings
  caption: Filament Sensor settings
- url: /assets/img/plugins/filamentbuddy/fr_simplified.png
  alt: Filament Remover settings
  caption: Filament Remover settings
- url: /assets/img/plugins/filamentbuddy/info_window.png
  alt: FilamentBuddy help
  caption: FilamentBuddy help

featuredimage: /assets/img/plugins/filamentbuddy/fc_simplified.png

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
  - windows

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

# FilamentBuddy

This plugin implements three features: filament change buttons, filament
sensor manager and filament remover when the print is completed.

These three features are independently implemented so, they can be
activated separately.

### Filament Changer

This feature implements two buttons in the _control_ section to change
the filament. Their role is to remove and to insert the filament sending
G-code command, which can be configured by the user via the settings 
page. This last page has two methods of configuration: one guided and
one completely free.

### Filament Sensor

This functionality allows to monitor the filament availability via a
hardware sensor, which  sends this information via a proper GPIO pin. 
When the plugin, during a print, notices that the filament has run out,
it pauses the printer, avoiding it to fail and waiting for filament
replacement, which can be done by hand, by another plugin or, better,
via the feature _Filament Changer_.
This plugin also has a toolbar indicator to signal if the filament is 
inserted or not and a run out MQTT notification.

The currently supported sensors are the ones that uses a binary digital
value, one for the filament inserted and the other where it is not.
Moreover, there are a lot of configurations that can be configured in
the settings page to more meet every user needs.

Remember that the Raspberry works with digital pin to **3.3V**, so keep
this in mind when connecting stuff to the GPIO. Moreover, _always check
multiple times_ every connection before turning on the board since
there is always the risk to seriously damage the hardware.

### Filament Remover

Sometimes happens that, when the print is over, the nozzle cools down
with the filament still inserted, requiring to heat it up again to
remove it. This feature solves this issue, running a user configurable
G-code snippet to remove the filament when the printer ends, fails or
is canceled. It also has the possibility to automatically insert the 
filament before printing. 

## Setup

Install via the bundled 
[Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/danieleborgo/OctoPrint-FilamentBuddy/archive/master.zip

All the stuff that the plugin needs to work are automatically installed
via OctoPrint plugin manager, so no other software are needed.

In some configurations, some parameters cannot be used, consequently
there is a mechanism to hide the values that the user cannot set, to
avoid confusion.

### Limitations

This plugin is thought to run on a Raspberry with a Marlin printer but,
if properly configured, _Filament Changer_ and _Filament Remover_ could
also work on different boards and printers. Despite this, these two
would require to manually specify the G-code commands to perform these 
operations.

The _Filament Sensor_ module is different since it uses a Python module
specifically developed for the Raspberry boards, _gpiozero_, so it has
this board as prerequisite. Nevertheless, Marlin is not a requirement,
since it only uses OctoPrint functionalities. In the case FilamentBuddy
is not running on a Raspberry Pi, the plugin will disable this feature.

## Setup

The three features can be used independently, hence if the user needs
just one or two of them, can just disable what is not wanted.

On the first startup, everything will be disabled and, through a 
notification, the plugin will remember to the user to do the first 
configuration. This can be done via a guided procedures or directly 
setting all the parameters. 

## Help

<img width="50%" src="/assets/img/plugins/filamentbuddy/info_button.png" alt="" align="right">
Almost all the parameters in configuration have on their side a button
that, if clicked, shows an explanation of what that value is meant to do.
For some users, these explanation may seem too detailed but they are
thought to be complete.

## Note for developers

Since it is impossible to cover all the available filament sensors on
the market, this plugin is easily extensible to support other models
in the future. More in details, it has an abstract class named 
_GenericFilamentSensorManager_, which can extended to support new sensor,
implementing its abstract methods, which are, hopefully, generic enough.
The plugin instantiates these in the _initialize_filament_sensor_ method
and it treats them as the abstract class, so it can support multiple
different filament sensors without changing other code parts.

## FAQ

#### _Can I use just one feature among these three?_

Yes, it is possible to use just what you need, enabling just the feature
that are needed.

#### _I don't know what a parameter is, what do I do?_

On the side on almost all parameters in configuration, there is a button
that shows an explanation of what that value represents.

#### _If I don't like the guided procedure, can I skip it?_

Yes, you can set the mode as you like, even specifying your G-code
commands directly, if you need, or you do not have a Marlin printer.

#### _Which filament sensors does this plugin support?_

Currently, it supports some digital ones, so the sensor that uses a 
voltage value to define the filament availability and the other when
it is not. Into the configuration page, it is possible to define if
the filament is available when the voltage high or low. From my 
limited experience, these are the sensors I can find more easily.
Since the filament sensor has been made generic, there may be new
filament sensors implemented in the future.

#### _How do I select the correct pin to connect the filament sensor?_

There is not a real answer to this question since it depends on
what the user needs. The plugin just requires a just BCM pin, and they
can be identified by the name starting with _GPIO_, as shown in this
[plugin](https://plugins.octoprint.org/plugins/gpiostatus/).

#### _Why do some parameters disappear when configuring?_

Some configurations are available only when certain conditions are
met. For instance, in _Filament Changer_, some features configurable
for _G0_ are not available for _M600_ and the other way around. To
avoid confusion, the plugin just shows only what is available for
that configuration.

#### _Which are the limitations? Does it work on other boards?_

Check the section [limitations](#limitations).

#### Why do filament changer or remover not work?

Some Marlin printers may have a check regarding the temperatures before
moving the extruder. So if the nozzle temperature, or the bed one, are
lower than a predefined threshold, the commands for the extruder are
not executed. Since, in some cases the printer is still hot enough to
perform these operations, it is possible to disable this check through
the command _M302 P1_. For these cases, check the flag _Force Command_
in their settings page.

## Screenshots

More images available [here](https://github.com/danieleborgo/OctoPrint-FilamentBuddy/blob/master/images/).


## License

This software is distributed on GPLv3.0, more information
available in
[LICENSE.md](https://github.com/danieleborgo/OctoPrint-FilamentBuddy/blob/master/LICENSE).
