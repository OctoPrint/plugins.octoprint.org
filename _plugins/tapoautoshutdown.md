---
layout: plugin

id: tapoautoshutdown
title: Tapo Auto Shutdown + Obico Delay
description: Automatically control a Tapo P110 smart plug and manage Obico AI monitoring around your prints.

#authors:
#- SpideRaY

license: MIT

date: 2026-09-12

homepage: https://github.com/SpideRaY/OctoPrint-TapoAutoShutdown-ObicoDelay
source: https://github.com/SpideRaY/OctoPrint-TapoAutoShutdown-ObicoDelay
archive: https://github.com/SpideRaY/OctoPrint-TapoAutoShutdown-ObicoDelay/archive/refs/tags/v0.2.0.zip

privacypolicy: https://github.com/SpideRaY/OctoPrint-TapoAutoShutdown-ObicoDelay/blob/main/PRIVACY.md

tags:
tapo
p110
smart plug
power
shutdown
obico
ai
automation
print monitoring

compatibility:
  python: ">=3.9,<3.14"

attributes:
cloud
ai-developed

---

Tapo Auto Shutdown automatically switches a Tapo P110 smart plug off after a completed print and can manage Obico AI monitoring during the print.

The plugin provides configurable delays for both Tapo shutdown and Obico AI monitoring. Obico AI monitoring is disabled when a print starts and can be automatically re-enabled after the configured delay if the print is still running.

If the print completes, is cancelled, or fails, the Obico monitoring timer is cancelled and AI monitoring is disabled.

The plugin requires an OctoPrint installation, a Tapo P110 smart plug, the tapo Python package, and the Obico OctoPrint plugin for Obico monitoring features.

The plugin does not modify the printer's operating system or install system services.

For more information, configuration details and source code, see the project repository.
