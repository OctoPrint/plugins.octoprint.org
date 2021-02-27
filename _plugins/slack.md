---
layout: plugin

id: slack
title: Slack
description: Send message to Slack chat when printing events happen
authors: 
  - Maurice Kevenaar
  - Richard Joyce
license: MIT

# today's date in format YYYY-MM-DD, e.g.
date: 2015-10-28

homepage: https://github.com/mkevenaar/OctoPrint-Slack
source: https://github.com/mkevenaar/OctoPrint-Slack
archive: https://github.com/mkevenaar/OctoPrint-Slack/archive/master.zip

# set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false

tags:
- notification

screenshots:
- url: /assets/img/plugins/slack/slack.png
  alt: View of chat in Slack
  caption: Printing events in slack chat

- url: /assets/img/plugins/slack/settings.png
  alt: Settings for plugin
  caption: Configurable settings for plugin

- url: /assets/img/plugins/slack/settings2.png
  alt: More settings for plugin
  caption: Configurable event messages

featuredimage: /assets/img/plugins/slack/slack.png

compatibility:
  python: ">=2.7,<4"

---
Send messages to your group's Slack chat when printing events happen! You need to set up an [Incoming Webhook](https://my.slack.com/services/new/incoming-webhook) integration on the Slack side to use this.

Features
--------

* Select which events you want to trigger a chat notification for
* Customizable messages for each event
* Customize bot icon and username in Slack chat
* Sends elapsed time of print after finished
