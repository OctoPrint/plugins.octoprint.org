---
layout: plugin

id: HeaderAnnouncements
title: OctoPrint-HeaderAnnouncements
description: Add an announcement to the header of your octoprint install for use in a shared environment
authors:
- Sean Smith
  license: MIT

date: 2021-09-12

homepage: https://github.com/wwsean08/OctoPrint-HeaderAnnouncements
source: https://github.com/wwsean08/OctoPrint-HeaderAnnouncements
archive: https://github.com/wwsean08/OctoPrint-HeaderAnnouncements/archive/master.zip

tags:
- alert
- navbar
- notification
- notifications
- ui

screenshots:
- url: /assets/img/plugins/HeaderAnnouncements/announcement.png
  alt: An example announcement below the navbar full of lorem ipsum text
  caption: An example notification
- url: /assets/img/plugins/HeaderAnnouncements/settings.png
  alt: The settings page for OctoPrint-HeaderAnnouncements
  caption: The settings page for OctoPrint-HeaderAnnouncements

featuredimage: /assets/img/plugins/HeaderAnnouncements/announcement.png

compatibility:
  octoprint:
  - 1.4.0
  python: ">=3,<4"

---

## Overview

This plugin is useful for shared environments like a maker space, lab, university, etc. where there may be many users and you need a way for people to see announcements and information when using OctoPrint about upcoming maintenance, changes in policies, or other important information.
