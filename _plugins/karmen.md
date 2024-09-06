---
layout: plugin

id: karmen
title: Karmen Connector
description: Secured 3D printer monitoring and sharing. G-codes and user management. Schedule print jobs, view print history and timelapse videos. FREE!
authors:
- Pavel Vojacek
license: MIT

date: 2022-08-15

homepage: https://github.com/fragaria/karmen-octoprint-plugin
source: https://github.com/fragaria/karmen-octoprint-plugin
archive: https://github.com/fragaria/karmen-octoprint-plugin/archive/refs/heads/main.zip

privacypolicy: https://karmen.tech/documents/fragaria-privacy-policy.pdf

tags:
- remote access
- remote camera
- remote app
- remote printing
- monitor
- monitoring
- remote
- control
- phone
- plugin support
- webcam
- free
- secure
- safe
- cloud printing
- notifications
- snapshots
- alert
- progress
- status
- live streaming
- streaming
- sharing
- twitter
- print status

featuredimage: /assets/img/plugins/karmen/versionA.png

compatibility:
  octoprint:
  - 1.4.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=3,<4" # Python 3 only

attributes:
- cloud
- commercial
- free-tier

---

Karmen
===

It's a breeze to install the Karmen plugin. With Karmen, you'll have access to your Octoprint-powered printer from anywhere in the world. Plan, launch, review and share print files and videos over a secured interface (web, mobile, tablet). And Karmen is absolutely free!

![Karmen GUI](/assets/img/plugins/karmen/versionB.png)

Karmen features:

- ***Security:*** Encrypted access to Octoprint from anywhere in the world.
- ***Printer control from a single interface:*** Manage and monitor one or more 3D printers from a single application.
- ***G-codes management:*** Cloud storage for print files with the ability to search and sort into folders.
- ***Application:*** A modern application optimized for all devices (computer, mobile, tablet).
- ***Live video:*** Watch your print in progress and stop the printer if something goes wrong.
- ***Time-lapse:*** Karmen makes a record of the print for review and sharing with others.
- ***Teamwork:*** Share your 3D printers and print files with friends and colleagues.
- ***Upload G-codes from any slicer:*** Send print jobs from your slicer (Slic3r, PrusaSlicer, Cura) straight to Karmen.
- ***History:*** Keep track of who printed what and when.
- **Automatic Error Detection:** Karmen features artificial intelligence that diligently monitors the printing process via webcam.
- **G-code previews:** This function enables you to find the correct print job and preview the final print, identifying errors like missing support structures.

Configuration and documentation
---

It's easy to connect your printer in a few short steps:

- Install the Karmen Connector plugin.
- Create an account on [next.karmen.tech](https://next.karmen.tech/).
- Create an Octoprint secondary API key.
- Add your printer(s) to your Karmen workspace.

We've got detailed instructions in our video [documentation](https://karmen.tech/en/docs/karmen-connector-octoprint-plugin) and in video tutorial
{% include youtube.html vid="UTc_Iv4nHaI" preview="<preview image, 'assets/img/plugins/karmen/how_to_connect_youtube.png'>" %}.

Contacts, support and social media
---

- <https://karmen.tech>
- <karmen@karmen.tech>
- <https://www.facebook.com/karmen3D>
- <https://twitter.com/Karmen3D>
- <https://www.instagram.com/karmen3d/>

Karmen is developed and maintained with love in Prague by [Fragaria](https://fragaria.cz/).

Pictures
---

![Karmen GUI](/assets/img/plugins/karmen/versionA.png)

![Print dialog](/assets/img/plugins/karmen/printdialog.png)

![Printer detail](/assets/img/plugins/karmen/printerdetail.png)

Security and privacy policy
---

Security is a key concern for us. You can rest assured that your device's public address will not be exposed when using this plugin. Communication between Karmen and your Octoprint installation is made using a secure WebSocket channel protected by the HTTPS protocol used by banks, online stores and many more organizations.

Karmen also uses key exchange to make sure it's speaking to the expected device on the other end of the line. The key set is established during the initial setup.

By connecting your Octoprint installation to the Karmen Cloud, you confirm that you understand Karmen Cloud will acquire full control over your device. We guarantee that information about you or about your printers will never be sold or shared to any third party.

Karmen shares basic information with the following parties in order to improve our services and website user experience in general:

- Google Analytics - tracks our website visits and provides statistics
- Stripe - payment provider
- Facebook pixel - website visit statistics and information about traffic sources
- Sentry - helps us analyze and track errors

Of course if you'd like to completely delete your account and all data from Karmen Cloud, we'll do so immediately upon your request.

API key security
---

Never share your keys with ANYONE.

Please follow our guidelines and do not use the primary Octoprint key when setting up the Karmen plugin. Instead you should create a special key for that purpose, as recommended in our tutorial. The full procedure, including the recommended way of creating your API key, can be found at <https://karmen.tech/en/docs/karmen-connector-octoprint-plugin>.
