---
layout: plugin

id: crealitycloud
title: OctoPrint-CrealityCloud
description: A OctoPrint-Plugin that connect the Octoprint to Creality Could
authors:
- Creality
license: AGPLv3

date: 2021-11-08

homepage: https://github.com/crealitycloud/OctoPrint-CrealityCloud
source: https://github.com/crealitycloud/OctoPrint-CrealityCloud
archive: https://github.com/crealitycloud/OctoPrint-Crealitycloud/archive/master.zip

tags:
- Remote control
- Online slice
- Models Download
- file management
- Remote webcam

compatibility:

  octoprint:
  - 1.6.1

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=3,<4"
---
* # OctoPrint-Crealitycloud


![preview](/assets/img/plugins/OctoPrint-CrealityCloud/main.png)

  A OctoPrint-Plugin that connect the Octoprint to Creality Cloud
=======
  A OctoPrint-Plugin that connect the Octoprint to CrealityCloud

  ## Setup

  Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html) or manually using this URL:

  https://github.com/crealitycloud/OctoPrint-Crealitycloud/archive/master.zip

  **Crealitycloud plugin depends on the following two plugins：**

  - https://github.com/SimplyPrint/OctoPrint-Creality2xTemperatureReportingFix/archive/master.zip
  - https://github.com/OllisGit/OctoPrint-DisplayLayerProgress/releases/download/1.26.0/master.zip

  ## Configuration

  1、Make sure OctoPrint is up and running ,and Raspberry Pi is online. 
  2、Make sure the above three plugins are installed.
  3、In Octoprint select Setting->Crealitycloud Plugin->click botton to get bind code 
  ![Configuration](/assets/img/plugins/crealitycloud/1.png)
  4、In Creality Could APP select print->Add Device->choose Raspberry Pi 
  ![Configuration](/assets/img/plugins/crealitycloud/2.png)
  5、input code or scan QR Code 
  ![Configuration](/assets/img/plugins/crealitycloud/3.png)

  Then you can control your Octoprint on Creality Could APP！
