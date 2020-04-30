---
layout: plugin

id: webhooks
title: OctoPrint-Webhooks
description: This allows you to send a webhook to any URL when events happen on OctoPrint.
author: Blane Townsend
license: AGPLv3

date: 2020-04-29

homepage: https://github.com/2blane/OctoPrint-Webhooks
source: https://github.com/2blane/OctoPrint-Webhooks
archive: https://github.com/2blane/OctoPrint-Webhooks/archive/master.zip

tags:
- webhook
- api
- url
- events
- prusa
- color change
- notification

screenshots:
- url: /assets/img/plugins/webhooks/Featured.png

featuredimage: /assets/img/plugins/webhooks/Featured.png

compatibility:
  python: ">=2.7,<4"

---

This plugin was created so that my own API could receive events from OctoPrint and perform custom actions such as
send a text message/push notification, log the events in a database, etc.
Also, I needed a way to get notified when a color change was needed on my Prusa. So, this plugin has a custom event
that will alert me whenever a color change is necessary. See the
[README.md](https://github.com/2blane/OctoPrint-Webhooks) for more information on how to configure
this plugin and what events are supported.
