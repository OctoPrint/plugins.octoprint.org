---
layout: plugin

id: touchui
title: TouchUI
description: A touch friendly interface for Mobile and TFT touch modules
author: Paul de Vries
license: AGPLv3
date: 2015-10-10

homepage: https://billyblaze.github.io/OctoPrint-TouchUI
source: https://github.com/BillyBlaze/OctoPrint-TouchUI
archive: https://github.com/BillyBlaze/OctoPrint-TouchUI/archive/master.zip
follow_dependency_links: false

tags:
- ui
- touchscreen
- mobile

screenshots:
- url: https://billyblaze.github.io/OctoPrint-TouchUI/images/screenshot1.png
  alt: Control tab
  caption: Control tab
- url: https://billyblaze.github.io/OctoPrint-TouchUI/images/screenshot2.png
  alt: Terminal tab
  caption: Terminal tab
- url: https://billyblaze.github.io/OctoPrint-TouchUI/images/screenshot3.png
  alt: TouchUI Settings
  caption: TouchUI Settings

featuredimage: https://billyblaze.github.io/OctoPrint-TouchUI/images/touchuisample.png

compatibility:
  # list of compatible versions, for example 1.2.0. If left empty no specific version requirement will be assumed
  octoprint:
  - 1.2.6+
---
This plugin will transform the OctoPrint layout into a Mobile/TFT friendly layout. With larger buttons and a responsive layout down to the smallest resolution possible. It will mimic pointer events as touch, so you can hook up those touchscreens. It also supports a virtual keyboard.

All these settings are set client-side, so we won't interfere with other clients. All settings are stored in your localstorage or as a delicious cookie. You can find the `TouchUI settings` in a dedicated modal. Remember they're stored on your device, so if you login with your desktop computer you won't get the touch interface.

![TouchUI Interface](https://billyblaze.github.io/OctoPrint-TouchUI/images/touchui-v030.gif)

- **Touchscreens**  
Read more about [setting up a touchscreen](https://github.com/BillyBlaze/OctoPrint-TouchUI/wiki/Setup#raspberrypi--touchscreen) on our Wiki.

## Configuration
The interface will automatically start when your browser is smaller then 980 pixels in width or if you're browsing with a touch device. You can turn this manually on and off in the ``TouchUI settings`` modal. Alternatively you can force TouchUI to load by adding ``#touch`` on the end of your URL.

Read more [configuration options](https://github.com/BillyBlaze/OctoPrint-TouchUI/wiki/Configuration) on our Wiki.

- **Customization**  
You can change 4 main colors of the interface with the power of LESS. If you would like to change more colors, then you're free to add your own LESS file. [Read more about this and the variables](https://github.com/BillyBlaze/OctoPrint-TouchUI/wiki/Customize:-Use-your-own-file) on our wiki.
