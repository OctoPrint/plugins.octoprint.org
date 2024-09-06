---
layout: plugin

id: thingiverse_downloader
title: Thingiverse Downloader
description: Download and extract a thing from Thingiverse to your Octoprint instance
authors:
  - Lucas Bock
license: MIT

date: 2021-09-10

homepage: https://github.com/appdevelopmentandsuch/Thingiverse-Downloader
source: https://github.com/appdevelopmentandsuch/Thingiverse-Downloader
archive: https://github.com/appdevelopmentandsuch/Thingiverse-Downloader/archive/main.zip

tags:
  - thingiverse
  - 3d models

featuredimage: /assets/img/plugins/thingiverse_downloader/demo.png

compatibility:
  octoprint:
    - 1.3.5

  python: ">=3,<4"

attributes:
- cloud
---

![Thingiverse-Downloader-Demo](/assets/img/plugins/thingiverse_downloader/demo_url.gif)
![Thingiverse-Downloader-Demo](/assets/img/plugins/thingiverse_downloader/demo_id.gif)

## Setup

### Quick Install

![Thingiverse-Downloader-Install](/assets/img/plugins/thingiverse_downloader/install.gif)

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/appdevelopmentandsuch/Thingiverse-Downloader/archive/main.zip

1. Install one of the following in order to view / upload STL files to your Octoprint instance.
   - [Octoprint-Slic3r](https://plugins.octoprint.org/plugins/slic3r/)
   - [STL Viewer](https://plugins.octoprint.org/plugins/stlviewer/)
   - [Cura Legacy](https://plugins.octoprint.org/plugins/curalegacy/)
   - [Full-featured Slicer](https://plugins.octoprint.org/plugins/slicer/)
2. Install the Thingiverse-Downloader plugin either from the Plugin manager, or manually.
3. Acquire an API key from the Thingiverse Developer Console (tutorial to come).

## Configuration

| Settings           | Description                                                                                                                |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| _API Key_          | An API key / App Key acquired from the Thingiverse Developer Console found [here](https://www.thingiverse.com/developers). |
| _Output Directory_ | The desired directory you wish to have the Thingiverse thing downloaded to. Recommend using `models`                       |
