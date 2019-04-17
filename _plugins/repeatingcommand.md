---
layout: plugin

id: repeatingcommand
title: OctoPrint_RepeatingCommand
description: Octoprint plugin for running a command at an interval during prints.
author: Andrew Erickson
license: AGPLv3

date: 2019-04-16

homepage: https://github.com/aerickson/OctoPrint_RepeatingCommand
source: https://github.com/aerickson/OctoPrint_RepeatingCommand
archive: https://github.com/aerickson/OctoPrint_RepeatingCommand/archive/master.zip

# TODO set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false

tags:
- events
- control
- integration
- command
- automation

screenshots:
- url: /assets/img/plugins/repeatingcommand/settings.png
  alt: Settings dialog screenshot

featuredimage: /assets/img/plugins/repeatingcommand/settings.png


compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.0

---

Runs a command at a specified interval during prints.

I use it to trigger my home automation to run an exhaust fan (that normally turns off after 5 minutes) when printing.
