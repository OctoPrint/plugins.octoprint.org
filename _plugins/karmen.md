---
layout: plugin

id: karmen
title: Karmen Connector
description: Securely integrate your OctoPrint with Karmen Cloud in just a few clicks and start managing your prints from anywhere around the globe.
authors:
- Pavel Vojacek
license: MIT

# today's date in format YYYY-MM-DD, e.g.
date: 2022-08-15

homepage: https://github.com/fragaria/karmen-octoprint-plugin
source: https://github.com/fragaria/karmen-octoprint-plugin
archive: https://github.com/fragaria/karmen-octoprint-plugin/archive/refs/heads/main.zip

privacypolicy: https://karmen.tech/documents/fragaria-privacy-policy.pdf

tags:
- remote access
- remote camera
- remote app
- remote printing
- monitor
- monitoring
- remote
- control
- phone
- plugin support
- webcam
- free
- secure
- safe
- cloud printing
- notifications
- snapshots
- alert
- progress
- status
- live streaming
- streaming
- sharing
- twitter
- print status

screenshots:
- url: /assets/img/plugins/karmen/karmen_screenshot.png
  alt: Karmen
  caption: Karmen Cloud

featuredimage: /assets/img/plugins/karmen/karmen_screenshot.png

compatibility:
  octoprint:
  - 1.4.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=3,<4" # Python 3 only

---

This plugin allows you to integrate your OctoPrint instance with [Karmen Cloud](https://karmen.tech/) — a cloud-based
solution for realtime control and monitoring of your prints.
It will grant you with these new superpowers:

- Securely view & manage your printers realtime from any place around the globe.
- Collaborate with others by using Karmen Cloud workspaces. Share your printers in a secure way. Extremely useful for home, office, schools and many other collaborative environments.
- Display live video stream of your printers using just a web browser.
- Record timelapse videos easily without any further config.
- View full print history of each of your printers, audit individual prints and their outcomes.
- Never get lost among your print files again: Karmen provides you with a personal Gcode repository with an advanced labeling system.
- This plugin will link your OctoPrint instance to the Karmen Cloud using a secure WebSocket channel protected by strong encryption. It will also provide it with an elevated permissions so that it will be able to control your printer remotely.
- Karmen Cloud will never use your OctoPrint data for anything besides extra features described above. It won't allow other Karmen Cloud users to access your OctoPrint or any related data unless you give them an explicit permission.

## Configuration

For configuration check [documentation](https://docs.karmen.tech/#/karmen-octo-plugin).

## Secure communication

Security is a key concern to us. Rest assured, your device public address will not be exposed when using this plugin. Rather, communication between Karmen and your Octoprint installation is made using a secure WebSocket channel protected by HTTPS protocol which is used by major organizations like eshops, banks and others.

Karmen also uses key exchange to ensure it speaks to the expected device on the other end. Key set is established during the initial setup.

## Privacy policy

We guarantee that information about you or about your printers will never be sold or even shared to any third party.

### Third party services

Karmen shares basic information with following parties in order to improve our services and website user experience in general:

- Google Analytics - tracks our website visits and provides statistics
- Stripe - payment provider
- Facebook pixel - website visit statistics and info about traffic sources
- Sentry - helps us analyze, track & report errors

### Deleting personal data

Should you decide to delete your Karmen account, all you need to do is to write a deletion request to karmen@karmen.tech. Our admins will delete all information about you, your account, your print files, print history as well as timelapse videos, printers and their configuration.

### Deleting general data

Should you decide to delete files stored under your user account, you can either do so using Karmen Cloud web app or by sending us an inquiry to karmen@karmen.tech

## Confirm you understand what will happen

By connecting your Octoprint installation to Karmen Cloud, you confirm you understand that Karmen Cloud will acquire full control over your device.

## API key security

- Never share your keys with ANYONE.
- Please follow our guidelines and do not use the primary Octoprint key when setting up the Karmen plugin. Rather, create a special key for that purpose as recommended in our tutorial. The full procedure including the recommended way of creating your API key can be found at <https://docs.karmen.tech/#/karmen-octo-plugin>

## Contacts & support

We’ll gladly answer all your questions or comments. Please get in touch at <karmen@karmen.tech>. Thank you for your interest and support!
