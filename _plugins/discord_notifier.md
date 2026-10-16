---
layout: plugin

id: discord_notifier
title: OctoPrint-DiscordNotifier
description: Sends print notifications directly to a Discord channel via webhook, with an optional webcam snapshot.
authors:
- Marcin Sadowski
license: AGPLv3

date: 2026-10-16

homepage: https://github.com/devouted/OctoPrint-DiscordNotifier
source: https://github.com/devouted/OctoPrint-DiscordNotifier
archive: https://github.com/devouted/OctoPrint-DiscordNotifier/archive/1.0.0.zip

tags:
- notifications
- discord
- webhook
- webcam
- events

screenshots:
- url: /assets/img/plugins/discord_notifier/settings.png
  alt: Discord Notifier settings panel
  caption: Settings panel — webhook URL, event checkboxes, snapshot and notification limit
- url: /assets/img/plugins/discord_notifier/notifications.png
  alt: Example notification on Discord
  caption: Example print notification on Discord with a webcam snapshot

featuredimage: /assets/img/plugins/discord_notifier/notifications.png

compatibility:
  octoprint:
  - 1.9.0

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=3.7,<4"

attributes:
- ai-developed

---

Send OctoPrint print notifications straight to a Discord channel using a Discord
**webhook** — no intermediate relay script or bot required.

## Features

- Configure the Discord **webhook URL** right in the plugin settings.
- Choose which events trigger a notification via **checkboxes**:
  - Print started / Print done / Print failed
  - Paused / Resumed / Cancelled
  - Printer connected / Printer disconnected
- **Webcam snapshot**: notifications (and the test button) can attach an image
  from the webcam configured in OctoPrint. The image is uploaded directly as an
  attachment — no external image hosting needed.
- **Notification limit (throttle)**: a configurable interval (default 10 s)
  prevents a burst of identical notifications, e.g. if the printer's serial
  port flaps. Set it to `0` to disable.
- **Send test** button to verify your configuration at any time (it sends a
  sample notification together with a webcam image if one is configured).
- Rich embeds with a per-event color, a progress bar, timestamps and the serial
  port/baudrate for connection events.

## Configuration

1. In Discord, open your channel settings → *Integrations → Webhooks → Copy
   Webhook URL*.
2. In OctoPrint, go to *Settings → Discord Notifier* and paste the URL into the
   **Webhook URL** field.
3. Tick the events you want to be notified about, optionally set a **username**
   and the **notification limit**, then save.
4. (Optional) Make sure a webcam snapshot URL is configured in *Settings →
   Webcam & Timelapse* and enable **Attach webcam image** to include a snapshot.
5. Click **Send test** to confirm everything works.

## Privacy and external services

This plugin only communicates with the Discord webhook URL that **you**
configure; it does not contact any other third-party service and includes no
tracking. If Discord is unreachable (e.g. the OctoPrint instance is offline),
the plugin fails gracefully and does not disrupt OctoPrint.

## AI-assisted development

This plugin was built with the help of **AI — Kiro (kiro-dev)** and is marked
with the `ai-developed` attribute accordingly. The author remains responsible
for maintenance, bug fixes and compatibility with future OctoPrint versions.
