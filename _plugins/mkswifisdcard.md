---
layout: plugin

id: mkswifisdcard
title: OctoPrint-mkswifisdcard
description: Octoprint plugin for fast upload file to SD-card over MKS WiFi module
authors:
- om2804
license: AGPLv3

date: 2022-07-31

homepage: https://github.com/om2804/octoprint_mkswifisdcard
source: https://github.com/om2804/octoprint_mkswifisdcard
archive: https://github.com/om2804/octoprint_mkswifisdcard/archive/master.zip

tags:
- file
- file upload
- transfer
- upload
- MKS
- WiFi

screenshots:
- url: /assets/img/plugins/sdwire/sdwire-octoprint.jpg
  alt: Uploading to sdwire
  caption: Uploading to sdwire
- url: /assets/img/plugins/sdwire/sdwire-hw.jpg
  alt: sdwire hardware
  caption: sdwire hardware

featuredimage: /assets/img/plugins/sdwire/sdwire-hw.jpg

compatibility:
  octoprint:
  - 1.4.0

  os:
  - linux

  python: ">=3,<4"

---

Octoprint plugin for fast upload file to SD-card over MKS WiFi module.
Uploading file to SD-card over serial connection is very slow. Uploading file over WiFi connection is fast.