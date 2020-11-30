---
layout: plugin

id: FriendlyBeeper
title: Friendly Neighborhood Beeper
description: Beeps after completion/failure of a print, but only during the specified hours
author: Alex Bahm
license: AGPLv3

date: 2020-04-25

homepage: https://github.com/techfreek/OctoPrint-Friendlybeeper
source: https://github.com/techfreek/OctoPrint-Friendlybeeper
archive: https://github.com/techfreek/OctoPrint-Friendlybeeper/archive/master.zip

follow_dependency_links: false

tags:
- notification
- beep
- print finished
- simple
- control

screenshots:
- url: /assets/img/plugins/FriendlyBeeper/settings.png
  alt: Friendly Neighborhood Beeper settigns
  caption: Config options for FNB. Current time is displayed as the OctoPrint host may be out of sync.

featuredimage: /assets/img/plugins/FriendlyBeeper/settings.png

compatibility:
  python: ">=2.7,<4"

---

This plugin is designed to be used to notify when a print is complete. While gcode to beep on print completion can easily be added to the slicer/octoprint, I wanted a way to only beep during certain time frames as I don't want my neighbors to hate me for my printer beeping at 2 in the morning.

# Requirements
- Currently requires the use of Gcode M300 to trigger the beep

# Configuration
## Active Hours
These settings define the hours the printer may beep when the printer completes. These default to 8am - 10pm as I won't likely be checking my printer outside those hours.

## Beep Tone Settings
If you want to change the tone, or duration of the beep the printer makes, these can be changed to modify that.

Can be configured for custom tones

## Beep Settings

Notify On Pause: Allow notification on pause events
Wait for Cooldown: Will delay the beep until the bed has reached the indicated temperature (while respecting active hours)
