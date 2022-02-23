---
layout: plugin

id: MakerOS
title: MakerOS
description: An OctoPrint plugin integration with the MakerOS Platform API.
author: Thomas Lawton
license: AGPLv3

date: 2020-10-05

homepage: https://github.com/makeros3d/Octoprint-Makeros
source: https://github.com/makeros3d/Octoprint-Makeros
archive: https://github.com/makeros3d/Octoprint-Makeros/archive/master.zip

#follow_dependency_links: false

tags:
- api
- addon
- makeros
- files

screenshots:
- url: /assets/img/plugins/MakerOS/Octoprint-Makeros-projects.png
  alt: MakerOS Plugin Projects Access
  caption: MakerOS projects being accessed via OctoPrint
- url: /assets/img/plugins/MakerOS/Octoprint-Makeros-project.png
  alt: MakerOS Plugin Project Access
  caption: A MakerOS project being accessed via OctoPrint
- url: /assets/img/plugins/MakerOS/Octoprint-Makeros-settings.png
  alt: MakerOS Plugin Settings
  caption: The settings for the MakerOS plugin

featuredimage: /assets/img/plugins/MakerOS/Octoprint-Makeros-projects.png

---

This plugin requires a [MakerOS](https://makeros.com) business account. Please
note that there is no free subscription tier.

The official MakerOS OctoPrint plugin will allow you to interface with your
MakerOS projects from within OctoPrint. Once installed you will be able to query
your projects and download both .gcode and .STL files from your projects to your
OctoPrint instance.

On the initial call to the MakerOS API a MakerOS folder will be created in your
files. From there, upon downloading a file, a project specific folder will be
created for you within the MakerOS folder.

> Please note that downloading .STL files will require you to install the
CuraEngine Legacy plugin which can be installed in the same way as you installed
the MakerOS plugin.

Setting up the plugin is simple - you may install via the Plugin Manager or
manually using this URL: https://github.com/makeros3d/Octoprint-Makeros/archive/master.zip

Once the plugin is installed it is easily configurable via the plugin's settings
in the settings menu. All that you'll need are your MakerOS Provider ID, API
key, and API URL.
