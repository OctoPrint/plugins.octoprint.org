---
layout: plugin

id: continuousprint
title: Continuous Print
description: Allows the queueing and automatic print and clearing of the queue
Authors: 
-Louis Sarwal
-Paul Goddard(original)
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

This is a simple plugin that, as its name suggests, allows _continuous print_. The gcode files are first loaded into a queue. Once this queue is started, the queue will automatically print from top to bottom. Between prints, it will run bed clearing commands so your prints won't get messed up.
Depending on your printer, and the material you are printing with, you may need to change the bed clearing commands.

## Screenshot

![screenshot](/assets/img/plugins/continuousprint/screenshot.png)
