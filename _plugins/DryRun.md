---
layout: plugin

id: DryRun
title: DryRun
description: Print without heating/extruding.
author: Olli
license: AGPLv3

date: 2019-04-02

homepage: https://github.com/OllisGit/OctoPrint-DryRun
source: https://github.com/OllisGit/OctoPrint-DryRun
archive: https://github.com/OllisGit/OctoPrint-DryRun/releases/latest/download/master.zip

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

#### Support my Efforts

This plugin, as well as my [other plugins](https://github.com/OllisGit/) were developed in my spare time.
If you like it, I would be thankful about a cup of coffee :) 

[![More coffee, more code](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2BJP2XFEKNG9J&source=url)

## Details
The implementation is based on the "test-mode" from [Octolapse](https://github.com/FormerLurker/Octolapse/)

For implementation details please visit the [homepage]({{ page.homepage | absolute_url }}).
