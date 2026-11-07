---
layout: plugin

id: uploadmanagertab
title: Upload Manager Tab
description: Shows OctoPrint's bundled Upload Manager in its own tab instead of a pop-up, with layout, column and hidden file settings
authors:
- Shell M. Shrader
license: AGPLv3

date: 2026-11-07

homepage: https://github.com/synman/OctoPrint-UploadManagerTab
source: https://github.com/synman/OctoPrint-UploadManagerTab
archive: https://github.com/synman/OctoPrint-UploadManagerTab/archive/main.zip

tags:
- files
- ui
- upload
- tab

screenshots:
- url: /assets/img/plugins/uploadmanagertab/tab.png
  alt: The Upload Manager in its own tab
  caption: Your print files in a tab, with nothing covering the page
- url: /assets/img/plugins/uploadmanagertab/settings.png
  alt: The Upload Manager Tab settings
  caption: Choose the layout, the columns and which names to hide

featuredimage: /assets/img/plugins/uploadmanagertab/tab.png

compatibility:
  octoprint:
  - 1.11.0
  python: ">=3.7,<4"

attributes:
- ai-developed

---

OctoPrint's bundled Upload Manager opens as a pop-up over the page. This plugin moves that same window into its own
**Upload Manager** tab, so your print files stay one click away. It adds no new file features: printing, moving and
removing files all work the way OctoPrint already does them.

## What it does

- Shows the bundled Upload Manager in a tab, with nothing covering the page
- Stretches the file list to fill the tab across, down, or both
- Hides names you never want to see, such as `@eaDir` on a NAS share, using simple patterns
- Reopens your last folder and list style when you come back
- Shows or hides the Uploaded, Last Printed and Size columns
- Grays or hides the Files panel's folder icon

Find the settings under **Settings > Upload Manager Tab**.

## Requirements

OctoPrint 1.11.0 or newer with the bundled Upload Manager plugin enabled. Tested on OctoPrint 1.11.8 and 2.0.0rc5.
