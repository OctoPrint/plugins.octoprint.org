---
layout: plugin

id: Nozzle_Filament_Validator
title: OctoPrint-Nozzle-Filament-Validator
description: Validate nozzle size and filament type before starting a print.
authors:
  - Rylan Meilutis
license: AGPLv3

date: 2024-02-26

homepage: https://github.com/Rylan-Meilutis/OctoPrint-Nozzle-Filament-Validator
source: https://github.com/Rylan-Meilutis/OctoPrint-Nozzle-Filament-Validator
archive: https://github.com/Rylan-Meilutis/OctoPrint-Nozzle-Filament-Validator/archive/master.zip

tags:
  - filament
  - error checking
  - print validation
  - nozzle size checking
  - build plate checking

# When registering a plugin on plugins.octoprint.org, all screenshots should be uploaded not linked from external sites.
screenshots:
  - url: /assets/img/plugins/Nozzle_Filament_Validator/settings_page.png
    alt: the settings page
    caption: The settings page for the plugin.
  - url: /assets/img/plugins/Nozzle_Filament_Validator/caught_error.png
    alt: the notification of an error
    caption: An example notification of an error. This one is for incorrect filament type.
  - url: /assets/img/plugins/Nozzle_Filament_Validator/success.png
    alt: notification of a successful validation
    caption: An example notification of a successful validation.

featuredimage: /assets/img/plugins/Nozzle_Filament_Validator/settings_page.png

compatibility:

  octoprint:
    - 1.9.3

  os:
    - linux
    - windows
    - macos
    - freebsd
  python: ">=3.10,<4"

---

# OctoPrint-Nozzle-Filament-Validator

This plugin validates nozzle size, build plate, and filament type before starting a print.
It uses provided gcode setting to work, it is not a replacement for checking yourself but
can help to prevent simple
mistakes from occurring.

## Needed plugins

- [Spool Manager](https://plugins.octoprint.org/plugins/SpoolManager/) - This plugin will
  automatically set the filament type for the spool if you have it installed and have set
  the filament type for the spool.

## Configuration

Go to plugin settings and set your nozzle size, and build plate.
Filament type should be set automatically if you have spool manager installed and have set
the filament type for the
spool.
When you go to print, the plugin will check if the gcode settings match the settings you
have set, and that the current filament is supported by the selected build plate. If it
does not match, it will notify you of the error. If it does match, it will notify you of a
successful validation.


