---
layout: plugin

id: customcss
title: OctoPrint-CustomCSS
description: Quickly add custom CSS to modify your OctoPrint UI.
authors:
- Neal Lambert
license: AGPLv3

date: 2020-12-10

homepage: https://github.com/crankeye/OctoPrint-CustomCSS
source: https://github.com/crankeye/OctoPrint-CustomCSS
archive: https://github.com/crankeye/OctoPrint-CustomCSS/archive/master.zip

tags:
- css
- settings

compatibility:
  python: ">=2.7,<4"

---
Add your CSS by navigating to Settings -> Plugins -> Custom CSS.

Originally developed to fix an issue with overly large thumbnails on mobile when using [PrusaSlicer Thumbnails](https://plugins.octoprint.org/plugins/prusaslicerthumbnails/) and [TouchUI](https://plugins.octoprint.org/plugins/touchui/) together.

<br/>
#### PrusaSlicer Thumbnails + TouchUI CSS Fixes
```
/* Fix PrusaSlicer Thumbnails size when using TouchUI  */
@media (max-width: 980px) {
  #touch .inline_prusa_thumbnail {
    max-width: 140px;
    margin-right: 10px;
    float: left;
  }
}

/* Optional: Make the file list taller (reccomended by PrusaSlicer Thumbnails)  */
#files > div > div.gcode_files > div.scroll-wrapper {
  min-height: 800px !important;
}
```
