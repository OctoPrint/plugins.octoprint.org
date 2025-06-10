---
layout: plugin

id: spooltracker
title: SpoolTracker
description: Simple filament tracking - load a spool, print until empty, repeat. No Spool Managment
author: thatguymendel
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2025-06-09

homepage: https://github.com/thatguymendel/OctoPrint-SpoolTracker
source: https://github.com/thatguymendel/OctoPrint-SpoolTracker
archive: https://github.com/thatguymendel/OctoPrint-SpoolTracker/archive/main.zip

tags:
- filament
- spool
- tracking
- management
- farm

screenshots:
- url: /assets/img/plugins/spooltracker/sidebar.png
  alt: sidebar screenshot
- url: /assets/img/plugins/spooltracker/popup.png
  alt: popup screenshot
---

Created by AI, this plugin simplifies filament management for farm printers. The workflow is straightforward:

1. Load a new spool
2. Enter the spool's total weight
3. Print as normal
4. Plugin automatically tracks remaining filament using gcode
5. Use remaining Filament to manage prints
6. When spool is empty, repeat with a new one

No complex spool management, no tracking multiple spools - just a simple way to know how much filament is left on your current spool. Perfect for farm printers where you want to maximize filament usage and avoid mid-print filament changes.

## Profiles

There is a save as profile option for quickly loading regularly used filament

To use a profile
1. Enter in Spool Info
2. Input profile name
3. Save profile
4. Use the Load profile dropdown to select the profile and the info will be automatically updated

## G-code Requirements

The plugin looks for the following G-code at the end of your print file to calculate filament usage:

; filament used [g] = 


Make sure your slicer includes this comment at the end of the G-code file for accurate filament tracking.

## Thing to Improve if anyone else actually wants to use this

1. Add a settings page where the user can specify the gcode to look for
2. Add optional text input to color option