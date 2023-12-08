---
layout: plugin

id: bgcode
title: BGCode
description: Adds bgcode support provided in PrusaSlicer version 2.7.0+
authors:
- jneilliii
license: AGPLv3

date: 2023-12-06

homepage: https://github.com/jneilliii/OctoPrint-BGCode
source: https://github.com/jneilliii/OctoPrint-BGCode
archive: https://github.com/jneilliii/OctoPrint-BGCode/archive/master.zip

tags:
- PrusaBuddy
- bgcode
- Prusa
- binary gcode

compatibility:
  octoprint:
  - 1.4.0
  python: ">=3,<4"

---

# BGCode

Plugin allows for the upload and conversion of bgcode files introduced in PrusaSlicer version 2.7.0+. Upon upload of the file, it will still have the bgcode extension but will be an ascii formatted text file that can be streamed to the printer as a standard gcode file from OctoPrint. 

## Why

So you may ask why I made this plugin. The answer is simple, people were posting requests to [OctoPrint](https://github.com/OctoPrint/OctoPrint/issues/4900) and the [OctoPrint Community Forum](https://community.octoprint.org/search?q=bgcode) for OctoPrint support of this new format. My personal opinion is that the best solution is to disable the new format altogether in your slicer profiles, as seen in the screenshot below.

![screenshot](/assets/img/plugins/bgcode/prusa_slicer_settings.png)

There is no good reason why anyone would want to use this new format with OctoPrint. The improvement in upload time would be countered by the extraction time of the ascii gcode upon upload. 

## Prerequisites

If installing on Windows you'll need some additional applications installed to complete the build process prior to installing the plugin. These are already included on OctoPi image, and possibly octoprint_deploy installations (need to verify). 

### Install the tools

Install Visual Studio Community 2019, or higher from [visualstudio.microsoft.com/vs/](https://visualstudio.microsoft.com/vs/).
Older versions are not supported as libbgcode requires support for C++17.
Select all workload options for C++ and make sure to launch Visual Studio after install (to ensure that the full setup completes).

Install CMake for Windows from [cmake.org](https://cmake.org/)
Download and run the exe accepting all defaults

Install git for Windows from [gitforwindows.org](https://gitforwindows.org/)
Download and run the exe accepting all defaults

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts

I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](/assets/img/plugins/bgcode/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/bgcode/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
