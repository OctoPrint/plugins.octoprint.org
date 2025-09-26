---
layout: plugin

id: cmdexec
title: Cmd exec
description: Execute bash commands from Octoprint's UI
authors:
- Alexis Coulombe
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2023-06-13

homepage: https://github.com/alexis-coulombe/Octoprint-CmdExec/
source: https://github.com/alexis-coulombe/Octoprint-CmdExec/
archive: https://github.com/alexis-coulombe/Octoprint-CmdExec/archive/master.zip

# Set this if your plugin heavily interacts with any kind of cloud services.
#privacypolicy: your plugin's privacy policy URL

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- cmdexec
- command
- bash
- script
- shell

screenshots:
- url: /assets/img/plugins/cmdexec/setting.png
  alt: Octoprint cmdexec plugin
  caption: Octoprint cmdexec plugin

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
  python: ">=3.7,<4" # Python 3 only

---

## Description

This plugin allows executing custom shell commands through the Octoprint's UI using a button.

## Configuration

In the plugin's settings page, enter the commands you want to execute using the navbar button. You can also change the navbar icon if you want.

You can chain commands with the ```&&``` and write the result of a command to a file with ```>>```.
Here is an example to execute 3 commands: ```command1 && command2 && command3 >> log.txt```

You can also execute a script directly on your computer by writing the path to the script ```./path/to/script```

**The command execution is only allowed by admin users**

## Usage

- Toggle power of a device
- Toggle power of the usb hub
- Toggle power of led strip connected to this device
- Log information at a specific time
- Send an email / sms
- Log device stats to a file
- Execute any custom scripts at a specific time

https://github.com/alexis-coulombe/Octoprint-CmdExec
