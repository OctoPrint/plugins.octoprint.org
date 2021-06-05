---
layout: plugin

id: fortune
title: OctoPrint-Fortune
description: Gives you a pithy fortune on web login or startup
authors:
- Stephen Berry
license: BSD

date: 2021-06-04

homepage: https://github.com/berrystephenw/OctoPrint-Fortune
source: https://github.com/berrystephenw/OctoPrint-Fortune
archive: https://github.com/berrystephenw/OctoPrint-Fortune/archive/main.zip

tags:
- fortune
- text 
- notification

# TODO
screenshots:
- url: /assets/img/plugins/fortune/fortune-1.png
  alt: Fortune message on login
  caption: Your fortune
- url: /assets/img/plugins/fortune/IMG_6255.PNG
  alt: text fortune
  caption: Fortune sent to OctoText

featuredimage: /assets/img/plugins/fortune/fortune-1

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
  # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
  #
  # Plugins that only wish to support Python 3 should set it to ">=3,<4".
  #
  # If your plugin only supports Python 2 (worst case, not recommended for newly developed plugins since Python 2
  # is EOL), leave at ">=2.7,<3" - be aware that your plugin will not be allowed to register on the
  # plugin repository if it only support Python 2.

  python: ">=3,<4"

---

This is an adaptation of the original UNIX fortune program. Fortune will 
run on OctoPrint login and popup a quote or saying from a database of stored quotes.

I have not created these quotes or sayings, they are simply provided from the
source given by Brian M. Clapper as a sample set of fortunes.

http://software.clapper.org/fortune/

There is an icon that looks like a book on the navigation bar for those that 
would like a more frequent fortune. This can be turned off in the settings page.

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/berrystephenw/OctoPrint-Fortune/archive/main.zip

This is a Python 3 or greater plugin!

## Configuration

The only configuration is to enable or disable the icon on the navigation bar, and optionally 
to enable sending your fortune to OctoText. [OctoText](https://plugins.octoprint.org/plugins/OctoText/) must be enabled and configured for
this feature to work.

## Copyright

Copyright © 2008-2019 Brian M. Clapper. All rights reserved.

