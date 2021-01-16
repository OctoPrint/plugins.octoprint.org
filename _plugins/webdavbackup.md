---
layout: plugin
id: webdavbackup
title: WebDAV Backup
description: This plugin will automatically save a copy of your OctoPrint backup to a WebDAV server upon completion.
author: edekeijzer
license: MIT
date: 2020-12-10
homepage: https://github.com/edekeijzer/OctoPrint-WebDavBackup
source: https://github.com/edekeijzer/OctoPrint-WebDavBackup
archive: https://github.com/edekeijzer/OctoPrint-WebDavBackup/archive/master.zip
tags:
- Backup
- WebDAV
- Nextcloud
- OwnCloud
screenshots:
- url: /assets/img/plugins/webdavbackup/configuration_screen.png
  alt: Configuration screen
  caption: Configuration screen for the plugin with Nextcloud config.
- url: /assets/img/plugins/webdavbackup/nextcloud_content.png
  alt: Upload result
  caption: The resulting content in Nextcloud.
featuredimage: /assets/img/plugins/webdavbackup/configuration_screen.png
compatibility:
  octoprint:
  - 1.5.0
  python: ">=3,<4"

---

# WebDAV Backup

This plugin will automatically upload a backup upon completion to a WebDAV compatible storage server.

## Configuration

Please note that the password to connect to the WebDAV server will be stored in the OctoPrint configuration in plain text, so use an app specific password if possible. See documentation how to configure this for [Nextcloud](https://docs.nextcloud.com/server/latest/user_manual/en/session_management.html#device-specific-passwords-and-password-changes), [OwnCloud](https://doc.owncloud.com/server/user_manual/session_management.html#app-passwords)

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.