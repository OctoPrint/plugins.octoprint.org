---
layout: plugin

id: tapoautoshutdown
title: Tapo Auto Shutdown + Obico Delay
description: Automatically control a Tapo P110 smart plug and manage Obico AI monitoring around your prints.

authors:
- SpideRaY

license: MIT

date: 2026-10-02

homepage: https://github.com/SpideRaY/OctoPrint-TapoAutoShutdown-ObicoDelay
source: https://github.com/SpideRaY/OctoPrint-TapoAutoShutdown-ObicoDelay
archive: https://github.com/SpideRaY/OctoPrint-TapoAutoShutdown-ObicoDelay/archive/main.zip

privacypolicy: https://github.com/SpideRaY/OctoPrint-TapoAutoShutdown-ObicoDelay/blob/main/PRIVACY.md

tags:
- tapo
- p110
- smart plug
- power
- shutdown
- obico
- ai
- automation
- print monitoring

compatibility:
  python: ">=3.11,<4"

attributes:
  - cloud
  - ai-developed

---

Tapo Auto Shutdown

Automatically control a Tapo P110 smart plug after a completed print and manage Obico AI monitoring during your prints.

Tapo Auto Shutdown switches off the printer’s Tapo smart plug when a print has finished. It can also delay shutdown to allow timelapse rendering to complete before power is removed.

Obico AI monitoring is disabled when a print starts. It can be automatically re-enabled after the configured Obico delay if the print is still running.

If the print completes, is cancelled, or fails, the Obico monitoring timer is cancelled and AI monitoring remains disabled.

The plugin supports optional Tapo plug control and Obico monitoring management, allowing you to configure the features you need for your printing setup.
