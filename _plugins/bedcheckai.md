---
layout: plugin

id: bedcheckai
title: OctoPrint-BedCheckAI
description: Detects the print bed in the camera frame. Useful for automation and smarter printing
authors:
- printpal.io
license: AGPLv3

date: 2023-09-18

homepage: https://printpal.io
source: https://github.com/printpal-io/OctoPrint-BedCheckAI
archive: https://github.com/printpal-io/OctoPrint-BedCheckAI/archive/master.zip

tags:
- ai
- ml
- detection
- automation
- macro
- free

screenshots:
- url: /assets/img/plugins/bedcheckai/tools.jpg
  alt: Bed Check AI detects any tools left on your print bed
  caption: Bed Check AI detects any tools left on your print bed
- url: /assets/img/plugins/bedcheckai/print.jpg
  alt: Bed Check AI detects any previous prints leftover on your print bed
  caption: Bed Check AI detects any previous prints leftover on your print bed


featuredimage: /assets/img/plugins/bedcheckai/tools.jpg


compatibility:
  octoprint:
  - 1.4.0
  os:
  - linux
  - windows
  - macos
  - freebsd
  python: ">=3.6,<4"

attributes:
- cloud

---

# Bed Check AI
Detect your print bed with the power of AI. This tool is great for automating your print process, or just a simple quality of life boost in your overall 3D printing experience.

### How does it work?
Bed Check AI uses a Deep Neural Network Segmentation model. The model determines which pixels within the image are associated with a print bed and then groups them together. The ML model is large so it is run on the cloud. When the BedCheck Macro/button is triggered, the current camera snapshot is sent to the cloud for ML inference and the various pixel values are returned. This allows for you to utilize the tool on any piece of hardware, from anywhere in the world.

The software compares the current bed detection to your set baseline, and using a loss function it calculates the similarity of the detected, based on this resulting 'loss' we can deduce whether the bed is clear or not.

The ML model approach is taken for a task such as this to account for dynamic settings - lighting, bed wear and tear, and many other factors in play during 3D printing.
### Watch the AI in action
The model detects anything on the bed - this can mean a leftover print, purge lines, or any tools left on the bed (blue handled-clippers we're looking at you).

![](/assets/img/plugins/bedcheckai/bedcheckai-demo.gif "OctoPrint Demo")

### Setup

1. Open the OctoPrint Web Inferface

2. Open the Settings using the 🔧 (wrench) icon in the top right header

3. Open the Plugin Manager in the left-side selection menu

4. Click on the "+ Get More" button

5. Search for BedCheckAI

6. Click Install on the BedCheckAI Plugin

7. Restart OctoPrint once Installation is completed

The full installation guide/quickstart can be found here: [QuickStart Guide](https://github.com/printpal-io/OctoPrint-BedCheckAI)

### Configuration

Once you have successfully installed Bed Check AI, you should configure the settings. To configure the settings:

1. Open the OctoPrint Web Inferface

2. Open the Settings using the 🔧 (wrench) icon in the top right header

3. Scroll down to the Plugin Settings in the left-side selection menu and select 'Bed Check AI'

Follow the setup guide on the official [GitHub](https://github.com/printpal-io/OctoPrint-BedCheckAI/wiki/Installation).


### Authentication

This plugin is completely free to use, the first 20 bed scans can be done immediately, but after that your account needs to be verified so we know that you are not a bot. In order to use create an account, visit [app.printpal.io](https://app.printpal.io) and register an account, verify the email, and use the API key provided in the settings page of the Web App.

# Privacy Policy
Read our privacy policy here: [PrintWatch Privacy policy](https://printpal.io/privacy/)

### Our Other Plugins
`PrintWatch AI monitoring & Remote Access` :
```
This plugin monitors your prints in real-time for defects and failures and notifies you and/or pauses the print so you save time, material, and gain peace of mind. This plugin also allows you to remotely view and manage your printer from anywhere in the world.
```
Check it out [here](https://plugins.octoprint.org/plugins/printwatch/)
