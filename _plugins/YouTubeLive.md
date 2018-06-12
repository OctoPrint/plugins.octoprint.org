---
layout: plugin

id: YouTubeLive
title: OctoPrint-YouTubeLive
description: Simple plugin to add a YouTube Live tab to OctoPrint.
author: jneilliii
license: AGPLv3

date: 2017-07-23

homepage: https://github.com/jneilliii/OctoPrint-YouTubeLive
source: https://github.com/jneilliii/OctoPrint-YouTubeLive
archive: https://github.com/jneilliii/OctoPrint-YouTubeLive/archive/master.zip

follow_dependency_links: false

tags:
- YouTube
- Live Stream

screenshots:
- url: /assets/img/plugins/YouTubeLive/tab_screenshot.jpg
  alt: YouTubeLive
  caption: YouTubeLive

featuredimage: /assets/img/plugins/YouTubeLive/tab_screenshot.jpg

---

# YouTube Live

Plugin that adds a YouTube Live tab to OctoPrint with the capability of starting and stopping a live stream that is created by reencoding the mjpg stream configured in OctoPrint's Webcam & Timelapse settings.

**Note:** OctoPrint's webcam stream requires using a full url path with an ip address, ie `http://192.168.1.2:8080/?action=stream` 

## Screenshots

![screenshot](/assets/img/plugins/YouTubeLive/tab_screenshot.jpg)

## Prerequisites

In order to stream please follow the instructions [here](https://github.com/jneilliii/OctoPrint-YouTubeLive/blob/master/docker_instructions.md).  If you are just wanting to watch a stream enter the channel id in settings, no other prerequisites required.

## Settings

![screenshot](/assets/img/plugins/YouTubeLive/settings_screenshot.jpg)

Once installed enter your YouTube's channel id ([Advanced Account Settings](https://www.youtube.com/account_advanced)) and your YouTube stream id ([YouTube Live Dashboard](https://www.youtube.com/live_dashboard)) into the YouTube Live plugin settings.

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip if you find this plugin helpful.

[![paypal](/assets/img/plugins/YouTubeLive/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
