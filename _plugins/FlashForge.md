---
layout: plugin

id: flashforge
title: Flashforge/Dremel/PowerSpec Printer Support
description: Enable OctoPrint to connect to certain FlashForge, Dremel and PowerSpec printers.
author: Mrnt
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2020-05-18

homepage: https://github.com/Mrnt/OctoPrint-FlashForge
source: https://github.com/Mrnt/OctoPrint-FlashForge
archive: https://github.com/Mrnt/OctoPrint-FlashForge/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- FlashForge
- Dremel
- PowerSpec

screenshots:

featuredimage:

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
      
  python: ">=2.7,<4"
      
---

The plugin allows control of some FlashForge, Dremel and PowerSpec printers
(such as the FlashForge Finder, Dreamer, etc) that connect via USB and do not
appear as a serial port under OctoPrint.

## IMPORTANT
For details of which printers are supported and **the level of functionality**
see the [homepage](https://github.com/Mrnt/OctoPrint-FlashForge/blob/master/README.md)
<br />
<hr />
<br />

### Support Additional Development
This plugin was/is developed by painstakingly reverse engineering the communication
between FlashPrint and FlashForge printers and much trial and error. If you find it
useful and/or want to see continued development, please consider making a donation.

[![More chocolate, more code](/assets/img/plugins/flashforge/paypal-donate.png)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&amp;hosted_button_id=S4TNWVKFLPL5C&amp;source=url)


