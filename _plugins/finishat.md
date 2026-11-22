---
layout: plugin

id: finishat
title: Finish At
description: Schedule a print by choosing the time it should finish. Powers the printer on through PSU Control.
authors:
- Ale6699
license: AGPLv3

date: 2026-11-22

homepage: https://github.com/Ale6699/OctoPrint-FinishAt
source: https://github.com/Ale6699/OctoPrint-FinishAt
archive: https://github.com/Ale6699/OctoPrint-FinishAt/archive/main.zip

tags:
- schedule
- scheduling
- timer
- delayed start
- psu control
- telegram

screenshots:
- url: /assets/img/plugins/finishat/tab.png
  alt: The Finish At tab
  caption: Pick a file and the finish time; the start time is worked out for you

featuredimage: /assets/img/plugins/finishat/tab.png

compatibility:
  octoprint:
  - 1.11.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=3,<4"

attributes:
- ai-developed

---

Finish At starts a print **so that it finishes at the time you choose**.

Pick a file, type the finish time (for example 16:00), and the plugin works out when to start from the
slicer's estimate in the G-code, plus a safety margin and the heat-up time. At start time it powers the
printer on through [PSU Control](https://plugins.octoprint.org/plugins/psucontrol/) if installed, waits
for it to connect and starts the print.

Safety first: you must confirm that the bed is clear before scheduling, and the print does not start if
the printer is busy, does not connect, or OctoPrint missed the start time.

Optional notifications through the [Telegram plugin](https://plugins.octoprint.org/plugins/telegram/).

Available in English and Italian.
