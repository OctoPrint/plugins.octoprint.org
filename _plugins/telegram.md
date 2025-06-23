---
layout: plugin

id: telegram
title: OctoPrint-Telegram
description: A plugin to send and react on messages before, during and after a print
  via Telegram Messenger.
authors:
    - Jacopo Tediosi
    - Fabian Schlenz
license: AGPLv3

date: 2016-02-25

homepage: https://github.com/jacopotediosi/OctoPrint-Telegram
source: https://github.com/jacopotediosi/OctoPrint-Telegram
archive: https://github.com/jacopotediosi/OctoPrint-Telegram/archive/master.zip

# TODO set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false

tags:
- notification
- mobile
- progress
- control

screenshots:
- url: /assets/img/plugins/telegram/features1.png
  alt: Telegram notifications during print
  caption: You can receive the current status with a webcam picture at user-definable
    intervals.
- url: /assets/img/plugins/telegram/features3.png
  alt: Requesting the current status
  caption: You can control OctoPrint via messages. E.g., sending /status lets the plugin
    send you the current status.
- url: /assets/img/plugins/telegram/features4.png
  alt: Custom keyboards
  caption: You can also abort the current print with /abort. A custom keyboard is
    shown for confirmation.
- url: /assets/img/plugins/telegram/features5.png
  alt: Settings
  caption: You can configure lots of settings via OctoPrint's settings. (Or you can
    use /settings to change them via Telegram.)
featuredimage: /assets/img/plugins/telegram/features3.png

compatibility:
  octoprint:
  - 1.4.0
  python: '>=3.7,<4'

attributes:
- cloud

---

This plugin integrates Telegram Messenger into OctoPrint.

You can receive automatic notifications with webcam images before and after a print -
and even during a print at customizable intervals, such as at specific heights or after a
certain time (e.g., every 5 mm of height OR every 10 minutes — whichever comes first).

You can also control OctoPrint via messages. For example, send:
- `/status` to receive the current printer status,
- `/abort` to stop the ongoing print,
- `/help` to get a list of all available commands.

Please refer to [the documentation on GitHub](https://github.com/jacopotediosi/OctoPrint-Telegram/blob/master/README.md)  
to learn how to register a Telegram bot - a required step for this plugin to work.
