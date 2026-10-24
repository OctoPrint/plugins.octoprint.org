---
layout: plugin

id: octolightHA
title: OctoLight Home Assistant
description: Control Home Assistant lights and switches from OctoPrint, with brightness, colour, print status lighting and delayed shutoff.
authors:
- Mark Bloom
- idontwantfame
license: AGPL-3.0-or-later
date: 2023-07-04

homepage: https://github.com/mark-bloom/OctoLight_Home-Assistant
source: https://github.com/mark-bloom/OctoLight_Home-Assistant
archive: https://github.com/mark-bloom/OctoLight_Home-Assistant/archive/master.zip

tags:
- raspberry pi
- home assistant
- lights
- switch
- automation
- gcode

screenshots:
- url: /assets/img/plugins/octolightHA/controls.png
  alt: OctoLight Home Assistant navbar controls for brightness and colour
  caption: Toggle configured entities and adjust supported lights from the OctoPrint navbar.
- url: /assets/img/plugins/octolightHA/settings.png
  alt: OctoLight Home Assistant connection settings and entity discovery
  caption: Connect to Home Assistant, search for entities and test access before saving.
- url: /assets/img/plugins/octolightHA/automation.png
  alt: OctoLight Home Assistant print automation and light appearance settings
  caption: Configure delayed shutoff, host commands, brightness defaults and print status colours.

featuredimage: /assets/img/plugins/octolightHA/controls.png

compatibility:
  octoprint:
  - ">=1.11.8,<3"
  os:
  - linux
  python: ">=3.9,<4"

attributes:
- ai-developed
---

Control your printer enclosure lighting and other Home Assistant lights or switches
from OctoPrint. Search for entities in settings, toggle them from the navbar, and
adjust brightness or RGB colour on supported lights. Optional automation follows
print events and switches lights off after a configurable delay.

Maintained by Mark Bloom and idontwantfame, originally based on
[OctoLight by Žiga Kralj](https://github.com/gigibu5/OctoLight).

## Features

- Search Home Assistant by friendly name or entity ID and test access before saving.
- Control multiple entities independently, with individual navbar icons, print
  automation settings and shutoff timers.
- Adjust brightness and RGB colour from navbar menus or configure turn-on defaults.
- Refresh state from Home Assistant, including changes made in other apps.
  Unavailable entities are distinguished from lights that are off.
- Optionally apply configurable colours for printing, pause, completion, cancellation
  and errors, plus a native short error flash on supported lights.
- Turn lights on at print start and off after completion, failure or cancellation.
  New prints and manual controls cancel pending completion shutoff timers.
- Control configured entities using opt-in `@OCTOLIGHT` host commands or an
  authenticated HTTP API.

Brightness, RGB colour and native flashes depend on each light's capabilities.
`switch` and `input_boolean` entities provide on/off control.

## Requirements and setup

Requires Python **>=3.9,<4**, OctoPrint **>=1.11.8,<3** on Linux, and a Home
Assistant instance reachable from the OctoPrint host. Create a Home Assistant
long-lived access token with access to the entities you want to control.

1. Install the plugin and restart OctoPrint.
2. Open **Settings → OctoLight Home Assistant**.
3. Enter your Home Assistant URL and long-lived access token.
4. Select **Search Home Assistant**, then choose a light, switch or input boolean.
5. Select **Test connection and entity**, save, and configure optional automation.

Tested with OctoPrint **1.11.8 / Python 3.9 and 3.10**, and
**2.0.0rc7 / Python 3.12**. OctoPrint 2 testing covers this release candidate.
Automated checks use Linux and a simulated Home Assistant; physical devices,
Windows and macOS have not been verified.

## G-code and API

Enable **@OCTOLIGHT host commands** in settings to control configured entities from
OctoPrint's Terminal, G-code scripts, streamed G-code files or OctoDash actions:

```gcode
@OCTOLIGHT on
@OCTOLIGHT set brightness=75 color=#ff8000
@OCTOLIGHT set light.printer color=#ff0000 flash=short
@OCTOLIGHT off
```

Commands run asynchronously and target configured entities only. Printing directly
from a printer's SD card does not process these host commands.

The API is `/api/plugin/octolightHA`. GET reads cached state; authenticated JSON
POST requests operate lights. See the
[API documentation](https://github.com/mark-bloom/OctoLight_Home-Assistant#http-api)
for commands and permission requirements.

## Upgrading

Existing OctoLight Home Assistant installations upgrade in place. The plugin
identifier, settings and update source remain the same, so no settings import is
needed. Integrations using GET requests to toggle, turn on or turn off lights must
switch to authenticated JSON POST commands on the same API endpoint.

## Connections and credentials

The plugin sends authenticated REST requests to the Home Assistant address you
configure. Home Assistant can run locally; no vendor cloud account is required.
Network requests use timeouts and run outside OctoPrint's event and serial command
dispatch threads.

New configurations verify HTTPS certificates by default; existing preferences are
preserved on upgrade. Local HTTP addresses are also supported. The access token
stays server-side, is masked in settings and is not logged. Credentials require
Settings permission, light controls require Control permission, and state access
requires Status permission.

For configuration details, troubleshooting and release notes, see the
[project README](https://github.com/mark-bloom/OctoLight_Home-Assistant)
and [releases](https://github.com/mark-bloom/OctoLight_Home-Assistant/releases).

