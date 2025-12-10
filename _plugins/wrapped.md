---
layout: plugin

id: wrapped
title: OctoPrint Wrapped!
description: Get your yearly stats and let it snow!
authors:
  - Gina Häußge
license: AGPL-3.0-or-later

date: 2025-12-10

homepage: https://github.com/OctoPrint/OctoPrint-Wrapped
source: https://github.com/OctoPrint/OctoPrint-Wrapped
archive: https://github.com/OctoPrint/OctoPrint-Wrapped/archive/main.zip

tags:
  - stats
  - achievements
  - wrapped
  - fun
  - seasonal
  - snow

screenshots:
  - url: /assets/img/plugins/wrapped/wrapped.png
    alt: "Example #OctoPrintWrapped picture"
    caption: "Get your yearly OctoPrint stats!"
  - url: /assets/img/plugins/wrapped/snowfall.gif
    alt: "Demo GIF of active snowfall on the OctoPrint UI"
    caption: "Let it snow!"

featuredimage: /assets/img/plugins/wrapped/wrapped.png

compatibility:
  octoprint:
    - 1.11.0
  python: ">=3.9,<4"

attributes:
#  - cloud  # if your plugin requires access to a cloud to function
#  - commercial  # if your plugin has a commercial aspect to it
#  - free-tier  # if your plugin has a free tier
---

Get your yearly OctoPrint stats as a shareable **#OctoPrintWrapped** picture - and let it snow!

The Wrapped picture depends on the Achievements plugin being enabled (as it takes care of
the stats collection during the year) and can be opened via the little gift package icon 🎁
in the navbar.

The snow effect can always be toggled during the season using the little snowflake icon ❄️
in the navbar, and its setting persists through the browser's local storage.

Both Wrapped and snowfall are only available from December 1st until January 10th.

**If you post your Wrapped on social media, please use the hashtag `#OctoPrintWrapped`! 😊**
