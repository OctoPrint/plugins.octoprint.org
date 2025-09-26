---
layout: plugin
id: navbartemp
title: Navbar Temp
description: Display temperatures on navbar
archive: https://github.com/imrahil/OctoPrint-NavbarTemp/archive/master.zip
homepage: https://github.com/imrahil/OctoPrint-NavbarTemp
source: https://github.com/imrahil/OctoPrint-NavbarTemp
authors:
- Cosik
- Jarek Szczepanski
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

v 0.15
- Fix few exceptions
- Themify support added Also made the CSS safe from conflicting with other elements
- Hide tools temps when not active [#80](https://github.com/imrahil/OctoPrint-NavbarTemp/issues/80)
- Fahrenheit display added [#63](https://github.com/imrahil/OctoPrint-NavbarTemp/issues/63) [#37](https://github.com/imrahil/OctoPrint-NavbarTemp/issues/37)
- Add BCM2711 as supported SoC
- Consolidate vcgencmd path between versions

v 0.14
- Temperature is visible, connection is no needed [#47](https://github.com/imrahil/OctoPrint-NavbarTemp/issues/47) [#65](https://github.com/imrahil/OctoPrint-NavbarTemp/issues/65)
- Fix for python 3 - [#68](https://github.com/imrahil/OctoPrint-NavbarTemp/issues/68)
- Support for shorter tool names - [#29](https://github.com/imrahil/OctoPrint-NavbarTemp/issues/29)
- Fix for settings saving reported in [#47](https://github.com/imrahil/OctoPrint-NavbarTemp/issues/47)
- Added possibility to remove target temperature output [#57](https://github.com/imrahil/OctoPrint-NavbarTemp/issues/57)
- Added possibility to configure soc name on navbar [#43](https://github.com/imrahil/OctoPrint-NavbarTemp/issues/47)

v 0.13
- added support for custom commands

v 0.11
- added support for all platforms running under Armbian
