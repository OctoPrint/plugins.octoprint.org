---
layout: plugin

id: gcode_macro
title: Gcode Macros
description: Configure custom gcode macros you can use anywhere!
authors:
- Charlie Powell
license: AGPLv3

date: 2021-08-09

homepage: https://github.com/cp2004/OctoPrint-GCodeMacros
source: https://github.com/cp2004/OctoPrint-GCodeMacros
archive: https://github.com/cp2004/OctoPrint-GCodeMacros/releases/latest/download/release.zip

tags:
- gcode
- macro
- scripts
- custom
- productivity

screenshots:
- url: /assets/img/plugins/gcode_macro/settings.png
  alt: Screenshot of Gcode Macro Settings
  caption: Gcode Macro settings
- url: /assets/img/plugins/gcode_macro/editor.png
  alt: Screenshot of Gcode Macro Editor
  caption: Editing a gcode macro

featuredimage: /assets/img/plugins/gcode_macro/settings.png

compatibility:
  octoprint:
  - 1.5.0

  python: ">=3,<4"

---

# OctoPrint Gcode Macros Plugin

Create custom commands you can add anywhere: in your gcode file, OctoPrint's terminal, gcode scripts, or other plugins
to run a configured script.

Use macros for preheating your printer, levelling the bed, changing filament... Possibilities are (nearly) endless!

## Installation

Install from the [plugin repository](https://plugins.octoprint.org/plugins/gcode_macro) or manually using this URL:

    https://github.com/cp2004/OctoPrint-GCodeMacros/releases/latest/download/release.zip

**Warning:** This plugin only supports Python 3 installs. To find out more about upgrading your OctoPrint install to
Python 3, you can take a look
[at this post](https://community.octoprint.org/t/upgrading-your-octoprint-install-to-python-3/35158?u=charlie_powell)

## Configuration

Once installed, you can start defining your macros. All commands are prefixed with an `@`, so they don't interfere
with standard gcode commands. However, this means that **some commands are reserved**. OctoPrint uses
[these specific commands](https://docs.octoprint.org/en/master/features/atcommands.html) for pausing & resuming prints,
but also other plugins can use custom @ commands. For example, OctoLapse uses `@OCTOLAPSE TAKE-SNAPSHOT` or the WLED
plugin uses `@WLED ON` or `@WLED OFF` to control some LEDs.

The commands are **case sensitive**, and you can have spaces, numbers and punctuation in them!

*These commands will not work while printing from the printer's SD card*

## Supporting Development

I work on OctoPrint, OctoPrint plugins and help support the community in my spare time. It takes a lot of work, so
if you are interested you can [support me through GitHub Sponsors](https://github.com/sponsors/cp2004). You can
contribute monthly or one time for any amount, you choose!

