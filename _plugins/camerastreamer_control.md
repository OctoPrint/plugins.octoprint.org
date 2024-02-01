---
layout: plugin

id: camerastreamer_control
title: Camera-Streamer Control
description: Make use of smooth, low-latency, low-bandwidth WebRTC streams from the OctoPi 'New camera stack'
authors:
- Charlie Powell
license: AGPLv3

date: 2024-02-01

homepage: https://github.com/cp2004/OctoPrint-CameraStreamer-Control
source: https://github.com/cp2004/OctoPrint-CameraStreamer-Control
archive: https://github.com/cp2004/OctoPrint-CameraStreamer-Control/releases/latest/download/release.zip

tags:
- webcam
- camera
- streaming
- camera-streamer
- h264
- webrtc
- camera-streamer-control
- new-camera-stack
- new-stack
- octopi

compatibility:
  octoprint:
  - 1.9.0

  os:
  - linux

  python: ">=3.7,<4"

---

Using OctoPi's new camera stack? Add this plugin to watch your prints in shiny, fast, low bandwidth H264 glory!

*The new camera stack is not fully stable yet, and neither is this plugin. Please report issues you find!*

*There may be cases where the new stack does not work for you. Please make a backup of your OctoPi instance before installing & be prepared to revert!*

## How do I use it?

First, you need to be using the recent updates to the streaming stack in OctoPi, based on camera-streamer that
Gina published a short while ago. [For info on that, see the blog post here](https://octoprint.org/blog/2023/05/24/a-new-camera-stack-for-octopi/).

You can install this image through the Raspberry Pi Imager. Follow the steps on <https://octoprint.org/download>,
but select the 'new camera stack' image:

![Image highlighting the correct image in the Pi imager](/assets/img/plugins/camerastreamer_control/pi_imager.png)

Once that is set up and running, you'll be able to install this plugin. It can be installed by finding it
from the plugin manager or manually using this URL:

```
https://github.com/cp2004/OctoPrint-CameraStreamer-Control/releases/latest/download/release.zip
```

Once installed, you should see your webcam stream still in the control tab,
but with a new option to switch to 'Camera Streamer':

![Image showing the new option in the control tab](/assets/img/plugins/camerastreamer_control/control_tab.png)

## Enabling WebRTC streaming

camera-streamer provides a h264 encoded stream alongside the classic mjpg stream. This plugin lets you use that
to view your webcam as well! You can switch stream formats in the plugin settings:

![Image showing the new option in the settings tab](/assets/img/plugins/camerastreamer_control/settings_tab.png)

### ⚠️ A note on WebRTC support

**This is still an 'experimental' feature** and issues will continue to be worked out. If your stream fails to connect,
the plugin will automatically fall back to the old mjpg stream, so you shouldn't see any interruption.

It is also important to note that camera-streamer uses the Pi's hardware encoders to do the heavy lifting here. On
low-powered Pi's such as the Pi Zero, you will struggle to use high resolutions and frame rates. A Pi 4 should be
capable of 1080p 30FPS streaming, but this is not guaranteed. If you find stuttering in the stream, lower the resolution
and framerate in the [streaming stack configuration](https://faq.octoprint.org/camera-streamer-config).
