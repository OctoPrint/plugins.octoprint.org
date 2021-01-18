---
layout: plugin

id: OctoBuddy
title: OctoBuddy
description: A plugin that allows common printer actions to be performed with physical buttons via GPIO
authors:
- Mark Lorenz
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2021/01/17

homepage: https://github.com/mlo821/OctoBuddy
source: https://github.com/mlo821/OctoBuddy
archive: https://github.com/mlo821/OctoBuddy/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- control
- heat bed
- GPIO
- easy control
- heat nozzle
- jog axis
- home printer
- push button
- pushbutton
- printer interface

screenshots:
- url: /assets/img/plugins/OctoBuddy/ShelfMount1.jpg
  alt: OctoBuddy Shelf Mount Version
  caption: OctoBuddy Shelf Mount Version
- url: /assets/img/plugins/OctoBuddy/OctoBuddySettings.png
  alt: OctoBuddy Shelf Mount Version
  caption: OctoBuddy Shelf Mount Version
- url: /assets/img/plugins/OctoBuddy/ShelfMount2.jpg
  alt: OctoBuddy Shelf Mount Version
  caption: OctoBuddy Shelf Mount Version
- url: /assets/img/plugins/OctoBuddy/ShelfMount4.jpg
  alt: OctoBuddy Shelf Mount Version
  caption: OctoBuddy Shelf Mount Version

featuredimage: /assets/img/plugins/OctoBuddy/ShelfMount1.jpg

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
OctoBuddy is 3D printable button panel with an accompanying OctoPrint plugin that lets perform common printer actions like moving your print head with the push of a single button.  It let’s you speed up things like maintenance, troubleshooting, and filament changes much quicker and easier by bypassing the need to access OctoPrint interface or cumbersome printer menus.  The concept is simple, connect a button to the Raspberry Pi GPIO interface and tell the plugin which what action you want the port to perform.  You can mount your buttons to one of the <a href="https://www.thingiverse.com/thing:4727285"> my button panels </a> or make your own.

OctoBuddy can currently perform the following actions:
<ul>
    <li>Home Printer</li>
    <li>Jog any Axis by a configurable distance</li>
    <li>Toggle bed temperature between a configurable temperature and 0</li>
    <li>Toggle nozzle temperature between a configurable temperature and 0</li>
</ul>

For a full how-to on building your own OctoBuddy go here: https://www.factoryrestart.com/octobuddy

I build these things cause I like it.  I make them available to you because… well, why not.  If you like my work and would like to donate just click <a href="https://www.paypal.com/donate?hosted_button_id=JVWDV6EYGZ7W6">here</a>.  All contributions are much appreciated.
