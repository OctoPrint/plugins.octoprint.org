---
layout: plugin

id: preheat
title: Preheat Button
description: Automatically heat printhead to the printing temperature of the current gcode file
author: Marian Kleineberg
license: MIT

date: 2017-11-21

homepage: https://github.com/marian42/octoprint-preheat
source: https://github.com/marian42/octoprint-preheat
archive: https://github.com/marian42/octoprint-preheat/archive/master.zip

follow_dependency_links: false

tags:
- ui
- api
- temperature

featuredimage: /assets/img/plugins/preheat/preheat.png

screenshots:
- url: /assets/img/plugins/preheat/preheat.png
  alt: Screenshot

# You only need the following if your plugin requires specific OctoPrint versions or
# specific operating systems to function - you can safely remove the whole
# "compatibility" block if this is not the case.

---

This plugin adds a preheat button to preheat the nozzle to the printing temperature of the selected gcode file.
This can be done manually but this plugin makes it more convenient.
If the target temperature is not zero, the button will instead turn off nozzle heating (cooldown).