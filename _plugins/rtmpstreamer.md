---
layout: plugin

id: rtmpstreamer
title: OctoPrint-RTMPStreamer
description: Plugin that reencodes the mjpg stream provided by octopi/mjpgstreamer/yawcam and posts to any RTMP stream server (ie Twitch) and adds a tab that will allow for wathing configured stream assuming there is a webpage url that allows that type of connection.
author: jneilliii
license: AGPLv3

date: 2018-08-13

homepage: https://github.com/jneilliii/OctoPrint-RTMPStreamer
source: https://github.com/jneilliii/OctoPrint-RTMPStreamer
archive: https://github.com/jneilliii/OctoPrint-RTMPStreamer/archive/master.zip

follow_dependency_links: false

tags:
- Twitch
- Live Stream
- RTMP

screenshots:
- url: /assets/img/plugins/rtmpstreamer/tab_screenshot.jpg
  alt: RTMP Streamer
  caption: RTMP Streamer

featuredimage: /assets/img/plugins/rtmpstreamer/tab_screenshot.jpg

---

# RTMP Streamer

Plugin that adds a tab to OctoPrint for viewing, starting, and stopping a re-encoded stream to any RTMP server. Only tested with Twitch.

**Notes:**
- Plugin requires that OctoPrint's webcam stream uses a full url path including the ip address, ie `http://192.168.1.2/webcam/?action=stream`
- Only tested streaming to Twitch from a Pi3.
- Plugin does not provide a streaming application, it just re-encodes the mjpg stream (included with ocotpi) to a flv stream and transmits to configured RTMP server url.
- Although resolution is configurable in the plugin, the mjpg input stream being re-encoded may have a lower resolution and therefore not really be as high as you set it in the plugin settings.

## Screenshots

![screenshot](/assets/img/plugins/rtmpstreamer/tab_screenshot.jpg)

## Prerequisites

In order to stream please follow the instructions [here](https://github.com/jneilliii/OctoPrint-RTMPStreamer/blob/master/docker_instructions.md).  If you are just wanting to watch a stream enter the view url in settings, no other prerequisites are required.

## Settings

![screenshot](/assets/img/plugins/rtmpstreamer/settings_screenshot.jpg)

Once the prerequisites are met and the test command is successfull enter the resolution, stream url, and view url in the RTMP Streamer settings.

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](/assets/img/plugins/rtmpstreamer/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/rtmpstreamer/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
