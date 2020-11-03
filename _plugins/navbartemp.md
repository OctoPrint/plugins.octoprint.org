---
layout: plugin
id: navbartemp
title: Navbar Temp
description: Display temperatures on navbar
archive: https://github.com/imrahil/OctoPrint-NavbarTemp/archive/master.zip
homepage: https://github.com/imrahil/OctoPrint-NavbarTemp
source: https://github.com/imrahil/OctoPrint-NavbarTemp
author: Jarek Szczepanski & Cosik
license: AGPLv3
featuredimage: https://github.com/imrahil/OctoPrint-NavbarTemp/blob/master/images/navbar.png?raw=true
date: 2015-04-17

tags:
- temperature
- heater
- navbar
- temp

compatibility:

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=2.7,<4"
---

# Plugin for OctoPrint - displays temperatures on navbar

![NavbarTemp](https://github.com/imrahil/OctoPrint-NavbarTemp/blob/master/images/navbar.png?raw=true)


## Setup

Install the plugin using Plugin Manager from Settings

## Need new platform support?
If you need support for additional platform, please inform us and add such information:
* How to read temperature
* How to define platform type

And be ready for testing.

## Custom command
Plugin is supporting up to one custom command, in navbar will be displayed raw output
of command.
Example:
![NavbarTemp](https://github.com/imrahil/OctoPrint-NavbarTemp/blob/master/images/custom_cmd_cfg1.png?raw=true)

![NavbarTemp](https://github.com/imrahil/OctoPrint-NavbarTemp/blob/master/images/custom_cmd_bar1.png?raw=true)


## Change notes:
v 0.13
- added support for custom commands

v 0.11
- added support for all platforms running under Armbian
