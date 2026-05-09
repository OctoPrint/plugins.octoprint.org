---
layout: plugin

id: lazarus
title: Lazarus
description: Resume failed 3D prints when the partial print is still attached to the bed.
authors:
- Kenneth B Smith
license: Proprietary - See LICENSE.txt

date: 2026-05-09

homepage: https://app.lazarus3dprint.com
source: https://github.com/ksmith1489/lazarus-plugin
archive: https://github.com/ksmith1489/lazarus-plugin/archive/refs/heads/main.zip

privacypolicy: https://app.lazarus3dprint.com/privacy

tags:
- printing
- recovery
- gcode
- klipper
- moonraker
- marlin

compatibility:
  python: ">=3.7,<4"

attributes:
- cloud
- commercial
---

Lazarus helps recover failed 3D prints when the partial print is still attached to the bed.

The plugin generates the resume G-code locally inside OctoPrint from the original G-code file, the measured print height, and the detected layer structure of that file. The original G-code is not uploaded to the Lazarus service for processing.

Lazarus includes a guided recovery workflow:

- select the original G-code from OctoPrint storage or your local device;
- enter the measured height of the saved print;
- generate a new resume file and a calculated alignment point;
- establish a safe starting coordinate state;
- align the nozzle to the saved print using OctoPrint motion controls;
- download or execute the generated resume sequence.

Printer movement remains user-controlled. Lazarus does not automatically home Z into an existing print.

Optional Moonraker/Klipper support is included through a user-provided local Moonraker address.

Lazarus uses `https://app.lazarus3dprint.com` for activation and subscription validation. If that service is unavailable, Lazarus fails closed for resume generation and execution without causing OctoPrint itself to malfunction.

Lazarus is commercial software and requires an active subscription for resume generation and execution. Pricing, activation, terms, license information, and privacy information are available here:

- https://app.lazarus3dprint.com/activate
- https://app.lazarus3dprint.com/license
- https://app.lazarus3dprint.com/terms
- https://app.lazarus3dprint.com/privacy
