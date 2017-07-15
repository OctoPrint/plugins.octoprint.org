---
layout: plugin

id: portlister
title: PortLister
description: Refreshes the port list in the browser when a printer shows up
author: Mark Walker
license: AGPLv3

date: 2015-10-08

homepage: https://github.com/markwal/OctoPrint-PortLister
source: https://github.com/markwal/OctoPrint-PortLister
archive: https://github.com/markwal/OctoPrint-PortLister/archive/master.zip

follow_dependency_links: false

tags:
- printer
- automatic

compatibility:
  os:
  - nix

---
Automatically notice when a new port is available for connecting.

Have you noticed that if you load up the OctoPrint web page when your printer is
off, the printer's port isn't in the list?  Then when you turn on the printer
you have to refresh the page to make it show up?  This plugin fixes that.

It watches for the device to appear (when you turn it on) and then notifies all
the web clients to refresh the list of ports.

It also (if you have autoconnect turned on), will automatically connect to the
printer (if the new port is the same as the one you've selected in connection
settings) after a reasonable (long) delay to wait for the printer to actually
come on.  The default delay is 20 secs.  It's settable in config.yaml, if
anybody uses this plugin besides me, I could be talked into a settings page.
