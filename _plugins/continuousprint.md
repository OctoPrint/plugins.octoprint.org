---
layout: plugin

id: continuousprint
title: Continuous Print
description: Allows the queueing and automatic print and clearing of the queue
authors: 
- Scott Martin (Current)
- Louis Sarwal
- Paul Goddard
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2020-04-24

homepage: https://github.com/smartin015/continuousprint
source: https://github.com/smartin015/continuousprint
archive: https://github.com/smartin015/continuousprint/archive/master.zip

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

This plugin automates your printing!

* **Add gcode files to the queue and set a number of times to print each.** The plugin will print them in sequence, running "bed clearing" script after each.
* **Group multiple files together into "jobs" and run them multiple times.** Don't make 10 boxes by printing 10 bases, then 10 lids - just define a "box" job and print box/lid combos in sequence.
* **Reduce manual intervention with failure automation.** This plugin optionally integrates with [The Spaghetti Detective](https://www.thespaghettidetective.com/) and can retry prints that fail to adhere to the bed, with configurable limits on how hard to try before giving up.

WARNING: Your printer must have a method of clearing the bed automatically, with correct GCODE instructions set up in this plugin's settings page - damage to your printer may occur if this is not done correctly. If you want to manually remove prints, look in the plugin settings for details on how to use `@pause` so the queue is paused before another print starts.

## Screenshot

![screenshot](/assets/img/plugins/continuousprint/screenshot.png)
