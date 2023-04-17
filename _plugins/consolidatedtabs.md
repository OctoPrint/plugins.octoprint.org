---
layout: plugin

id: consolidatedtabs
title: Consolidated Tabs
description: Combines configured tabs into a single tab as draggable and resizable panels.
author: jneilliii
license: AGPLv3

date: 2020-08-06

homepage: https://github.com/jneilliii/OctoPrint-ConsolidatedTabs
source: https://github.com/jneilliii/OctoPrint-ConsolidatedTabs
archive: https://github.com/jneilliii/OctoPrint-ConsolidatedTabs/archive/master.zip

tags:
- tab
- widescreen
- style
- styling
- UI


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

This plugin will allow you to consolidate any OctoPrint tab into a single Consolidated Tab as a draggable and resizable panel. Click the screenshot below to see an example YouTube video. Since version 1.0.0 the plugin utilizes [gridstack.js](https://gridstackjs.com/) for positioning and sizing.

{% include youtube.html vid="1Qg6TIGGRB4" preview="/assets/img/plugins/consolidatedtabs/screenshot_tab.png" %}

## Settings

Click the screenshot below to open a YouTube video demonstrating setting up Consolidated Tabs.

{% include youtube.html vid="BuJJV-giFNc" preview="/assets/img/plugins/consolidatedtabs/screenshot_settings.png" %}

- **Resize Navbar:** whether to resize the width of the top navbar to 100% or not.
- **Remove Tab Name:** don't show the name of the consolidated tab, only possible if all tabs are consolidated.
- **Use Full Width of Browser:** if enabled the tab area will be sized to fit the entire width of the browser, and the sidebar will be moved to the left.
- **Enable Floating Panels:** if enabled the panels will not auto collapse into available open space. Can be helpful when panels are jumping around a lot.
- **Don't Show Instructions:** if enabled the instructions will not be displayed when enabling edit mode.
- **Don't Show Edit Button:** if enabled the edit button in the navbar will be hidden.

## Instructions

![screenshot_instructions](/assets/img/plugins/consolidatedtabs/screenshot_instructions.png)

## Tips

- The name of the tab will match what is configured in OctoPrint's `Title` appearance setting.
- It's best to consolidate the desired tabs first and save, reload, and then enable edit mode again to resize and position.
- Panels will become full width automatically and realign once the tab's area width drops below a certain size.

## Themeify

If using Themeify you may want to add extra settings to your Advanced options. These are the relevant css selectors that you can adjust.

{:.table}
| Selector                                               | CSS-Rule         | Value             | Context             | Hidden Tab Name Specific |
|--------------------------------------------------------|------------------|-------------------|---------------------|--------------------------|
| .grid-stack-item.consolidated .grid-stack-item-content | background-color | #2f3136           | Each Panel          |                          |
| .grid-stack-item.consolidated .grid-stack-item-content | border           | 1px solid #fc8003 | Panels Border       |                          |
| #tabs_content                                          | box-shadow       | unset             | Tab content wrapper | Yes                      |
| #tabs_content                                          | background-color | unset             | Tab content wrapper | Yes                      |

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](/assets/img/plugins/consolidatedtabs/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/consolidatedtabs/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
