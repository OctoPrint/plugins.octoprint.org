---
layout: plugin

id: DryRun
title: DryRun
description: Print without heating/extruding.
author: Olli
license: AGPLv3

date: 2019-03-25

homepage: https://github.com/OllisGit/OctoPrint-DryRun
source: https://github.com/OllisGit/OctoPrint-DryRun
archive: https://github.com/OllisGit/OctoPrint-DryRun/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- printer

screenshots:
- url: https://github.com/OllisGit/OctoPrint-DryRun/raw/master/screenshots/StateAndNavBar.jpg
  alt: dryrun-activated
  caption: dryrun-activated
  
featuredimage: dryrun-activated

---

A Octoprint-Plugin that allows to execute a print without heating your bed or nozzle, turning on any fans, or extruding any filament.

The implementation is based on the "test-mode" from [Octolapse](https://github.com/FormerLurker/Octolapse/)

For implementation details please visit the [homepage]({{ page.homepage | absolute_url }}).