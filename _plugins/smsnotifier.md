---
layout: plugin

id: smsnotifier
title: SMS Notifier (with Twilio)
description: Recieve SMS notifications when OctoPrint jobs are complete.
author: Richard Bteman
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2017-01-10

homepage: https://github.com/taxilian/OctoPrint-Twilio
source: https://github.com/taxilian/OctoPrint-Twilio
archive: https://github.com/taxilian/OctoPrint-Twilio/archive/master.zip

# set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false

tags:
- notification

screenshots:
- url: /assets/img/plugins/smsnotifier/smsnotifier.png
  alt: Settings dialog and SMS notification screenshot
  caption: Configure notification recipient, Twilio API SID and Auth Token, printer
    name, and from number.
featuredimage: /assets/img/plugins/smsnotifier/smsnotifier.png

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.4

  python: '>=2.7,<4'

attributes:
- cloud
---

Recieve email notifications when OctoPrint jobs are complete.
