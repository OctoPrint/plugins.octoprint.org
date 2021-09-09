---
layout: plugin

id: thingiverse_downloader
title: Thingiverse Downloader
description: Download and extract a thing from Thingiverse to your Octoprint instance
authors:
  - Lucas Bock
license: MIT

date: 2021-09-08

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
---

![Thingiverse-Downloader-Demo-URL](https://user-images.githubusercontent.com/22528729/132139046-1b1b4dc5-dfb8-4084-bb2d-1d3c27e53bb4.gif)
![Thingiverse-Downloader-Demo-ID](https://user-images.githubusercontent.com/22528729/132139044-446589ee-4ab9-4962-ac1d-04c991062782.gif)

## Setup

### Quick Install

![Thingiverse-Downloader-Install](https://user-images.githubusercontent.com/22528729/131595461-adb80ed1-4f57-4f24-ade5-fa84749ae93a.gif)

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/appdevelopmentandsuch/Thingiverse-Downloader/archive/main.zip

1. Install the [Octoprint-Slic3r](https://plugins.octoprint.org/plugins/slic3r/) plugin in order to view / upload STL files to your Octoprint instance.
2. Install the Thingiverse-Downloader plugin either from the Plugin manager, or manually.
3. Acquire an API key from the Thingiverse Developer Console (tutorial to come).

## Configuration

| Settings           | Description                                                                                                                |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| _API Key_          | An API key / App Key acquired from the Thingiverse Developer Console found [here](https://www.thingiverse.com/developers). |
| _Output Directory_ | The desired directory you wish to have the Thingiverse thing downloaded to. Recommend using `models`                       |
