---
layout: plugin

id: signalnotifier
title: OctoPrint_Signal-Notifier
description: Octoprint plugin for print completion notifications using Signal.
author: Andrew Erickson
license: AGPLv3

date: 2018-12-04

homepage: https://github.com/aerickson/OctoPrint_Signal-Notifier
source: https://github.com/aerickson/OctoPrint_Signal-Notifier
archive: https://github.com/aerickson/OctoPrint_Signal-Notifier/archive/master.zip

# TODO set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false

tags:
- notification

screenshots:
- url: /assets/img/plugins/signalnotifier/signalnotifier.png
  alt: Settings dialog screenshot
  caption: Configure path to signal-cli, sender, recipient, and message.

featuredimage: /assets/img/plugins/signalnotifier/signalnotifier.png

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.0

---

Receive [Signal](https://signal.org/) messages when OctoPrint jobs are complete.

Requires `signal-cli` to be installed and configured. See [the plugin's github page](https://github.com/aerickson/OctoPrint_Signal-Notifier) for more information.
