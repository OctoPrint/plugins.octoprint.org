---
layout: plugin

id: autoscroll
title: Autoscroll
description: Turn on/off terminal autoscroll when scrolling up/down
author: ovidiu
license: AGPLv3
date: 2016-06-27

homepage: https://github.com/MoonshineSG/OctoPrint-Autoscroll
source: https://github.com/MoonshineSG/OctoPrint-Autoscroll
archive: https://github.com/MoonshineSG/OctoPrint-Autoscroll/archive/master.zip
follow_dependency_links: false

tags:
- terminal
- autoscroll


compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.6


---

Turn on/off terminal autoscroll when scrolling up/down

- turns autoscroll off when scrolling up (rename button to "Now")
- turns autoscroll on when "Now" is pressed or scrolled to the end

Behaviour similar to "Console" application, the OSX log viewer.
