---
layout: plugin

id: bedcooldown
title: OctoPrint-BedCooldown
description: Turns off the bed heater toward the end of a print
authors:
- Ryan Finnie
license: MPL-2.0

date: 2021-09-26

homepage: https://github.com/rfinnie/OctoPrint-BedCooldown
source: https://github.com/rfinnie/OctoPrint-BedCooldown
archive: https://github.com/rfinnie/OctoPrint-BedCooldown/archive/main.zip

follow_dependency_links: false

tags:
- heated bed
- bed temperature
- cooldown

screenshots:
- url: /assets/img/plugins/bedcooldown/settings.png
  alt: A screen capture of the Bed Cooldown settings page within OctoPrint, showing basic usage and the options "Enabled", "Print time left threshold" and "Print completion threshold"
  caption: Bed Cooldown settings
- url: /assets/img/plugins/bedcooldown/graph.png
  alt: A screen capture of the main OctoPrint progress graph, showing the bed starting to cool down 5 minutes before the end of the print
  caption: Example progress graph showing Bed Cooldown in action

featuredimage: /assets/img/plugins/bedcooldown/graph.png

compatibility:
  python: ">=3,<4"

---

For filaments such as PLA, many printers have more than enough stored thermal mass in the bed to keep bed adhesion throughout the print.
Therefore, you may want to turn off the bed heater automatically before the end of a print, saving cooldown time.

The bed heater will be turned off during a print, when both conditions are met:

  * The print time left is below the configured threshold (default 300 seconds / 5 minutes)
  * The print completion percentage is above the configured threshold (default 90%)

This should cover both long and short prints; you wouldn't want the bed to turn off 90% into a 20 hour print, or 5 minutes before the end of a 10 minute total print.

Be sure to monitor your print, as turning off the bed heater could cause the print to come loose prior to completion.
