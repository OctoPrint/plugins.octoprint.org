---
layout: plugin
id: snapstream
title: SnapStream
description: Emulate webcam streaming by showing a sequence of snapshots
archive: https://github.com/markwal/OctoPrint-SnapStream/archive/master.zip
homepage: https://github.com/markwal/OctoPrint-SnapStream
source: https://github.com/markwal/OctoPrint-SnapStream
author: Mark Walker
license: AGPLv3
date: 2015-05-22
tags:
- ui
compatibility:
  octoprint:
  - 1.2.0
---

The default video streamer in the OctoPi image is mjpg-streamer. It works by
fairly simply stitching the jpeg images from the webcam into a stream that can
be displayed by the browser. You may want to avoid this stitching and just have
javascript display the jpg images every few hundred milliseconds instead.

A couple of reasons might be:

1. You want to use a browser that doesn't support mjpeg streams (IE).

2. You want to reduce your bandwidth and cpu usage on your host.

You can reduce bandwidth and cpu usage by reducing the frame rate on
mjpg-streamer, but perhaps the plugin is even lighter weight, try it out on
your hardware and see.

Settings
--------
The plugin has a couple of settings you can change:

1. Frames per second.

    The plugin uses javascript to update the snapshot so the frames are really
    limited by the browsers ability/willingness to call a timer interval
    function. Probably best to stay in the slow, reliable, but choppy end of
    things: 1, 2 or 4 or something like that.

2. Fallback mode only.

    The plugin only takes over and uses snapshots when
    the stream fails to load.
