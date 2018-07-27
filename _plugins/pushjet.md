---
layout: plugin

id: pushjet
title: OctoPrint-Pushjet
description: A plugin to send notifications with Pushjet when the job is done or is failed
author: Jacopo Ferrigno
license: AGPLv3

date: 2017-09-09

homepage: https://github.com/dipusone/OctoPrint-Pushjet
source: https://github.com/dipusone/OctoPrint-Pushjet
archive: https://github.com/dipusone/OctoPrint-Pushjet/archive/master.zip

follow_dependency_links: false


tags:
- notification
- Pushjet

screenshots:
- url: /assets/img/plugins/pushjet/settings.png
  alt: Settings
  caption: The plugin has some configurable settings which can modify the messages and they stile.

featuredimage: /assets/img/plugins/pushjet/settings.png

---

Notification plugin for [OctoPrint](https://octoprint.org). It can be used to receive push notifications on your phone using [Pushjet](https://pushjet.io/).
This is practically an adaptation of the plugin from [thijsbekke](https://github.com/thijsbekke/OctoPrint-Pushover/) with minor modification and 
the possibility to sent the notification asynchronously.

