---
layout: plugin

id: terminalmessaging
title: Terminal Messaging
description: Adds styling to the terminal tab that makes it easier to see where a message is from.
author: jeffeb3
license: MIT

date: 2020-09-22

homepage: https://github.com/jeffeb3/OctoPrint-TerminalMessaging
source: https://github.com/jeffeb3/OctoPrint-TerminalMessaging
archive: https://github.com/jeffeb3/OctoPrint-TerminalMessaging/archive/master.zip

tags:
- terminal
- ui
- style
- gcode

screenshots:
- url: /assets/img/plugins/terminalmessaging/screenshot.png
  alt: screenshot of terminal with the messages on either side.
  caption: What it looks like

featuredimage: /assets/img/plugins/terminalmessaging/screenshot.png

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
  - windows
  - macos
  - freebsd

  # Compatible Python version
  #
  # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
  #
  # Plugins that only wish to support Python 3 should set it to ">=3,<4". 
  #
  # If your plugin only supports Python 2 (worst case, not recommended for newly developed plugins since Python 2
  # is EOL), leave at ">=2.7,<3"

  python: ">=2.7,<3"

---

# Octoprint-TerminalMessaging

Plugin that adds styling to the terminal tab that makes it easier to see where a message is from.

Messages you send are on the right and are in green. Messages the printer sends back are on the left
and in blue.

This is similar to how a text messaging app would differentiate between sender and receiver in the
UI.

![Screenshot](/assets/img/plugins/terminalmessaging/screenshot.png)

This plugin is very small, and just edits the css of the elements in the terminal for readability.

Enjoy!

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/jeffeb3/OctoPrint-TerminalMessaging/archive/master.zip

### Special Thanks

@jneilliii wrote this plugin after I asked about it in the forums. Thank you!
