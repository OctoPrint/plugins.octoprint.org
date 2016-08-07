---
layout: plugin

id: updatefix127
title: Updatefix 1.2.7
description: Fixes an issue in OctoPrint 1.2.7 that prevents updating
author: Gina Häußge
license: AGPLv3

date: 2015-12-07

homepage: https://github.com/OctoPrint/OctoPrint-Updatefix-1.2.7
source: https://github.com/OctoPrint/OctoPrint-Updatefix-1.2.7
archive: https://github.com/OctoPrint/OctoPrint-Updatefix-1.2.7/archive/master.zip

tags:
- fix

compatibility:
  octoprint:
  - ">=1.2.7,<1.2.8"
---

This plugin fixes an issue in OctoPrint 1.2.7's software updater, causing updates
of OctoPrint itself to fail.

The plugin monkey-patches the bug causing this issue with the same fix that is
present in 1.2.8, but only for the affected version 1.2.7.
Once version 1.2.8 (which ships with the fix) is detected, the plugin uninstalls
itself during startup utilizing the plugin manager.

## How does it work?

After installing the plugin and restarting, the plugin will check if you are
running OctoPrint version 1.2.7 or 1.2.8.

If you are running 1.2.7, it will apply the necessary fix to the loaded class 
of the Software Update Plugin during start-up of the server (via so called monkey 
patching). Once your server has started you may then update as usual.

If the plugin detects version 1.2.8 as running, it will uninstall itself
and restart the server (since it's not necessary any more).

If you are running neither 1.2.7 nor 1.2.8, the plugin will not do anything
but change its name and description to hint at the fact that it should be 
uninstalled.

Usually the process will look like the following:

1. You are running 1.2.7.
2. You install the plugin and are prompted to restart the server.
3. You restart the server.
4. You perform the update to 1.2.8. The server is restarted.
5. The plugin detects you are now running 1.2.8. It uninstalls itself and
   restarts the server.
6. You have a clean 1.2.8 install.
