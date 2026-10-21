---
layout: plugin

id: ha_light_control
title: Home Assistant Light Control
description: Control Home Assistant lights and switches from OctoPrint, with brightness, colour, print status lighting and delayed shutoff.
authors:
- idontwantfame
license: AGPL-3.0-or-later
date: 2026-10-21

homepage: https://github.com/idontwantfame/OctoLight_Home-Assistant
source: https://github.com/idontwantfame/OctoLight_Home-Assistant
# Update this URL when publishing a new release; install released code, not master.
archive: https://github.com/idontwantfame/OctoLight_Home-Assistant/archive/refs/tags/v0.3.0.zip

tags:
- home assistant
- lights
- switch
- automation
- gcode

compatibility:
  octoprint:
  - ">=1.11.8,<3"
  os:
  - linux
  python: ">=3.9,<4"

attributes:
- ai-developed

screenshots:
- url: /assets/img/plugins/ha_light_control/controls.png
  alt: OctoPrint navbar with a Home Assistant light's brightness slider open
  caption: Adjust a supported light's brightness directly from the OctoPrint navbar.
- url: /assets/img/plugins/ha_light_control/settings.png
  alt: Home Assistant Light Control connection and entity settings
  caption: Configure the Home Assistant connection, search entities and test access before saving.
- url: /assets/img/plugins/ha_light_control/automation.png
  alt: Print automation, brightness defaults, status colours and error flash settings
  caption: Configure host commands, print automation, turn-on appearance and optional status colours.

featuredimage: /assets/img/plugins/ha_light_control/controls.png
---

Control your printer enclosure lighting and other Home Assistant lights or switches
from OctoPrint. Search for entities in settings, toggle them from the navbar, and
adjust brightness or RGB colour on supported lights. Optional automation follows
print events and switches lights off after a configurable delay.

This is a maintained fork of [OctoLight Home Assistant](https://plugins.octoprint.org/plugins/octolightHA/),
originally based on OctoLight. It installs as a separate plugin named **Home Assistant
Light Control**, with its own settings and update source.

## Features

- Search Home Assistant by friendly name or entity ID, with automatic selection
  when exactly one supported entity exists and the entity field is empty.
- Test connection settings and entity access before saving, without operating a light.
- Control multiple entities independently, with individual navbar icons, automation
  settings and shutoff timers.
- Adjust brightness and RGB colour from navbar menus, or configure turn-on defaults.
- Refresh reported state from Home Assistant, including changes made in other apps.
  Unavailable entities are distinguished from lights that are off.
- Optionally apply configurable colours for printing, pause, completion, cancellation
  and errors, plus a native short error flash on supported lights.
- Turn lights on at print start and off after completion, failure or cancellation.
  New prints and manual controls cancel pending completion shutoff timers.
- Control configured entities using opt-in `@HALIGHT` host commands or an
  authenticated HTTP API.

Brightness, RGB colour and native flashes depend on the capabilities reported by
each light. `switch` and `input_boolean` entities provide on/off control.

## Requirements and setup

Requires Python 3.9 or later, OctoPrint 1.11.8 or later within the declared range,
and a Home Assistant instance reachable from the OctoPrint host. Create a Home
Assistant long-lived access token with access to the entities you want to control.

1. Install the plugin and restart OctoPrint.
2. Open **Settings → Home Assistant Light Control**.
3. Enter your Home Assistant URL and long-lived access token.
4. Select **Search Home Assistant**, then choose a light, switch or input boolean.
5. Select **Test connection and entity**, save, and configure optional automation.

Validated on Linux with OctoPrint **1.11.8 / Python 3.9 and 3.10**, and
**2.0.0rc7 / Python 3.12**. OctoPrint 2 testing covers this release candidate;
later releases require verification. Automated validation includes a local OctoPrint
server, Chromium and a simulated Home Assistant. Physical printers and Home
Assistant devices, Windows and macOS have not been verified.

## G-code and API

Enable **@HALIGHT host commands** in settings to use commands from OctoPrint's
Terminal, G-code scripts, streamed G-code files or OctoDash actions:

```gcode
@HALIGHT on
@HALIGHT set brightness=75 color=#ff8000
@HALIGHT set light.printer color=#ff0000 flash=short
@HALIGHT off
```

Commands run asynchronously and target configured entities only. Printing directly
from a printer's SD card does not process these host commands.

The API is `/api/plugin/ha_light_control`. GET reads cached state; authenticated
JSON POST requests operate lights. See the
[README](https://github.com/idontwantfame/OctoLight_Home-Assistant#http-api)
for commands and permission requirements.

## Migrating from OctoLight Home Assistant

The original plugin is not replaced or uninstalled. Disable **OctoLight Home
Assistant**, restart OctoPrint, then select **Import OctoLight settings** in this
plugin's settings before entering a new configuration. Import copies known settings
and leaves the original configuration intact. It refuses to overwrite a configured
destination or run while the original plugin is enabled.

Update scripts from `@OCTOLIGHT` to `@HALIGHT` and API integrations from
`/api/plugin/octolightHA` to `/api/plugin/ha_light_control`. Light controls require
POST requests; legacy GET mutation calls are not supported. Avoid enabling both
plugins' automation for the same entity.

## Connections and credentials

The plugin sends authenticated REST requests to the Home Assistant address you
configure. No vendor cloud account is required; Home Assistant can run on your
local network. Polling and controls use bounded requests outside OctoPrint's event
and serial dispatch threads so connection failures do not block those threads.

New configurations verify HTTPS certificates by default. Local HTTP addresses
and explicitly disabling HTTPS certificate verification are also supported.
Use HTTPS with a trusted certificate for connections outside your trusted network.
The Home Assistant token stays server-side, is masked in settings and is not logged
by the plugin. Access to credentials requires OctoPrint's Settings permission;
light controls require Control permission and state access requires Status permission.

For configuration details, troubleshooting and release notes, see the
[project README](https://github.com/idontwantfame/OctoLight_Home-Assistant)
and [releases](https://github.com/idontwantfame/OctoLight_Home-Assistant/releases).
