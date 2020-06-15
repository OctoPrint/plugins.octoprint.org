---
layout: plugin

id: homeassistant
title: HomeAssistant Discovery
description: Automatically add your OctoPrint server to Home Assistant with MQTT
author: Clifford Roche
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2020-06-14

homepage: https://github.com/cmroche/OctoPrint-HomeAssistant
source: https://github.com/cmroche/OctoPrint-HomeAssistant
archive: https://github.com/cmroche/OctoPrint-HomeAssistant/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- notification
- iot
- automation
- mqtt

screenshots:
- url: /assets/img/plugins/homeassistant/hassio.png
  alt: HomeAssistant Device
  caption: HomeAssistant Device

featuredimage: /assets/img/plugins/homeassistant/hassio.png
      
---

Enable MQTT based discovery of your OctoPrint server with Home Assistant.

You will also need the OctoPrint-MQTT plugin installed and configured to connected to your Home Assistant MQTT service, and MQTT discovery enabled (should be the default). With these, by using the OctoPrint-HomeAssistant plugin your OctoPrint instance will automatically register a device and several sensors to follow your printer status, printing and slicing progress.
