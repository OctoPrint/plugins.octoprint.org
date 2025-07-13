---
layout: plugin

id: remote_connection
title: OctoPrint-Remote_connection
description: Connect to devices attached to another host via Serial over IP
authors:
- Malte Starostik
license: AGPL-3.0-or-later

date: 2025-07-13

homepage: https://github.com/mstarostik/OctoPrint-Remote_connection
source: https://github.com/mstarostik/OctoPrint-Remote_connection
archive: https://github.com/mstarostik/OctoPrint-Remote_connection/archive/main.zip

follow_dependency_links: false

tags:
- connection
- network

screenshots:
- url: /assets/img/plugins/remote_connection/settings.png
  alt: Remote Connection Settings
  caption: Remote Connection Settings
- url: /assets/img/plugins/remote_connection/connecting.png
  alt: Connection Widget With Remote Connection
  caption: Connection Widget With Remote Connection
- url: /assets/img/plugins/remote_connection/connection_established.png
  alt: Remote Connection Established
  caption: Remote Connection Established

featuredimage: /assets/img/plugins/remote_connection/settings.png

compatibility:
  python: ">=3,<4"

attributes: []

---

If you want to connect to a device connected to a different machine than you run OctoPrint on, this plugin is for you. You can add remote connections to the serial ports OctoPrint knows about and thus transparently access such a device as if it was plugged into your OctoPrint machine.
