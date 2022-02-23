---
layout: plugin

id: webcamstreamer
title: OctoPrint-WebcamStreamer
description: Plugin that re-encodes the webcam and streams it to streaming sites like YouTube Live or Twitch.Tv
author: Adi Linden
license: AGPLv3

date: 2019-02-08

homepage: https://github.com/adilinden-oss/octoprint-webcamstreamer
source: https://github.com/adilinden-oss/octoprint-webcamstreamer
archive: https://github.com/adilinden-oss/octoprint-webcamstreamer/archive/master.zip

tags:
- Stream
- Webcam

screenshots:
- url: /assets/img/plugins/webcamstreamer/screenshot_tab.png
  alt: WebcamStreamer Tab
  caption: WebcamStreamer Tab
- url: /assets/img/plugins/webcamstreamer/screenshot_settings.png
  alt: WebcamStreamer Settings
  caption: WebcamStreamer Settings
- url: /assets/img/plugins/webcamstreamer/screenshot_settings_advanced.png
  alt: WebcamStreamer Advanced Settings
  caption: WebcamStreamer Advanced Settings

featuredimage: /assets/img/plugins/webcamstreamer/screenshot_tab.png

abandoned: https://github.com/OctoPrint/plugins.octoprint.org/issues/807

---

# OctoPrint-WebcamStreamer

## Overview

Plugin that adds a tab to OctoPrint for viewing, starting, and stopping a live stream.

![screenshot](/assets/img/plugins/webcamstreamer/screenshot_tab.png)

**Credits:**

Inspired by and based on the work by

- Alex Ellis found [here](https://blog.alexellis.io/live-stream-with-docker/)
- jneilliii [OctoPrint-YouTube Live](https://plugins.octoprint.org/plugins/YouTubeLive/) plugin found [here](https://github.com/jneilliii/OctoPrint-YouTubeLive)

## Requirements for Streaming

Although this plugin should work with a wide variety of webcam, it has only been tested with a Raspberry Pi cam running on [OctoPi](https://octoprint.org/download/) and made available via OctoPrint mjpeg-streamer. This plugin relies on a [Docker](https://www.docker.com/) container running [FFmpeg](https://www.ffmpeg.org/) to convert the mjpeg-streamer video stream and pipe it to a live streaming service. The YouTube Live and Twitch.Tv streaming services have been tested.

## Installation

Using `ssh` access the OctoPi and install `docker`:

    curl -sSL https://get.docker.com | sh
    sudo usermod pi -aG docker
    sudo reboot

Pull the `adilinden/rpi-ffmpeg` image:

    docker pull adilinden/rpi-stream:latest

Install OctoPrint-WebcamStreamer via one of these 3 methods, also in-depth explained on the official OctoPrint [Installing a plugin](https://plugins.octoprint.org/help/installation/) page.

1. Open the plugin repository in the Plugin Manager's settings dialog, search for "OctoPrint-WebcamStreamer" and install with the "Install" button.

2. Open the plugin repository in the Plugin Manager's settings dialog, click on "Get more..." and enter the `https://github.com/adilinden-oss/octoprint-webcamstreamer/archive/master.zip` URL in the "... from URL" box. Click the Install button to complete the installation.

3. Access the OctoPi command line and run the `~/oprint/bin/pip install https://github.com/adilinden-oss/octoprint-webcamstreamer/archive/master.zip` command.

## Setup

Pull up **Webcam Streamer** in the OctoPi settings panel

- Enter your streaming providers embed URL for your live stream video into the "Viewer Embed URL" field.
    * YouTube: Your "YouTube Channel ID" is needed to construct the embed URL. It can be found on your [Advanced settings](https://www.youtube.com/account_advanced) page. With the "YouTube Channel ID" in hand, constrcut the URL like this:

        https://www.youtube.com/embed/live_stream?channel=CHANNEL_ID

    * Twitch: Your Twitch username is needed to construct the embed URL. With your username in hand, construct the URL like this:

        https://player.twitch.tv/?channel=USERNAME

- Enter your streaming providers ingest or stream server URL into the "Stream Server URL" field.
    * YoutTube: Your complete URL is created by appending your "Stream name/key" to your "Server URL". Both values can be found on your [Live dashboard](https://www.youtube.com/live_dashboard) page. With both values in hand, the complete "Stream Server URL" should look like this:

        rtmp://a.rtmp.youtube.com/live2/xxxx-xxxx-xxxx-xxxx

    * Twitch: Your complete URL is created by appending your "Primary Stream key" to the `rtmp://live.twitch.tv/app/` URL. The "Primary Stream key" can be found on your [Dashboard Settings](https://www.twitch.tv/dashboard/settings) page. The complete "Stream Server URL" should look like this:

        rtmp://live.twitch.tv/app/live_xxxxxxxxx_xxxxxxxxxx

- Enter your OctoPi webcam URL into the "OctoPi Webcam URL" field. A fully qualified URL is needed containing either the resolvable hostname or the IP address of the OctoPi. The "OctoPi Webcam URL" typically looks something like this:

        http://192.168.10.79:8080/?action=stream

Terse setup information is also availabe via the expandable "Additional Information" section on the "Webcam Streamer" settings page.

![screenshot](/assets/img/plugins/webcamstreamer/screenshot_settings.png)

## Advanced Setup

Advanced option allow for modification of the [FFmpeg](https://www.ffmpeg.org/) command line for use with other streaming services or cameras. It also allows for a different [Docker](https://www.docker.com/) container to be specified if desired or needed.

- "Webcam Frame Rate" default is 5 frames per second which is appropriate for the Raspberry Pi webcam.

- "Docker Image" default is `adilinden/rpi-stream:latest`. This value needs to match the docker image installed in the setup steps.

- "Docker Container" default is `WebStreamer`. This value is rather arbitrary but the default makes sense (to me).

- "FFmpeg Command" allows for customization of the `ffmpeg` command line. Variable substitution is performed to insert setup values into the `ffmpeg` command line.

    Default command line for `ffmpeg` is:

        ffmpeg -re -f mjpeg -framerate 5 -i {webcam_url} -ar 44100 -ac 2 -acodec pcm_s16le -f s16le -ac 2 -i /dev/zero -acodec aac -ab 128k -vcodec h264 -pix_fmt yuv420p -framerate {frame_rate} -g {gop_size} -strict experimental -filter:v {filter} -f flv {stream_url}

    The following variable substitutions are available:

    | FFmpeg Cmd Var   | Settings value
    | -----------------| -------------------------------------------|
    | `{stream_url}`     | Stream Server URL
    | `{webcam_url}`     | OctoPi Webcam URL
    | `{frame_rate}`     | OctoPi Webcam Frame Rate
    | `{gop_size}`       | Internal Calculated Value (frame rate * 2)
    | `{filter}`         | Internal Calculated Value

![screenshot](/assets/img/plugins/webcamstreamer/screenshot_settings_advanced.png)
