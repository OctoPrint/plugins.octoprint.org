---
layout: plugin

id: octogoat
title: OctoGoat
description: Safely resume failed 3D prints with guided alignment, local resume G-code generation, and Klipper/Moonraker support.
author: ksmith1489
license: Proprietary https://app.lazarus3dprint.com/license

date: 2026-05-05

homepage: https://app.lazarus3dprint.com
source: https://github.com/ksmith1489/octogoat-plugin
archive: https://github.com/ksmith1489/octogoat-plugin/archive/main.zip

privacypolicy: https://app.lazarus3dprint.com/privacy

tags:
- recovery
- resume
- gcode
- klipper
- moonraker
- failed print
- utility

attributes:
- cloud
- commercial

compatibility:
  octoprint:
  - 1.8.0

  os:
  - linux
  - windows
  - macos

  python: ">=3.7,<4"

---

OctoGoat helps recover failed 3D prints by generating safe resume G-code and guiding the user through alignment before restarting the print.

If a print fails but the part is still attached to the bed, OctoGoat helps the user:

- choose the original G-code file,
- enter the measured print height,
- calculate a safe resume point,
- preview the reconstructed resume G-code,
- align the printer to the real-world print position,
- and resume the print with user confirmation.

OctoGoat is designed around user-controlled recovery. It does not force automatic Z homing into an existing print. The user remains in control of the alignment and final resume step.

## Features

- Generates reconstructed resume G-code locally inside the OctoPrint plugin.
- Uses measured print height and layer height to calculate the resume layer.
- Removes unsafe startup, homing, leveling, and end-print commands from the resumed file.
- Provides guided alignment controls inside the OctoPrint UI.
- Supports standard OctoPrint printer communication.
- Supports Klipper/Moonraker setups through a user-provided local Moonraker address.
- Includes license validation through the OctoGoat/Lazarus service.

## External services

OctoGoat uses the OctoGoat/Lazarus service at `https://app.lazarus3dprint.com` for subscription and license validation.

Resume G-code generation runs locally in the plugin. The original G-code file is not uploaded to the OctoGoat/Lazarus service for resume generation.

If the license validation service is unavailable, OctoGoat is designed to fail gracefully without breaking OctoPrint.

## Commercial use

OctoGoat is a commercial plugin with subscription-based licensing. Installing the plugin is free, but an active paid subscription is required before the plugin can generate, download, upload, or execute resume output. License, terms, privacy, and pricing information are available from the OctoGoat/Lazarus website.

## Klipper/Moonraker support

For Klipper users, OctoGoat can send alignment and positioning commands through Moonraker when the user provides their local Moonraker printer address.

## Safety note

OctoGoat is intended to help users recover failed prints while keeping the user in control of printer motion and resume confirmation. Users should verify printer position, print condition, and nozzle clearance before resuming any failed print.
