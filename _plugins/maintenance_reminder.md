---
layout: plugin

id: maintenance_reminder
title: OctoPrint-Maintenance-Reminder
description: Receive maintenance notifications when you complete a certain number of prints
authors:
    - Garron Anderson
license: AGPL-3.0-or-later

date: 2026-07-03

homepage: https://github.com/GarronAnderson/OctoPrint-Maintenance-Reminder
source: https://github.com/GarronAnderson/OctoPrint-Maintenance-Reminder
archive: https://github.com/GarronAnderson/OctoPrint-Maintenance-Reminder/archive/main.zip

# TODO
tags:
    - maintenance
    - reminders
    - alerts
    - monitoring

# TODO
# When registering a plugin on plugins.octoprint.org, all screenshots should be uploaded not linked from external sites.
screenshots:
    - url: /assets/img/plugins/maintenance_reminder/maintenance_navbar.png
      alt: icon in navbar
      caption: Icon in navbar
	- url: /assets/img/plugins/maintenance_reminder/maintenance_popover.png
      alt: popover from navbar
      caption: Popover showing maintenance status
    - url: /assets/img/plugins/maintenance_reminder/maintenance_modal.png
      alt: modal showing maintenance due
      caption: Modal before printing with maintenance due
    - ...

# TODO
featuredimage: /assets/img/plugins/maintenance_reminder/maintenance_popover.png

# TODO
# If any of the below attributes apply to your project, uncomment the corresponding lines. This is MANDATORY!

attributes:
#  - cloud  # if your plugin requires access to a cloud to function
#  - commercial  # if your plugin has a commercial aspect to it
#  - free-tier  # if your plugin has a free tier
---

# Maintenance Reminder

I wrote this plugin because I wanted OctoPrint to remind me to wash my PEI sheet and was suprised to find there wasn't already a plugin for that. So, I decided to fill the gap.

This plugin counts completed prints and increments counters. You set up a reminder with a certain number of prints, and when it reaches that number, a message shows in the navbar and a modal appears before each print. You are offered the option to cancel the print, ignore the maintenance, or reset and continue. You can also view maintenance status in a popover from the navbar.

I may add support for notifications via ntfy.sh in the future.