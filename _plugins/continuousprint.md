---
layout: plugin

id: continuousprint
title: Continuous Print
description: This plugin automates your printer! Queue your prints, push the button, and walk away - now with auto bed clearing and failure recovery.
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
- automation
- failure detection

featuredimage: /assets/img/plugins/continuousprint/screenshot.png

compatibility:
  python: ">=3.6,<4"

---

![screenshot](/assets/img/plugins/continuousprint/screenshot.png)

* **Add files to the queue and set a number of copies.** The plugin will print the files in sequence, clearing the bed after each print to set up for the next one.
* **Group files together to run them as a unit.** Don't make 10 boxes by printing 10 bases, then 10 lids - instead, define a "box" job and print box/lid combos in sequence.
* **Use failure recovery to stop wasting time and filament.** Optional [Spaghetti Detective](https://www.thespaghettidetective.com/) integration detects bed adhesion failures and recovers automatically.

WARNING: Your printer must have a method of clearing the bed automatically, with correct GCODE instructions set up in this plugin's settings page - damage to your printer may occur if this is not done correctly. If you want to manually remove prints, look in the plugin settings for details on how to use `@pause` so the queue is paused before another print starts.

