---
layout: plugin

id: pinozcam
title: OctoPrint-PiNozCam
description: AI-driven FREE monitoring for 3D print failures, running entirely on the printer's own board. Requires Linux on ARM32, ARM64 or x86_64.
author: DrAlexLiu
license: AGPLv3

date: 2024-03-06

homepage: https://github.com/DrAlexLiu/OctoPrint-PiNozCam
source: https://github.com/DrAlexLiu/OctoPrint-PiNozCam
archive: https://github.com/DrAlexLiu/OctoPrint-PiNozCam/archive/master.zip

follow_dependency_links: false

tags:
- ai
- failure detection
- machine learning
- computer vision
- ai on pi
- monitor
- telegram
- discord
- free
- no subscription
- secure
- privacy

screenshots:
- url: /assets/img/plugins/pinozcam/tab.jpg
  alt: PiNozCam tab in OctoPrint
  caption: Open PiNozCam from its OctoPrint tab
- url: /assets/img/plugins/pinozcam/screenshot.jpg
  alt: PiNozCam status panel in OctoPrint
  caption: PiNozCam status and failure-ratio display
- url: /assets/img/plugins/pinozcam/telegram_remote_control.jpg
  alt: Telegram remote printer monitor and control
  caption: Check, mute, pause, resume or stop the print from Telegram
- url: /assets/img/plugins/pinozcam/discord_notification.jpg
  alt: Discord remote printer monitor and control
  caption: The same buttons, in Discord

featuredimage: /assets/img/plugins/pinozcam/failure_detection1.jpg

compatibility:
  # List of compatible versions
  octoprint:
  - 1.4.0

  # List of compatible operating systems
  os:
  - linux
  - macos

  # Compatible Python version
  python: ">=3.7,<4"

# Developed with the use of Artificial Intelligence.
attributes:
- ai-developed
- cloud

# Detection is local, but the optional Telegram and Discord integrations
# upload camera images and print status to a third party, so the plugin
# declares where that is documented.
privacypolicy: https://github.com/DrAlexLiu/OctoPrint-PiNozCam/blob/master/docs/notifications.md#privacy-notes
---

# OctoPrint-PiNozCam

![failure_detection1](/assets/img/plugins/pinozcam/failure_detection1.jpg)

## Introduction

PiNozCam watches your OctoPrint camera, spots print failures, and alerts
you — or pauses or stops the print for you. Everything runs on your own
machine; camera frames never leave your network unless you deliberately
connect Telegram or Discord.

**Features:**

- **Detection entirely on-device** — no upload, no account, no
  subscription
- **Notify, pause or stop** when a failure is confirmed
- **Telegram and Discord alerts**, with buttons to check, mute, pause,
  resume or stop the print from your phone
- **Mask out anything permanently in frame** so bed clips and cables do
  not cause false alarms

> ⚠️ **Requires Linux on ARM32, ARM64 or x86_64** — a Raspberry Pi,
> similar SBC, or Intel/AMD Linux host (Apple Silicon Macs are also
> supported). The detector ships as a prebuilt native binary; there is
> no Windows or FreeBSD build, and on those platforms the plugin reports
> the backend as unavailable rather than detect anything.

## 📱 Your printer, in your pocket

Connect Telegram or Discord: AI failure alerts land on your phone, and
you can see the camera, pause, or stop the print right from the chat.
Don't wait for an alert — press **Check** whenever you're curious.

| Telegram | Discord |
|---|---|
| ![Telegram remote control](/assets/img/plugins/pinozcam/telegram_remote_control.jpg) | ![Discord remote control](/assets/img/plugins/pinozcam/discord_notification.jpg) |

- 🔍 **Check** — current camera view + printer status
- 🔇 **Mute / Unmute** — quiet alerts for this print
- ⏸️ **Pause / Resume** — step in from anywhere
- ⏹️ **Stop** — cancel with a confirmation tap
- 🚨 **Failure alert** — the analysed image, boxes included
- 🖨️ **Multiple printers** — one chat, all your printers

## ⚡ How fast is it?

| Device | Checks/min |
|---|---:|
| Raspberry Pi 5 | 221 |
| Raspberry Pi 4 / CM4 | 23 |
| Jetson Orin Nano Super | 335&dagger; |
| BIQU CB2 / Orange Pi 3B (RK3566 NPU) | 215 |
| LubanCat-4 (RK3588 NPU) | 625 |

These are full camera-to-result checks, the rate you actually get,
except &dagger;: the Jetson figure is the detection step alone. Even a
few checks a minute is plenty to catch a failing print — throughput is
rarely the constraint.

**Light on memory too:** OctoPrint + PiNozCam together stay under
**512 MB** — even a 512 MB Pi Zero 2 W / Pi CM0 works. A **1 GB
Raspberry Pi 5 (~US$45)** runs it comfortably.

## 🚀 First run — three decisions

1. **Camera** — PiNozCam checks the webcam OctoPrint already uses.
2. **Sensitivity** — pick a preset; you can refine it later.
3. **Action on Failure** — start with **Alert only**.

Stay on Alert only, start sensitive, and step down until false alerts
stop bothering you.

## 🖥️ OctoPrint interface

PiNozCam adds its own OctoPrint status tab and keeps all detector
controls together under **Settings → PiNozCam**.

![PiNozCam tab](/assets/img/plugins/pinozcam/tab.jpg)

![PiNozCam settings](/assets/img/plugins/pinozcam/screenshot.jpg)

## 🔒 Private by default

Frames, results, and settings stay on your OctoPrint machine. Nothing
leaves your network unless **you** connect Telegram or Discord — and
then only the analysed image and print status go out. Keep bot tokens
secret like passwords.
