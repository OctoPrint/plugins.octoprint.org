---
layout: plugin

id: chamberlight
title: Prusa Chamber Light
description: Turn the Prusa CORE One chamber light on and off from OctoPrint, with optional brightness control through Prusa Connect.
authors:
- Aryeh95
license: AGPLv3

date: 2026-10-06

homepage: https://github.com/Aryeh95/OctoPrint-PrusaChamberLight
source: https://github.com/Aryeh95/OctoPrint-PrusaChamberLight
archive: https://github.com/Aryeh95/OctoPrint-PrusaChamberLight/archive/main.zip

# Only the optional brightness feature talks to a cloud service (Prusa Connect)
privacypolicy: https://github.com/Aryeh95/OctoPrint-PrusaChamberLight/blob/main/PRIVACY.md

tags:
- prusa
- core one
- light
- led
- chamber
- enclosure
- prusa connect

screenshots:
- url: /assets/img/plugins/chamberlight/sidebar.png
  alt: Chamber Light sidebar panel
  caption: On/off button and brightness slider in the sidebar
- url: /assets/img/plugins/chamberlight/settings.png
  alt: Chamber Light settings
  caption: Optional Prusa Connect setup for brightness control

featuredimage: /assets/img/plugins/chamberlight/sidebar.png

compatibility:
  octoprint:
  - 1.10.0

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=3.9,<4"

attributes:
- cloud  # only the optional brightness feature, which goes through Prusa Connect
- ai-developed

---

Turn the chamber light of a **Prusa CORE One** on and off from OctoPrint, and optionally set its brightness.

- A lightbulb button in the navbar and a **Chamber Light** panel in the sidebar.
- On/off is sent to the printer over USB using `M151`, based on how the Buddy firmware handles its chamber LED strip.
  No account or internet access is needed.
- If the printer is power cycled while the light is off, the plugin turns it off again when OctoPrint reconnects.
- Optional and experimental: brightness (0–100 %) through Prusa Connect, the same way the Prusa app sets it. The
  firmware has no G-code for brightness. This uses Prusa Connect's unofficial web API and a login token from your
  Prusa account, so it needs internet access and may stop working if Prusa changes the API.

Tested with a CORE One on firmware 7.0.0, on OctoPrint 1.11.8 and 2.0.0rc5. Not affiliated with Prusa Research.

See the [README](https://github.com/Aryeh95/OctoPrint-PrusaChamberLight#readme) for setup and details.
