---
layout: plugin

id: thespaghettidetective
title: Access Anywhere - The Spaghetti Detective
description: Monitor and control your printer anywhere over the internet, on your phone! No port-forwarding or VPN is needed. Best part? AI-based failure detection!
author: TSD Team
license: AGPLv3

# TODO
date: 2019-11-07

homepage: https://www.thespaghettidetective.com
source: https://github.com/TheSpaghettiDetective/OctoPrint-TheSpaghettiDetective
archive: https://github.com/TheSpaghettiDetective/OctoPrint-TheSpaghettiDetective/archive/master.zip

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

# TODO
tags:
- remote
- monitor
- monitoring
- webcam
- AI
- Machine Learning
- phone
- control
- port forwarding
- internet

featuredimage: /assets/img/plugins/thespaghettidetective/video_preview1.png

# TODO
# You only need the following if your plugin requires specific OctoPrint versions or
# specific operating systems to function - you can safely remove the whole
# "compatibility" block if this is not the case.

compatibility:

  # List of compatible versions
  #
  # A single version number will be interpretated as a minimum version requirement,
  # e.g. "1.3.1" will show the plugin as compatible to OctoPrint versions 1.3.1 and up.
  # More sophisticated version requirements can be modelled too by using PEP440
  # compatible version specifiers.
  #
  # You can also remove the whole "octoprint" block. Removing it will default to all
  # OctoPrint versions being supported.

  octoprint:
  - 1.3.2

  # List of compatible operating systems
  #
  # Valid values:
  #
  # - windows
  # - linux
  # - macos
  # - freebsd
  #
  # There are also two OS groups defined that get expanded on usage:
  #
  # - posix: linux, macos and freebsd
  # - nix: linux and freebsd
  #
  # You can also remove the whole "os" block. Removing it will default to all
  # operating systems being supported.

  os:
  - linux
  - windows
  - macos
  - freebsd

---

**Can't sleep well whenever your 3D printer is printing at night? Always worried that your print may fail when you are not home?**

[The Spaghetti Detective](https://www.thespaghettidetective.com) constantly watches your prints when you are not. It uses AI (Deep Learning) to analyze webcam images in the background and alerts you when your print shows the signs of failing.

It also comes with a host of other features so that you can **print remotely with a peace of mind even when you are not home**.

* Remote webcam access. No port-forwarding or VPN required (merged from [OctoPrint Anywhere](https://plugins.octoprint.org/plugins/anywhere/)).

* Full remote control of your printer. Pause or cancel print. Check and set heater temperatures or turn them off. Move print head.

* Upload G-Code files and start a print remotely.

* Easy share of your webcam streaming or time-lapses with your friend.

* Alert and print job notification (when a print is done or cancelled) via email, Telegram, PushBullet, and Slack.

{% include youtube.html vid="VRoV9Z1C1yM" preview="'/assets/img/plugins/thespaghettidetective/video_preview1.png'" %}

<br />

## Sounds cool! But does this AI thing really work?

The Spaghetti Detective is still at early stage so it doesn't always get it right. But many beta testers have already written to us and told us "hey it worked!". Here are a few time-lapses from our users:

{% include youtube.html vid="znI9_Vs6X9c" preview="'/assets/img/plugins/thespaghettidetective/video_preview2.png'" %}
From beta tester **Torsten**

{% include youtube.html vid="btNtCFfFYk0" preview="'/assets/img/plugins/thespaghettidetective/video_preview3.png'" %}
From beta tester **Lila**

If you can't have enough spaghetti (pun intended), head to our [Spaghetti Gallery](https://app.thespaghettidetective.com/publictimelapses/) for more time-lapses.


## How about webcam streaming?

Glad that you asked! The Spaghetti Detective has a shiny new feature - webcam streaming in 25 frames per second (Pro subscriber only)! Check out this video and be amazed about how smooth the webcam streaming is!

{% include youtube.html vid="UgGzcuX6Z1A" preview="'/assets/img/plugins/thespaghettidetective/streaming.png'" %}

## Install and setup

Setting up The Spaghetti Detective is quite straightforward. Just install this plugin and follow the steps on the wizard screen and you will be all set.

If you run into any difficulties, check out the [Setup Guide](https://www.thespaghettidetective.com/docs/octoprint-plugin-setup/).

![wizard](/assets/img/plugins/thespaghettidetective/plugin_wizard.png "The Spaghetti Detective Set up Wizard")

## Does it cost anything?

Yes and No.

* First and foremost, The Spaghetti Detective is an [open source project](https://github.com/TheSpaghettiDetective). You can always grab the code and run the server yourself.
* If you want to skip the hassle and risk of setting up the server and exposing it to internet, you can use The Spaghetti Detective cloud. You can have a free account with limited service, or upgrade to a paid account for a couple coffees a month if you want unrestricted access and features. Check out the [pricing](https://app.thespaghettidetective.com/ent/pricing/).

<hr />

*Questions? Comments? Run into problems? [Reach out to us](mailto:support@thespaghettidetective.com).*

*Support us by liking us or following us on social media:* &nbsp;<a href="https://www.facebook.com/pg/thespaghettidetective/posts/"><i class="fab fa-facebook fa-2x" style="color: rgb(121, 53, 241);"></i></a>&nbsp;<a href="https://www.youtube.com/channel/UCbAJcR6t5lrdZ1JXjPPRjGA/featured?view_as=subscriber"><i class="fab fa-youtube-square fa-2x" style="color: rgb(121, 53, 241);"></i></a>&nbsp;<a href="https://twitter.com/thespaghettispy"><i class="fab fa-twitter-square fa-2x" style="color: rgb(121, 53, 241);"></i></a>
