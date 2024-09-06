---
layout: plugin

id: ngrok
title: Ngrok Tunnel
description: A plugin to securely access your OctoPrint instance remotely through ngrok
author: fieldOfView
license: AGPLv3

date: 2020-06-23

homepage: https://github.com/fieldOfView/OctoPrint-ngrok
source: https://github.com/fieldOfView/OctoPrint-ngrok
archive: https://github.com/fieldOfView/OctoPrint-ngrok/archive/master.zip

tags:
- remote access
- authentication
- security
- password
- ngrok
- tunnel
- ssl

screenshots:
- url: /assets/img/plugins/ngrok/ngrok_navbar.png
  alt: Ngrok Tunnel navbar
  caption: The Ngrok Tunnel navbar item has shortcuts to the tunnel as well as settings and the ngrok dashboard.
- url: /assets/img/plugins/ngrok/ngrok_settings.png
  alt: Ngrok Tunnel settings
  caption: The Ngrok Tunnel settings page shows the status of the connection with ngrok.
- url: /assets/img/plugins/ngrok/ngrok_dashboard.png
  alt: ngrok dashboard
  caption: The ngrok dashboard is where you get the authtoken, and where you find the url of the active tunnel.

featuredimage: /assets/img/plugins/ngrok/ngrok_navbar.png

compatibility:

  os:
  - linux
  - windows
  - macos

  python: ">=2.7,<4"

  octoprint:
  - 1.4.0

attributes:
- cloud

---
This plugin creates a secure tunnel to access OctoPrint remotely. It provides a more secure alternative to using port forwarding to expose your OctoPrint instance to the internet.

Forwarding a port and setting up a dynamic dns record unfortunately remains a popular way to make an OctoPrint instance accessible through the internet. This is very insecure (especially when not using HTTPS with a proper certificate), and requires changes to the local network (static IP for the OctoPrint instance, configuration changes to the router). The truly safe way to access an OctoPrint instance is to use a VPN, but this is hard to set up and properly configure.

The OctoPrint Ngrok Tunnel plugin sets up a secure tunnel to your OctoPrint instance via the [ngrok](https://ngrok.com) service. The tunnel is encrypted with SSL and proper certificates (even if your OctoPrint instance is not accessible via HTTPS locally), and is further protected with Basic Authentication (username and password) out of the box.

There is no configuration of the local network necessary, and there are no ports to open or forward. No certificates to set up, and no changes to make to HAProxy. Just full access to your OctoPrint instance, including both the web interface and the API, from anywhere in the world. With the standard OctoPi confguration, you even get a working webcam stream remotely (if your home internet connection can keep up with the demands of streaming mjpeg).

You only need to sign up for a free account at [ngrok.com](https://ngrok.com). There is one caveat: with a free account, you get assigned a random subdomain of ngrok.com, and this subdomain changes each time OctoPrint gets restarted. The tunnel address is shown within the OctoPrint interface, but it can also be looked up in the [ngrok service dashboard](https://dashboard.ngrok.com/status/tunnels). With a paid ngrok account, you can configure a static subdomain to use. A paid plan gives you additional features, such as using more than one tunnel (printer) and creating an IP whitelist to limit who can access the tunnel.

## Configuration

The Ngrok Tunnel plugin can be configured via the OctoPrint settings panel.

The ngrok **auth token** is used to authenticate you on the ngrok service and can be found by logging in to the [ngrok dashboard](https://dashboard.ngrok.com/auth/your-authtoken). Though not strictly required for an ngrok tunnel, the plugin requires you to set up Basic Authentication on the tunnel in addition to the access control already set up on your OctoPrint instance. Any username and password combination can be chosen, but it is recommended to use a different username and password than your OctoPrint credentials. If you wish, you *can* use the same username and password you use for logging in to OctoPrint and have the login to the tunnel automatically log you in to OctoPrint too.

## Disclaimer

The authors of the plugin have no affiliation with [ngrok](https://ngrok.com). The plugin uses [pyngrok](https://github.com/alexdlaird/pyngrok) by Alex Laird to setup and manage ngrok tunnels.

Security is a serious topic, especially when there's a 3d printer involved. This plugin is provided "as is", without warranty of any kind. In no event shall the authors be liable for any claim, damages or other liability arising from, out of or in connection with the plugin or the use or other dealings in the plugin.
