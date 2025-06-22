---
layout: plugin

id: prusa_connect_uploader
title: Prusa Connect Uploader
description: Uploads webcam snapshots from OctoPrint to Prusa Connect for enhanced remote monitoring.
authors:
- Rizz
license: MIT

date: 2025-05-01

homepage: https://github.com/rizz360/prusa_connect_uploader
source: https://github.com/rizz360/prusa_connect_uploader
archive: https://github.com/rizz360/prusa_connect_uploader/archive/refs/heads/main.zip

tags:
- prusa
- monitoring
- camera
- snapshot
- remote access

#screenshots:
#- url: /assets/img/plugins/prusa_connect_uploader/docs/config-panel.png
#  alt: "Plugin settings view"
#  caption: "Configure your token and upload interval from the settings tab."

#featuredimage: /assets/img/plugins/prusa_connect_uploader/example.png

compatibility:
  octoprint:
  - 1.10.3

  os:
  - linux
  - windows
  - macos

  python: ">=3,<4"

attributes:
  - cloud
---

Prusa Connect Uploader is an OctoPrint plugin that captures webcam snapshots and uploads them to [Prusa Connect](https://connect.prusa3d.com) for remote viewing and monitoring.

Easily configure your upload token and snapshot frequency from the plugin settings. Once set up, snapshots will be pushed automatically during printing, improving your visibility while away from the printer.

See the [README](https://github.com/rizz360/prusa_connect_uploader#readme) for detailed setup instructions.
