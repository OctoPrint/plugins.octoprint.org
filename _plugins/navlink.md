---
layout: plugin

id: navlink
title: Nav Link
description: Adds a button with a configurable link, label and icon (Font Awesome or your own uploaded image) to OctoPrint's top navigation bar.
authors:
- mikulik86
license: MIT

date: 2026-10-19

homepage: https://github.com/mikulik86/OctoPrint-NavLink
source: https://github.com/mikulik86/OctoPrint-NavLink
archive: https://github.com/mikulik86/OctoPrint-NavLink/archive/main.zip

tags:
- navbar
- ui
- link
- shortcut

screenshots:
- url: /assets/img/plugins/navlink/navbar.png
  alt: Nav Link button with a Font Awesome icon in the navbar
  caption: A link to Home Assistant with a Font Awesome icon
- url: /assets/img/plugins/navlink/navbar_image.png
  alt: Nav Link button with an uploaded image in the navbar
  caption: The same button with an uploaded SVG as its icon
- url: /assets/img/plugins/navlink/settings.png
  alt: Nav Link settings page
  caption: Settings

featuredimage: /assets/img/plugins/navlink/navbar.png

compatibility:
  octoprint:
  - 1.4.0
  python: ">=3.7,<4"

attributes:
- ai-developed

---

Adds a single button to OctoPrint's top navigation bar that links wherever you like: Home Assistant, a webcam
stream, your NAS, the printer's manual and so on.

Everything is configured in **Settings → Nav Link**:

- **URL** the button opens, optionally in a new tab
- **Label** next to the icon, or leave it empty for an icon-only button
- **Icon**: any [Font Awesome](https://fontawesome.com/search?ic=free) class, or an image you upload
  (PNG, JPG, GIF, WebP, SVG or ICO, up to 1 MB, shown 20 px tall)
- **Tooltip** shown on hover

The button previews changes live while you edit and only keeps them when you click Save.

Uploaded images are stored in the plugin's data folder and served by OctoPrint itself, so they also work offline
and over HTTPS. Uploading or removing the image requires the *Settings* permission.

The plugin doesn't contact any external service; the link is only opened by your browser when you click the button.
