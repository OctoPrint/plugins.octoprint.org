---
layout: plugin

id: bedfilamentdryer
title: Bed Filament Dryer
description: Run a heated-bed filament drying cycle with a configurable temperature, countdown, and automatic shutoff.
authors:
- Shagster19
license: AGPL-3.0-or-later

date: 2026-09-22

homepage: https://github.com/Shagster19/OctoPrint-BedFilamentDryer
source: https://github.com/Shagster19/OctoPrint-BedFilamentDryer
archive: https://github.com/Shagster19/OctoPrint-BedFilamentDryer/archive/refs/heads/main.zip

tags:
- filament
- temperature
- utility

screenshots:
- url: /assets/img/plugins/bedfilamentdryer/bedfilamentdryer-tab.png
  alt: Bed Filament Dryer controls in the OctoPrint interface
  caption: Configure the bed temperature and drying duration, monitor the countdown, or stop the heater manually.
featuredimage: /assets/img/plugins/bedfilamentdryer/bedfilamentdryer-tab.png

compatibility:
  octoprint:
  - ">=1.11.0"
  python: ">=3.9,<4"
  os:
  - linux
  - windows
  - macos
  - freebsd

attributes:
- ai-developed
---

Bed Filament Dryer uses a printer's heated bed as a timed filament drying
surface. Enter a target temperature and duration in the **Filament Dryer** tab,
then start the cycle. The plugin displays the current bed temperature and a live
countdown before automatically setting the bed target to 0&nbsp;&deg;C when the
timer expires.

The plugin refuses to start while a print is active or paused. If a print starts
during a drying cycle, it cancels its timer and leaves heater control to the
print so that a delayed cutoff cannot turn the bed off mid-print. It also
requests heater shutoff during an intentional disconnect or clean OctoPrint
shutdown while drying is active. Temperature and duration safety caps are
configurable by an administrator.

> **Safety:** This plugin is a convenience timer, not an independent thermal
> safety device. Keep firmware thermal-runaway protection enabled, remain within
> the safe limits of the printer and filament, keep flammable materials away,
> and do not leave the printer unattended. A computer crash, power loss, USB
> failure, or firmware fault can prevent software-controlled shutoff.

The plugin does not use cloud services, collect telemetry, or transmit user
data.

