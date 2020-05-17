---
layout: plugin

id: pushover
title: Pushover
description: A plugin that send a notification with Pushover when the job is done or is failed
author: Thijs Bekke
license: AGPLv3

date: 2016-04-13

homepage: https://github.com/thijsbekke/OctoPrint-Pushover/
source: https://github.com/thijsbekke/OctoPrint-Pushover/
archive: https://github.com/thijsbekke/OctoPrint-Pushover/archive/master.zip

follow_dependency_links: false

tags:
- notification
- pushover

compatibility:
  python: ">=2.7,<4"

screenshots:
- url: /assets/img/plugins/pushover/settings.png
  alt: Settings
  caption: You can configure a couple of settings via Octoprint's settings. Set your user key, change the sound, priority and test your settings.
- url: /assets/img/plugins/pushover/pushover.png
  alt: Pushover
  caption: An examplatory push notification in the Pushover webclient


featuredimage: /assets/img/plugins/pushover/pushover.png

---

This plugin adds support for [Pushover notifications](https://pushover.net/) to OctoPrint.

When your job is finished or is failed OctoPrint will send a notification to Pushover. You can configure the sound or priority of the messages.

This plugin supports the following features/events

- Send notifications on an interval (percent or time)
- Include a capture of your camera with your notifications
- Temperature reached
- Print done
- After first couple of layer
- Print Failed
- Print Started
- Printer is Waiting
- Printer Shutdown
- Print Paused
- Alert Event (M300)
- Panic Event (M112)
- Error Event
- Limit to specific devices 

