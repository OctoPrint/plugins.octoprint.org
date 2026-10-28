---
layout: plugin

id: pangolin_newt
title: Pangolin Newt Client
description: Reach OctoPrint from anywhere through Pangolin. Installs, verifies and runs the Newt tunnel client for you.
authors:
- Gulianrdgd
license: AGPLv3

date: 2026-10-28

homepage: https://github.com/Gulianrdgd/OctoPrint-PangolinNewt
source: https://github.com/Gulianrdgd/OctoPrint-PangolinNewt
archive: https://github.com/Gulianrdgd/OctoPrint-PangolinNewt/archive/main.zip

tags:
- remote access
- tunnel
- pangolin
- wireguard

screenshots:
- url: /assets/img/plugins/pangolin_newt/sidebar.png
  alt: Sidebar showing the tunnel status, controls and Newt log
  caption: Sidebar
- url: /assets/img/plugins/pangolin_newt/settings.png
  alt: Settings page with status, version and connection fields
  caption: Settings

featuredimage: /assets/img/plugins/pangolin_newt/sidebar.png

compatibility:
  octoprint:
  - 1.11.0
  os:
  - linux
  python: ">=3.7,<4"

attributes:
- ai-developed

---

Makes your OctoPrint reachable through [Pangolin](https://pangolin.net) without opening ports and without a terminal.

Enter your Pangolin endpoint, Newt ID and Newt secret in the settings and save. The plugin downloads the matching
[Newt](https://github.com/fosrl/newt) build for your Pi, verifies its sha256 checksum and keeps it running alongside
OctoPrint. The sidebar shows whether the tunnel is connected, along with Start, Stop and Restart buttons and Newt's live log.

New Newt releases are shipped as plugin updates through OctoPrint's Software Update.

## Requirements

- A [Pangolin](https://pangolin.net) server: Pangolin Cloud or your own self-hosted instance, reachable over https.
- A site of type Newt created in the Pangolin dashboard, which gives you the Newt ID and secret.
- Linux on arm64, 32-bit ARM (armv7 / armv6) or x86_64. Tested on OctoPi 1.1 with OctoPrint 1.11.

## What the plugin does on your system

- Downloads the official Newt binary from [Newt's GitHub releases](https://github.com/fosrl/newt/releases) into
  OctoPrint's plugin data folder and verifies its sha256 against the checksum pinned in the plugin release.
  It installs nothing system-wide and does not need root or sudo.
- Runs Newt as a child process of OctoPrint while the tunnel is enabled, and stops it when OctoPrint shuts down.
- Newt connects to the Pangolin endpoint you configure, over https only.
- No tracking or analytics. The Newt secret stays in OctoPrint's config.yaml and is never sent back to the browser.
