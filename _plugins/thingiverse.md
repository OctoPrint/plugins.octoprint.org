---
layout: plugin

id: Thingiverse
title: OctoPrint-Thingiverse
description: This plugin creates a new tab where Thingiverse website is embedded.
author: stefancandrea
license: AGPLv3

date: 2019-10-28

homepage: https://github.com/stefancandrea/OctoPrint-Thingiverse/
source: https://github.com/stefancandrea/OctoPrint-Thingiverse/
archive: https://github.com/stefancandrea/OctoPrint-Thingiverse/archive/master.zip

tags:
- Thingiverse
- embedded website

compatibility:
  python: ">=2.7,<4"

screenshots:
- url: /assets/img/plugins/thingiverse/thingiverse_tab.jpg
  alt: Thingiverse Tab
  caption: ThingiverseTab
- url: /assets/img/plugins/thingiverse/thingiverse_settings.jpg
  alt: Thingiverse Settings
  caption: ThingiverseSettings
  
---

# OctoPrint-Thingiverse

**UPDATE 2020.08.13**

The plugin will no longer work. This is left here as a reminder for someone who will build a new Octoprint Thingiverse Plugin directly from the Thingiverse API.
This is why the plugin doesn't work anymore, and the Thingiverse team does not allow me to run this plugin inside an iframe, because then have an API.

So maybe if someone has time and is willing to build such a thing, that will be great.

This repository is open for everyone, for then mentioned task.


**Description**

This plugin adds the ability to browse Thingiverse website from OctoPrint. 
A lot of people use Thingiverse website for their 3D model portfolio, but they need 
to change windows all the time (ALT+TAB).

**No more!**

Now you can search 3D models inside your OctoPrint environment.

**Tip:**
If you have Slic3r or Cura engine plugin, all you need is your OctoPrint. No browser, no external slicing engines. 

**Search the model** > **Download**  > **Open zip file** > **Drag&Drop .stl file** > **Print!**.

Here is a [YouTube Video](https://www.youtube.com/watch?v=0I_BIR36Grk) that can help you install the latest Slic3r slicer including 3d representation of the model.

## Screenshots

![screenshot](/assets/img/plugins/thingiverse/thingiverse_tab.jpg)
![screenshot](/assets/img/plugins/thingiverse/thingiverse_settings.jpg)

## Install

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html) or manually using this URL:
    ```
        https://github.com/stefancandrea/OctoPrint-Thingiverse/archive/master.zip
    ```
## Setup

Once installed go into OctoPrint Settings > Thingiverse where you can enable/disable this function and follow a small guide for a cleaner and ergonomic view of the website.   

## Disclaimer

This plugin adds a tab to the OctoPrint interface that loads the Thingiverse website within an iframe.

The Thingiverse website is copyright, trademark, and owned by MakerBot Industries, LLC, see their [T&C](https://www.makerbot.com/legal/terms/) for additional information regarding the use of their website and service(s).

The author of this plugin is not responsible for any malicious action regarding MakerBot Industries, LLC property.

### Support the effort
If you found this plugin useful you can support it's creator. 
Thank you.

[![paypal](/assets/img/plugins/thingiverse/paypal-support.png)](https://paypal.me/stefancandrea)
