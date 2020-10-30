---
layout: plugin

id: continuousprint
title: Continuous Print
description: Allows the queueing and automatic print and clearing of the queue
author: Paul GOddard
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2020-04-24

homepage: https://github.com/Zinc-OS/continuousprint
source: https://github.com/Zinc-OS/continuousprint
archive: https://github.com/Zinc-OS/continuousprint/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- continuous print
- queueing

featuredimage: /assets/img/plugins/continuousprint/screenshot.png

compatibility:
  python: ">=2.7,<4"

---

# Continuous Print

Simple plugin to allow queuing of code files which when started will automatically print, run bed clearing commands and then print again until the end of the queue. Depndeing on your printer, and the material you are printing with, you may want to change the bed clearing commands.

## Screenshot

![screenshot](/assets/img/plugins/continuousprint/screenshot.png)
