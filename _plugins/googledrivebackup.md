---
layout: plugin
id: googledrivebackup
title: Google Drive Backup
description: This plugin will automatically save a copy of your OctoPrint backup to Google Drive upon completion.
author: jneilliii
license: MIT
date: 2020-09-21
homepage: https://github.com/jneilliii/OctoPrint-GoogleDriveBackup
source: https://github.com/jneilliii/OctoPrint-GoogleDriveBackup
archive: https://github.com/jneilliii/OctoPrint-GoogleDriveBackup/archive/master.zip
tags:
- Google Drive
- Backup
- OAuth
screenshots:
- url: /assets/img/plugins/googledrivebackup/configuration_step2.png
  alt: Configuration Step 2
  caption: Upload client_secrets.json file.
- url: /assets/img/plugins/googledrivebackup/configuration_step6.png
  alt: Configuration Step 6
  caption: Authenticate client secrets file.
- url: /assets/img/plugins/googledrivebackup/configuration_step7.png
  alt: Configuration Step 7
  caption: Google Drive Backup is active.
featuredimage: /assets/img/plugins/googledrivebackup/configuration_step7.png
compatibility:
  octoprint:
  - 1.5.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=2.7,<4"

---

# Google Drive Backup

This plugin will automatically upload a backup upon completion to your authorized Google Drive. In order for the plugin to work properly you will have to create a Google OAuth App to authorize access. To create your own Google OAuth app please follow the directions outlined in the [Prerequisites](https://github.com/jneilliii/OctoPrint-GoogleDriveBackup#create-a-google-oauth-app).

## Configuration

Once the [Prerequisite](https://github.com/jneilliii/OctoPrint-GoogleDriveBackup#create-a-google-oauth-app) are met and you have downloaded your client_secrets.json file follow the steps [here](https://github.com/jneilliii/OctoPrint-GoogleDriveBackup#configuration) to authorize the plugin to your newly created OAuth app.

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](/assets/img/plugins/googlegrivebackup/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/googlegrivebackup/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
