---
layout: plugin

id: alexaoctoprint
title: Alexa OctoPrint
description: Control selected OctoPrint and 3D printer actions through Alexa on the local network without an external backend.
authors:
- RICLAMER
license: AGPL-3.0-or-later

date: 2026-07-17

homepage: https://github.com/RICLAMER/AlexaOctoPrint
source: https://github.com/RICLAMER/AlexaOctoPrint
archive: https://github.com/RICLAMER/AlexaOctoPrint/archive/0.2.0.zip

tags:
- alexa
- automation
- control
- raspberrypi

compatibility:
  octoprint:
  - ">=1.6.0"
  os:
  - linux
  python: ">=3.7,<4"

attributes:
- ai-developed

---

Alexa OctoPrint simulates local smart devices for enabled printer actions. No
external integration account, Alexa skill, cloud backend, telemetry service, or
relay is required.

Actions include pause, resume, guarded cancellation, homing, leveling, Z and
extruder movement, configurable bed and nozzle temperatures, motors, selected
files, emergency stop, and optional OctoPrint-Enclosure power and light outputs.
Portuguese, English, and Spanish device names are included.

Local discovery requires restricted root routes on TCP port 80. Existing
HAProxy or another reverse proxy can provide them. The repository includes an
explicit Easy Setup that inspects the current listener, preserves unrelated
routes, validates HAProxy before restart, and saves rollback state. The plugin
does not silently modify system services.

Each installation generates its own local 40-character username. Proxy ACLs
match only the description, username creation, and corresponding light paths;
normal OctoPrint API routes are excluded.

Updates use OctoPrint's `github_release` check and install the archive for the
matching GitHub release tag.
