---
layout: plugin

id: freemobilenotifier
title: OctoPrint-FreeMobile-Notifier
description: Octoprint plugin for print completion notifications using Free (Free is a French telecommunications company)
author: Antoine CAVARD
license: AGPLv3

date: 2017-01-25

homepage: https://github.com/Pinaute/OctoPrint-FreeMobile-Notifier
source: https://github.com/Pinaute/OctoPrint-FreeMobile-Notifier
archive: https://github.com/Pinaute/OctoPrint-FreeMobile-Notifier/archive/master.zip

# TODO set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false

tags:
- notification

screenshots:
- url: /assets/img/plugins/freemobilenotifier/freemobilenotifier.jpg
  alt: Settings dialog and SMS notification screenshot
  caption: Configure notification recipient, login, pass key and message.

featuredimage: /assets/img/plugins/freemobilenotifier/freemobilenotifier.jpg


compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.0

---

Receive SMS notifications when OctoPrint jobs are complete.