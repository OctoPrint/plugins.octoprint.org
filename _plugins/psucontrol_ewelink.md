---
layout: plugin

id: psucontrol_ewelink
title: PSU Control - eWeLink
description: Control your 3D printer's power supply using eWeLink smart switches (Sonoff, etc.) through the PSU Control plugin.
authors:
- Christos Miniotis
license: MIT

date: 2026-01-07

homepage: https://github.com/chrismin13/OctoPrint-PSUControl-eWeLink
source: https://github.com/chrismin13/OctoPrint-PSUControl-eWeLink
archive: https://github.com/chrismin13/OctoPrint-PSUControl-eWeLink/archive/main.zip

# Privacy policy for cloud service usage
privacypolicy: https://github.com/chrismin13/OctoPrint-PSUControl-eWeLink/blob/main/PRIVACY.md

tags:
- psu
- psucontrol
- power
- switch
- sonoff
- ewelink
- smart home
- automation
- psucontrol subplugin

compatibility:
  octoprint:
  - 1.3.10
  
  os:
  - posix
  - windows
  
  python: ">=3.7,<4"

attributes:
- cloud

screenshots:
- url: /assets/img/plugins/psucontrol_ewelink/settings_screenshot.png
  alt: Settings Interface
  caption: Plugin settings allowing device selection and credential configuration

featuredimage: /assets/img/plugins/psucontrol_ewelink/settings_screenshot.png
---

Integrate [eWeLink](https://ewelink.cc/) smart switches (Sonoff, etc.) with [OctoPrint-PSUControl](https://github.com/kantlivelong/OctoPrint-PSUControl) to turn your 3D printer on and off remotely.

## Features

- **Cloud Integration**: Control any eWeLink-compatible device (Sonoff Basic, S26, etc.)
- **Device Discovery**: Test connection and browse devices directly in OctoPrint settings
- **State Sensing**: Real-time feedback on switch state
- **Secure Credentials**: Passwords are encrypted locally using XOR obfuscation

## Requirements

- OctoPrint 1.3.10 or higher
- [OctoPrint-PSUControl](https://github.com/kantlivelong/OctoPrint-PSUControl) plugin installed
- eWeLink account and compatible smart switch
- Active internet connection

## External Services

This plugin connects to the **eWeLink Cloud API** to control your smart devices. An active internet connection is required for all functionality. Your eWeLink credentials are transmitted securely over HTTPS to eWeLink's servers.

The plugin does **not** collect or transmit any data to third parties other than eWeLink.

## Setup

1. Install via Plugin Manager
2. Navigate to **Settings** → **PSU Control - eWeLink**
3. Enter your eWeLink email and password
4. Click **Test Connection / Get Devices**
5. Select your device from the dropdown
6. Save settings
7. Go to **PSU Control** settings and select this plugin for switching/sensing

## Troubleshooting

- **Authentication Failed**: Double-check your eWeLink email and password
- **Device Not Found**: Ensure the device is "Online" in the eWeLink app
- **Connection Issues**: Check your internet connection; the eWeLink cloud must be reachable
