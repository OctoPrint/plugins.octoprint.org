---
layout: plugin

id: tabinfo
title: TabInfo
description: display print information as browser tab title
authors:
- Daniel Dakhno
license: your plugin's license

# today's date in format YYYY-MM-DD, e.g.
date: 2024-05-16

homepage: https://github.com/dakhnod/OctoPrint-TabInfo
source: https://github.com/dakhnod/OctoPrint-TabInfo
archive: https://github.com/dakhnod/OctoPrint-TabInfo/archive/master.zip

# Set this if your plugin heavily interacts with any kind of cloud services.
#privacypolicy: your plugin's privacy policy URL

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- information
- progress
- tab
- browser
- overview

screenshots:
- url: /assets/img/plugins/tabinfo/banner.png
  alt: plugin preview in browser
  caption: plugin preview in browser

featuredimage: /assets/img/plugins/tabinfo/banner.png

compatibility:
  python: ">=2.7,>=3" # Python 2 & 3

---

# OctoPrint-TabInfo

TabInfo shows information about your print in the browser tab.
The information displayed can be changed using format strings.


## Configuration

The plugin can be configured in OctoPrint's settings using format strings.
Currently, two format strings can be defined, one for the Printing state and one for Idle state.
The format string can be any text. everything inside curly brackets is replaced by it's value in a data object.
That data object can be printed to the browsers developer console by ticking the checkbox.
In Chrome, the developer console can be accessed by pressing F12.

Two special cases are relevat:
- when the path points to a zero-argument function, the function is called and the result is used
- when the path points to a float, the value is floored. For instance, 1.123 would become 1
