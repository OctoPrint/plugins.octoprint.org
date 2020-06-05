---
layout: plugin

id: signalclirestapi
title: Signalclirestapi
description: Another Signal Messenger Integration based on the signal-cli-rest-api docker image. Supports Signal Messenger groups and print progress.
author: Bernhard B.
license: AGPLv3

date: 2020-06-05 

homepage: https://github.com/bbernhard/OctoPrint-Signalclirestapi
source: https://github.com/bbernhard/OctoPrint-Signalclirestapi
archive: https://github.com/bbernhard/OctoPrint-Signalclirestapi/archive/master.zip


# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- notification 


screenshots:
- url: /assets/img/plugins/signalclirestapi/config1.png
  alt: Signal Messenger Configuration Part1
  caption: Signal Messenger Configuration Part1
- url: /assets/img/plugins/signalclirestapi/config2.png
  alt: Signal Messenger Configuration Part2
  caption: Signal Messenger Configuration Part2
- url: /assets/img/plugins/signalclirestapi/config3.png
  alt: Signal Messenger Configuration Part3
  caption: Signal Messenger Configuration Part3
- url: /assets/img/plugins/signalclirestapi/config4.png
  alt: Signal Messenger Configuration Part4
  caption: Signal Messenger Configuration Part4

- url: /assets/img/plugins/signalclirestapi/signal1.png
  alt: Signal Messenger Screenshot
  caption: Supports Signal Messenger groups

featuredimage: /assets/img/plugins/signalclirestapi/config1.png

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
  - 1.2.0

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
  # is EOL), leave at ">=2.7,<3"
  
  python: ">=2.7,<4"

---

# Features 

* Support for Signal Messenger groups: 
  
  It's possible to create a Signal Messenger group for every print job. That way, all the messages and webcam snapshots are nicely grouped together. 

* Support for Print Progress:
  
  If enabled, a message will be sent when the print job progress reaches 20%, 40, 80%.

* Support for all Print Events: 
  
  The plugin supports the `Print Started`, `Print Failed`, `Print Cancelled`, `Print Paused`, `Print Resumed`, `Print Done` events.

* Support for signal-cli-rest-api: 
  
  The [signal-cli-rest-api](https://github.com/bbernhard/signal-cli-rest-api) is a small REST API wrapper around the awesome [signal-cli](https://github.com/AsamK/signal-cli) commandline tool. The main advantage is, that you don't need to run `signal-cli` on the same host as your Octoprint instance. That's especially useful, if you use other services in your home network (like [Home Assistant](https://www.home-assistant.io/)) that also send Signal Messenger notifications.
