---
layout: plugin
id: octobullet
title: Pushbullet
description: Pushes notifications about finished print jobs via Pushbullet
author: Gina Häußge
license: AGPLv3
date: 2015-07-23
homepage: https://github.com/OctoPrint/OctoPrint-Pushbullet
source: https://github.com/OctoPrint/OctoPrint-Pushbullet
archive: https://github.com/OctoPrint/OctoPrint-Pushbullet/archive/master.zip
tags: 
- notification
screenshots:
- url: /assets/img/plugins/octobullet/configuration.png
  alt: Settings Dialog
  caption: The settings dialog allows configuring the Pushbullet Access Token
- url: /assets/img/plugins/octobullet/example_push.png
  alt: Example Push Notification
  caption: An examplatory push notification in the Pushbullet client for Windows
featuredimage: /assets/img/plugins/octobullet/example_push.png
compatibility:
  octoprint:
  - 1.2.4
  
up_for_adoption: https://github.com/OctoPrint/OctoPrint-Pushbullet/issues/24
  
---

This plugin adds support for [Pushbullet notifications](https://www.pushbullet.com/) to OctoPrint.

At the current state OctoPrint will send a notification when a print job finishes. If a webcam is available, an image
of the print result will be captured and included in the notification.
