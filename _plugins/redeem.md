---
layout: plugin
    
id: redeem
title: OctoPrint Redeem
description: Control Redeems configuration
author: Elias Bakken
license: AGPLv3
    
# today's date in format YYYY-MM-DD, e.g.
date: 2016-04-26
    
homepage: http://wiki.thing-printer.com/index.php?title=Main_Page
source: https://github.com/eliasbakken/octoprint_redeem
archive: https://github.com/eliasbakken/octoprint_redeem/archive/master.zip
    
# set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
follow_dependency_links: false
    
tags:
- redeem
- replicape
- firmware
- control

screenshots: 
- url: http://www.thing-printer.com/wp-content/uploads/2016/04/octoprint-redeem.png
  alt: OctoPrint Redeem
  caption: Settings page for OctoPrint Redeem

featuredimage: http://www.thing-printer.com/wp-content/uploads/2016/04/octoprint-redeem.png

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.8
---
    
The OctoPrint Redeem plugin enables choosing printer configuration for Redeem directly from OctoPrint. 
Redeem is the firmware for Replicape, and although it can be configured on the command line, it might be better 
to simply download the configuration file, edit it on a local computer and upload it. All of this can be done 
directly form the settings window using this plugin. 
