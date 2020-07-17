---
layout: plugin

id: discordremote
title: OctoPrint-DiscordRemote
description: Discord bot for OctoPrint
author: Cameron Cross, originally by Benjamin Chanudet
license: MIT

# TODO
date: 2018-06-04

homepage: https://github.com/cameroncros/OctoPrint-DiscordRemote
source: https://github.com/cameroncros/OctoPrint-DiscordRemote
archive: https://github.com/cameroncros/OctoPrint-DiscordRemote/archive/master.zip

# tags
tags:
- discord
- notifications
- snapshots
- remote
- control

# screenshots
screenshots:
- url: /assets/img/plugins/DiscordRemote/featured.jpg
  alt: Send commands to your octoprint instance via discord
  caption: Send commands to your octoprint instance via discord
- url: /assets/img/plugins/DiscordRemote/snapshot.jpg
  alt: Get a snapshot from OctoPrint
  caption: Get a snapshot from OctoPrint
- url: /assets/img/plugins/DiscordRemote/settings.jpg
  alt: Customize the text Octorant sends to your channel
  caption: Customize the text Octorant sends to your channel

# Featured image
featuredimage: /assets/img/plugins/DiscordRemote/featured.jpg

---

# DiscordRemote

DiscordRemote is a plugin that allows OctoPrint to be interacted with using a Discord bot.

The bot is able to post messages to a discord channel based on events, and can include screenshots.

The bot also listens on the channel, for certain commands, will execute actions on the machine.
A list of supported commands is available by sending a "/help" message.
It is currently capable of:

* Starting a print.
* Aborting a print.
* Listing the files.
* Taking a snapshot with the configured webcam.
* Connecting and Disconnecting to the printer.


**Important**: There are no permissions or controls as to who can send commands to the bot. 
This **MUST** be done by the owner of the Discord channel.
