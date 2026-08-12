---
layout: plugin

id: fullscreen
title: Fullscreen Webcam
description: Open the webcam feed in fullscreen mode with extra details about the printjob
authors:
    - Mike Ratcliffe
    - Paul de Vries
license: AGPLv3
date: 2017-01-16

homepage: https://github.com/MikeRatcliffe/OctoPrint-FullScreen
source: https://github.com/MikeRatcliffe/OctoPrint-FullScreen
archive: https://github.com/MikeRatcliffe/OctoPrint-FullScreen/archive/main.zip
follow_dependency_links: false

tags:
- ui
- display
- webcam

screenshots:
- url: /assets/img/plugins/fullscreen/main.jpg
  alt: Fullscreen mode
  caption: Fullscreen mode

featuredimage: /assets/img/plugins/fullscreen/main.jpg

redirect_from:
- /plugins/fullscreen_webcam

compatibility:
  python: ">=2.7,<4"

---
This plugin will allow you to open the webcam feed in fullscreen mode by double clicking the image. It will also show an overlay containing information about print time, remaining time, temperatures and a pause button.

If the DisplayLayerProgress plugin is installed, it will also display the layer progress.
