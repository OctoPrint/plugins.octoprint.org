---
layout: plugin

id: eeprom_marlin
title: Marlin EEPROM Editor
description: Makes it possible to change the EEPROM values of Marlin Firmware through OctoPrint
authors:
- Charlie Powell
- Anderson Silva
license: AGPLv3

date: 2015-08-30

homepage: https://github.com/cp2004/OctoPrint-EEPROM-Marlin
source: https://github.com/cp2004/OctoPrint-EEPROM-Marlin
archive: https://github.com/cp2004/OctoPrint-EEPROM-Marlin/releases/latest/download/release.zip

follow_dependency_links: false

tags:
- marlin
- eeprom
- editor
- eeprom editor
- eeprom config
- helper

featuredimage: /assets/img/plugins/eeprom_marlin/firmware_info.png

compatibility:
  python: ">=2.7,<4"
  octoprint: 1.4.0

---

*Originally by [Anderson Silva](https://github.com/amsbr) until 2018 development taken over by [Charlie Powell](https://github.com/cp2004) in October 2020.*

The Marlin EEPROM editor provides an easy to use, feature-rich UI to edit your machine's configuration.

## Features

- Load & parse the EEPROM data out of the firmware
- Edit many of the values configured
- Save EEPROM changes on the printer with a minimal number of commands
- Storage of data on the OctoPrint server, so it can be viewed while printer is disconnected or printing.
- Backup feature:
  - Enabled saving configuration snapshots, restoring, downloading, uploading

- Display firmware info, including capability report

Be sure to [check out the screenshots](#Screenshots) below for more details!

## Setup

Find it in the plugin manager or install manually using this URL:

    https://github.com/cp2004/OctoPrint-EEPROM-Marlin/releases/latest/download/release.zip

## Firmware requirements

This plugin requires that you have **both** these items in Marlin's `Configuration.h` file:

- `#define EEPROM_CHITCHAT`
- `//#define DISABLE_M503`

In other words, `EEPROM_CHITCHAT` and the M503 command must be enabled - comment out disabling it.

## New in Marlin EEPROM Editor V3.0.0

A complete re-write of this plugin, now V3!

Featuring:

- Python processing & storage, eliminating performance issues in the UI.
- Storage of data on the OctoPrint server, so it can be viewed while the printer is disconnected or printing.
- Brand new UI, written from the ground up.
- Includes new read-only mode, when the printer is printing
- All-new backup feature, allowing naming and storing of backups, so you can quickly swap between profiles and more.
- ... and more!

**For the full changelist please check out the [release notes](https://github.com/cp2004/OctoPrint-EEPROM-Marlin/releases/tag/3.0.0).**

## Screenhots

Firmware info overview
![Firmware Info](/assets/img/plugins/eeprom_marlin/firmware_info.png)

Configuration editor
![Configuration Editor](/assets/img/plugins/eeprom_marlin/config.png)

Backup feature
![Backup feature](/assets/img/plugins/eeprom_marlin/backup.png)


## Enjoying the plugin? Sponsor its development!
I am working on this plugin in my spare time, if you appreciate the work I have put in
please consider [sponsoring its development on GitHub.](https://github.com/sponsors/cp2004)

## Need help? Get in touch!
Whilst I don't like bugs, I want to know where they are!
* Get in touch on the [Github Repository](https://github.com/cp2004/OctoPrint-EEPROM-Marlin)
* Ask a question on the [community forums](https://community.octoprint.org)
* Find help on the [OctoPrint Discord Server](https://discord.octoprint.org)

## My other plugins
Check out some more of my plugins [in the repository here](https://plugins.octoprint.org/by_author/#charlie-powell)
