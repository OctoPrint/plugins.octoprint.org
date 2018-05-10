---
layout: plugin

id: multicam
title: MultiCam
description: Extends the Control tab of OctoPrint, allowing the ability to switch between multiple webcam feeds.
author: Michael Morris
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2018-05-09

homepage: https://github.com/mikedmor/OctoPrint_MultiCam
source: https://github.com/mikedmor/OctoPrint_MultiCam
archive: https://github.com/mikedmor/OctoPrint_MultiCam/archive/master.zip

tags:
- webcam
- display
- ui
- control

screenshots:
- url: /assets/img/plugins/multicam/Octoprint_MultiCam_Control.png
  alt: MultiCam Control Tab
  caption: MultiCam Control Tab
- url: /assets/img/plugins/multicam/Octoprint_MultiCam_Settings.png
  alt: MultiCam Settings
  caption: MultiCam Settings

---

It is recommended to setup a second RPi (potentially with [MotionEyeOS](https://github.com/ccrisan/motioneyeos)) to setup webcams from. Attaching more than one webcam to your octoprint device could result in high proccess use causing issues with your prints. You may also have to invest in a usb hub to power your webcams as RPi's tend to have low votage issues when they are plugged in directly to the Rpi. [This Link](https://elinux.org/RPi_Powered_USB_Hubs) has a good list of USB hubs that are support by Raspberry.

Future updates will include the more options to show different types of streams, as well as the abilitly to show more than one stream at a time.
