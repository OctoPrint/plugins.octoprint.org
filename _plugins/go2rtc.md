---
layout: plugin

id: go2rtc
title: go2rtc
description: Plugin to configure and use go2rtc server streams.
authors:
- jneilliii
license: AGPLv3
date: 2025-02-09

homepage: https://github.com/jneilliii/OctoPrint-go2rtc
source: https://github.com/jneilliii/OctoPrint-go2rtc
archive: https://github.com/jneilliii/OctoPrint-go2rtc/archive/master.zip

tags:
- go2rtc
- multicam
- multi cam
- webcam

featuredimage: /assets/img/plugins/go2rtc/screenshot.png

compatibility:
  octoprint:
  - 1.9.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=3,<4"
attributes:
#  - cloud  # if your plugin requires access to a cloud to function
#  - commercial  # if your plugin has a commercial aspect to it
#  - free-tier  # if your plugin has a free tier

---

# go2rtc

This plugin allows for the configuration and embedding of [go2rtc](https://github.com/AlexxIT/go2rtc) streams inside OctoPrint's UI directly.

## Requirements

You must have a running go2rtc server/service. There are many [options](https://github.com/AlexxIT/go2rtc#fast-start) available for running go2rtc. For OctoPi 1.0.0+ images I have created [installation steps](https://gist.github.com/jneilliii/93b412cb0bbf6b7bfd76f7e10d612f24?permalink_comment_id=4993013#gistcomment-4993013) to get you started for replacing the default streamers with go2rtc.

## Configuration

Once installed, enter the server address of your go2rtc installation and click verify.

![verify screenshot](/assets/img/plugins/go2rtc/screenshot_settings_verify.png)

The plugin will validate the server url is reachable and that the necessary configuration settings are set. If a required setting is not detected you will be presented with a warning and direction on changing. The plugin can make this change for you as mentioned in the warning.

![cors screenshot](/assets/img/plugins/go2rtc/screenshot_settings_cors.png)

Once the required settings are applied, a list of saved streams will display and inputs for adding additional streams. You can either manually enter a stream configuration (see go2rtc's documentation) or click the add button next to one of the ffmpeg detected devices.

![streams screenshot](/assets/img/plugins/go2rtc/screenshot_settings.png)

Click Save and you will need to restart OctoPrint to get the newly added webcams added to the Control tab properly.

 ![restart screenshot](/assets/img/plugins/go2rtc/screenshot_restart.png)

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](/assets/img/plugins/go2rtc/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/go2rtc/paypal-with-text.png)](https://paypal.me/jneilliii) [![GitHub](/assets/img/plugins/go2rtc/github.png)](https://github.com/sponsors/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
