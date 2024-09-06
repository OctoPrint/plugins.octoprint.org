---
layout: plugin

id: xmpp_plugin
title: XMPP Plugin
description: Sends print progress notifications over xmpp
authors:
- Tobias Sachs
license: AGPLv3

date: 2023-12-27

homepage: https://github.com/tobser/octoprint-xmpp-plugin
source: https://github.com/tobser/octoprint-xmpp-plugin
archive: https://github.com/tobser/octoprint-xmpp-plugin/archive/main.zip

tags:
- xmpp
- jabber

screenshots:
- url: /assets/img/plugins/xmpp_plugin/xmpp-plugin-configuration.png
  alt: screenshot configurationdialog for the xmpp-plugin
  caption: plugin confgiguration

featuredimage: /assets/img/plugins/xmpp_plugin/xmpp-plugin-configuration.png

compatibility:
  python: ">=3,<4"

attributes:
- cloud

---

# A Simple XMPP Plugin for octoprint.

This plugin lets you configure an account to connect to a
[xmpp](https://en.wikipedia.org/wiki/XMPP) server to
send notifications about your prints progress to another xmpp account.

Currently this plugin can inform you about the start of the octoprint service as well
as the start/stop of your prints. It is also possible to trigger a notification every x%
of print progress.

Recently a feature was added to configure custom g-codes to trigger notifications.
This makes it possible to get notified about pretty much everything that's contained in
your g-code file. I use it to notify me about a required filament change or when the print
was paused.
