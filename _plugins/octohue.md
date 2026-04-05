---
layout: plugin

id: octohue
title: OctoHue
description: Illuminate your 3D printer and signal its status using Philips Hue lights. Supports event-driven colour changes, CT mode for white-spectrum bulbs, night mode, smart plug auto power-off, and guided in-settings bridge pairing.
authors:
- Simon Beckett
license: AGPLv3

date: 2020-01-31

homepage: https://github.com/entrippy/OctoPrint-OctoHue
source: https://github.com/entrippy/OctoPrint-OctoHue
archive: https://github.com/entrippy/OctoPrint-OctoHue/archive/master.zip

follow_dependency_links: false

tags:
- Philips Hue
- Hue
- Lights
- Status
- Automation
- Smart Plug
- Power Control
- Night Mode

screenshots:
- url: /assets/img/plugins/octohue/Settings-octohue-general.png
  alt: OctoHue event lighting settings
  caption: Event lighting table — map any OctoPrint event to a colour, brightness, delay, flash, or turn-off action
- url: /assets/img/plugins/octohue/Settings-octohue-bridge-pair.png
  alt: OctoHue bridge pairing screen
  caption: Guided bridge pairing — discover and pair your Hue bridge without leaving OctoPrint settings
- url: /assets/img/plugins/octohue/Settings-octohue-pair-success.png
  alt: OctoHue bridge paired successfully
  caption: After pairing, a single button takes you straight to the Lights tab
- url: /assets/img/plugins/octohue/Settings-octohue-lights.png
  alt: OctoHue light and group selection
  caption: Combined light and group dropdown — individual bulbs and Hue rooms/zones in one list

featuredimage: /assets/img/plugins/octohue/Featured-Image.png

compatibility:
  octoprint:
  - 1.8.0

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=3.9"

---

# OctoPrint-OctoHue

Illuminate your 3D print job and signal its status using Philips Hue lights — and optionally cut power to your printer automatically once it cools down.

## Features

- **Event-driven lighting** — map any OctoPrint event (Connected, PrintStarted, PrintDone, PrintFailed, etc.) to a specific colour or colour temperature, brightness, optional delay, flash alert, and on/off state
- **CT mode** — switch any event to colour-temperature mode for RGBCCT lights, activating the white channel instead of the RGB LEDs
- **Configurable toggle colour** — the navbar toggle button turns your light on with a dedicated colour, CT value, and brightness you configure
- **Night mode** — define a time window during which light changes are paused entirely, or brightness is capped at a configurable maximum
- **Smart plug control** — configure a Hue smart plug to cut printer power after a completed print
- **Auto power-off** — automatically switch off the plug once all extruders cool below a configurable temperature threshold
- **Guided bridge pairing** — find your Hue bridge on the network and pair it without leaving OctoPrint settings; after pairing, a single button takes you straight to the Lights tab
- **Navbar toggle** — optional toolbar button to toggle your lights on/off at any time
- **Group support** — target individual lights or Hue rooms/zones from a single combined dropdown
- **Configurable delay** — add a delay (in seconds) before each event triggers its light change
- **API** — `getstate`, `turnon`, `turnoff`, `togglehue`, `getdevices`, `getgroups`, and `cooldown` commands for third-party integrations

## Setup

### 1. Bridge pairing

Open OctoPrint **Settings → OctoHue → Bridge**.

- Click **Find My Bridge** to locate your Hue bridge automatically on your local network.
- Once found, press the **physical button on top of your Hue bridge**, then click **Start Pairing** within 30 seconds.
- After a successful pairing, click **Select your light →** to jump straight to the Lights tab with your devices already populated.

> If auto-discovery does not work (e.g. the bridge is on a different subnet), you can enter the bridge IP address and API key manually after pairing via the [Hue Getting Started guide](https://developers.meethue.com/develop/get-started-2/).

### 2. Light or group selection

On the **Lights** tab, select your light or group from the dropdown. Individual lights and Hue rooms/zones appear in the same list — groups are labelled **(Group)**. Set **Default Brightness** (1–100%) to control brightness when an event does not specify its own.

### 3. Event configuration

Still on the **Lights** tab, expand **Event Lighting Options** to configure which OctoPrint events trigger a light change. For each event you can set colour (RGB or CT), brightness (1–100%), delay, flash, and turn-off behaviour.

### 4. Power control (optional)

Open the **Power** tab to select a Hue smart plug and configure auto power-off after prints complete.

## API

OctoHue exposes a [SimpleAPI](https://docs.octoprint.org/en/master/plugins/mixins.html#octoprint.plugin.SimpleApiPlugin) for third-party integrations. Light-control commands (`turnon`, `turnoff`, `togglehue`, `cooldown`) are accessible without authentication; device and bridge commands require OctoPrint admin access.
