---
layout: plugin

id: consolidatedtabs
title: Consolidated Tabs
description: Combines configured tabs into a single tab as draggable and resizable panels.
author: jneilliii
license: AGPLv3

date: 2020-07-26

homepage: https://github.com/jneilliii/OctoPrint-ConsolidatedTabs
source: https://github.com/jneilliii/OctoPrint-ConsolidatedTabs
archive: https://github.com/jneilliii/OctoPrint-ConsolidatedTabs/archive/master.zip

tags:
- tab
- widescreen

featuredimage: /assets/img/plugins/consolidatedtabs/screenshot_tab.png

compatibility:
  octoprint:
  - 1.2.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=2.7,<4"

---

# Consolidated Tabs

This plugin will allow you to combine the selected tabs into a single tab as draggable and resizable panels.

![screenshot tab](/assets/img/plugins/consolidatedtabs/screenshot_tab.png)

**Note:** Initial positioning and sizing can be a little tricky due to the snapping feature between panels. You may have to move/resize and refresh the page a couple of times to get everything perfectly aligned. Once you're happy with the positions and sizes you should not have to mess with them again.

## Settings

![screenshot settings](/assets/img/plugins/consolidatedtabs/screenshot_settings.png)

* Combined Tabs Order: all the tabs that will be combined into one tab as draggable and resizable panels.
* Uncombined Tabs: tabs that have not been combined and will remain as their own tab.
* Resize Navbar: whether to resize the width of the top navbar to 100% or not.
* Remove Tab Name: don't show the name of the consolidated tab, only possible if all tabs are combined.
* Overall width: width to set the overall page container, useful for widescreen displays.
* Clear All Positions and Sizes: use the buttons to clear any position or size customizations, helpful when panels get moved off screen.

## To-Do
* [ ] Figure out how to get rid of the extra whitespace at the bottom of the page after panels are positioned.

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](/assets/img/plugins/consolidatedtabs/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/consolidatedtabs/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
