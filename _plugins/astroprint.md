---
layout: plugin

id: astroprint
title: AstroPrint Cloud
description: Wirelessly manage and monitor your OctoPi powered printer from the AstroPrint Platform (AP Mobile Apps, AP Desktop Software, & AP Web Portal).
author: AstroPrint
license: AGPLv3

date: 2017-12-15

homepage: https://github.com/AstroPrint/OctoPrint-AstroPrint/blob/master/README.md
source: https://github.com/AstroPrint/OctoPrint-AstroPrint
archive: https://github.com/AstroPrint/OctoPrint-AstroPrint/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- cloud printing
- remote monitoring
- remote access
- video streaming
- design management
- fleet management

screenshots:
- url: /assets/img/plugins/astroprint/astroprint-hero.jpg
  alt: AstroPrint Platform
  caption: Connect your OctoPrint Device to the AstroPrint Software Suite
- url: /assets/img/plugins/astroprint/astroprint-plugin.png
  alt: AstroPrint Plugin
  caption: View of the AstroPrint Plugin on OctoPrint
- url: /assets/img/plugins/astroprint/astroprint-monitor.png
  alt: AstroPrint Monitor
  caption: Monitor your OctoPrint-enabled 3D printer remotely from the AstroPrint Cloud
- url: /assets/img/plugins/astroprint/start-print.png
  alt: Start a Print
  caption: Start a print from your AstroPrint Cloud on your OctoPi device
- url: /assets/img/plugins/astroprint/apm-monitor-crop.gif
  alt: Remote Monitoring
  caption: Monitor your OctoPrint Device from anywhere with the FREE AstroPrint App
- url: /assets/img/plugins/astroprint/apm-thing-crop.gif
  alt: Print from your phone
  caption: Find and print cool designs right from your phone

featuredimage: /assets/img/plugins/astroprint/astroprint-hero.jpg

compatibility:
  python: ">=2.7,<4"
  
  octoprint:
  - 1.3.4
  
---

# Connect to the AstroPrint Cloud

Once the AstroPrint plugin is installed on your OctoPi, and you have logged into your FREE AstroPrint Cloud account, you will be able to access, control, and monitor your 3D Printer from AstroPrint Mobile, AstroPrint Desktop, and the AstroPrint Web Portal.

General benefits of connecting your OctoPi to the AstroPrint Cloud include:

- Remotely start / stop prints, monitor prints, pre-heat, etc.
- Access your printer(s) from anywhere.  No need to be limited to local networks.
- Manage multiple printers easily.
- Cloud slicing - This means you can print from any device, slicing happens in the cloud. (AstroPrint Desktop offers offline slicing as well.)
- Sync your printing files across devices.
- and more…

# Plugin Setup

You can follow the instructions in this [README](https://github.com/AstroPrint/OctoPrint-AstroPrint/blob/master/README.md)

## AstroPrint Mobile

Use the free [AstroPrint Mobile](https://www.astroprint.com/products/p/astroprint-mobile) app (iOS & Android) to connect to your OctoPi.  You can connect from anywhere: local network, out-of-network wifi, or via your phone's data network.  The Mobile app lets you monitor prints, start/stop prints, search and print from Thingiverse, check out your printing stats, save files in the cloud, slice files in the cloud, and more.

## AstroPrint.com Web Portal

In addition to using Mobile and Desktop, you'll be able to access your OctoPi from any web enabled device by logging in at [AstroPrint.com](https://www.astroprint.com).  You can also access 3rd party applications here to do things like:  Cloud based file repair, print queuing, and more.

## Other Applications

Via AstroPrint APIs, some developers are adding the ability to print from their apps directly to 3D printers.  You'll be able to print directly to your printer from websites like the [NIH 3D Print Exchange](https://3dprint.nih.gov/), [3DaGoGo](https://www.3dagogo.com) and [TinkerCad](https://www.tinkercad.com).  You’ll also be able to print-from-app from apps like [Toy Maker](https://toymaker.astroprint.com).


Happy Printing!<br>
[The AstroTeam](https://www.astroprint.com/team)