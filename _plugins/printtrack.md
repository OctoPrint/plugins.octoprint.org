---
layout: plugin

id: printtrack
title: OctoPrint-PrintTrack
description: Keep track of your printer and prints with some simple additions & customizability.
author: ElectricSquid
license: AGPLv3

# TODO
date: 2019-02-25

homepage: https://github.com/ElectricSquid/OctoPrint-PrintTrack
source: https://github.com/ElectricSquid/OctoPrint-PrintTrack
archive: https://github.com/ElectricSquid/OctoPrint-PrintTrack/archive/master.zip

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

# TODO
tags:
- connection
- status
- monitor
- monitoring
- notification
- notifications
- progress
- remote monitoring
- title

# TODO
screenshots:
- url: /assets/img/plugins/printtrack/printtrack_settings.png
  alt: screenshot showing the options menu of customizability
  caption: The settings that can be changed as of version 1.0.2
- url: /assets/img/plugins/printtrack/printtrack_title.png
  alt: screenshot of the title bar replacement
  caption: The title of your octoprint window being changed to the status of the printer

# TODO
featuredimage: /assets/img/plugins/printtrack/printtrack_title.png

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

  python: ">=2.7,<4"

---

### OctoPrint-PrintTrack
This plugin is meant to help you keep track of your printers progress and status. Currently it will display the printers status in the tab of OctoPrint in the browser. There are customization options to change how it is displayed and also has adjustable strings so you can translate them or just make them something else.  

#### Install & Setup
Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager) or manually using this URL:  
```https://github.com/ElectricSquid/OctoPrint-PrintTrack/archive/master.zip```

#### Reporting Issues & Improvments
If you encounter any issues or bugs with the plugin please feel free to make an issue on the repo. I also fully support additions to the plugin from third partys. If you have an idea or an already developed solution that would implement with the plugin well please submit it to the github repo and I will gladly consider additions and contributions.

See the [github page](https://github.com/ElectricSquid/OctoPrint-PrintTrack) for more details.