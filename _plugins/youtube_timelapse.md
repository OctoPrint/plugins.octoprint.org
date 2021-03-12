---
layout: plugin
id: youtube_timelapse
title: Octoprint Youtube Timelapse
description: Automatically upload rendered timelapses to Youtube. Can also delete after upload to save space on the Raspberry Pi SD Card.
author: ryanfox1985
license: MIT
<<<<<<< HEAD
<<<<<<< HEAD
date: 2021-03-06
=======
date: 2021-03-09
>>>>>>> cf6598188f1539161d27b7499880f2d842f1c8b5
=======
date: 2021-03-09
>>>>>>> b32b96f0db419a073544550b861cd41897c8409a
homepage: https://github.com/ryanfox1985/OctoPrint-Youtube-Timelapse
source: https://github.com/ryanfox1985/OctoPrint-Youtube-Timelapse
archive: https://github.com/ryanfox1985/OctoPrint-Youtube-Timelapse/archive/master.zip
tags:
- youtube
- timelapse
- oAuth
- google

screenshots:
- url: /assets/img/plugins/youtube_timelapse/configuration_step7.png
  alt: Main plugin screenshot
  caption: Main plugin screenshot

featuredimage: /assets/img/plugins/youtube_timelapse/configuration_step7.png

compatibility:
  octoprint:
  - 1.5.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=3,<4"

---

# OctoPrint-Youtube-Timelapse

Automatically upload rendered timelapses to Youtube. Can also delete after upload to save space on the Raspberry Pi
SD Card. In order for the plugin to work properly you will have to create a Google OAuth App to authorize access. To create your own Google OAuth app please follow the directions outlined in the [Prerequisites](https://github.com/ryanfox1985/OctoPrint-Youtube-Timelapse#prerequisites).

## Configuration

Once the [Prerequisite](https://github.com/ryanfox1985/OctoPrint-Youtube-Timelapse#create-a-google-oauth-app) are met and you have downloaded your client_secrets.json file follow the steps [here](https://github.com/ryanfox1985/OctoPrint-Youtube-Timelapse#configuration) to authorize the plugin to your newly created OAuth app.

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.
