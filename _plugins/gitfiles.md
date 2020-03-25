---
layout: plugin
id: gitfiles
title: OctoPrint-GitFiles
description: Use a github repository for keeping your OctoPrint Files collection up-to-date.
author: OutsourcedGuru
license: MIT
date: 2018-09-29
homepage: https://github.com/OutsourcedGuru/OctoPrint-GitFiles
source: https://github.com/OutsourcedGuru/OctoPrint-GitFiles
archive: https://github.com/OutsourcedGuru/OctoPrint-GitFiles/archive/master.zip
tags:
- change management
- source control
- github
- git
- file manager

screenshots:
- url: https://user-images.githubusercontent.com/15971213/45835939-45777700-bcc0-11e8-80c6-2bc31e08f3ec.png
  alt: Settings screen
  caption: Settings
- url: https://user-images.githubusercontent.com/15971213/45719691-396fa600-bb56-11e8-9e71-d0d51c58ce4a.png
  alt: Github - new repository
  caption: Create a repository in Github for your gcode files
- url: https://user-images.githubusercontent.com/15971213/45836320-5c6a9900-bcc1-11e8-92eb-3b0b20292e54.png
  alt: Button in Files side panel
  caption: Click the button in the Files side panel

featuredimage: https://user-images.githubusercontent.com/15971213/45835939-45777700-bcc0-11e8-80c6-2bc31e08f3ec.png

compatibility:
  octoprint:
  - 1.3.9
  os:
  - linux
  - macos
  - freebsd

---

With this plugin, you can use a github repository for keeping your OctoPrint Files collection up-to-date. Publish your sliced files from a local repository on your workstation, then select to pull the latest from this github repository.