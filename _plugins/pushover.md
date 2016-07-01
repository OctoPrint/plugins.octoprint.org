---
layout: plugin

id: pushover
title: Pushover
description: A plugin that send a notification with Pushover when the job is done
author: Thijs Bekke
license: AGPLv3

date: 2016-04-13

homepage: https://github.com/thijsbekke/OctoPrint-Pushover/
source: https://github.com/thijsbekke/OctoPrint-Pushover/
archive: https://github.com/thijsbekke/OctoPrint-Pushover/archive/master.zip

follow_dependency_links: false

tags:
- notification

screenshots:
- url: /assets/img/plugins/pushover/settings.png
  alt: Settings
  caption: You can configure a couple of settings via Octoprint's settings. Change the sound or priority.
- url: /assets/img/plugins/pushover/pushover.png
  alt: Pushover
  caption: An examplatory push notification in the Pushover webclient


featuredimage: /assets/img/plugins/pushover/pushover.png

compatibility:

  octoprint:
  - 1.2.0


---

This plugin adds support for [Pushover notifications](https://pushover.net/) to OctoPrint.

When your job is finished OctoPrint will send a notification to Pushover. You can configure the sound or priority of the message.



