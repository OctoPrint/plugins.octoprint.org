---
layout: plugin

id: printwatch
title: Abort Failures - Printwatch
description: PrintWatch monitors your prints for defects in real-time and optimizes your 3D printers using Artificial Intelligence
author: printpal.io
license: AGPLv3

date: 2022-01-16

homepage: https://github.com/printpal-io/OctoPrint-Printwatch
source: https://github.com/printpal-io/OctoPrint-Printwatch
archive: https://github.com/printpal-io/OctoPrint-Printwatch/archive/master.zip

tags:
- AI
- Monitor
- Watch
- Shutoff
- Defect Detection
- Remote
- Access
- Cloud
- Remote monitoring
- Machine Learning
- alerts
- internet
- email
- notifications
- remote
- restart
- Optimize
- Analytics
- failure
- sms
- automation
- material
- save
- time


screenshots:
- url: /assets/img/plugins/printwatch/printwatch.png
  alt: PrintWatch monitors your prints with Artificial Intelligence and saves you time and material
  caption: PrintWatch monitors your prints with Artificial Intelligence
- url: /assets/img/plugins/printwatch/printwatch-notification.png
  alt: Get notified when something goes wrong with your print. Reduce downtime and loss
  caption: PrintWatch notifies you when something goes wrong. Let AI do the watching for you while you enjoy your day
- url: /assets/img/plugins/printwatch/printwatch-settings.png
  alt: Configurable settings allow you to customize how PrintWatch works for you.
  caption: Configure your settings the way you like.

featuredimage: /assets/img/plugins/printwatch/printwatch.png


compatibility:

  octoprint:
  - 1.3.2

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=2.7,<4"

---

# PrintWatch

PrintWatch uses Artificial Intelligence to monitor your 3D prints for any defects that begin to form. The plugin takes the video feed from any camera compatible with OctoPrint and runs it through a Machine Learning model that detects print defects in real-time. The plugin takes actions set by the user once a failure is positively detected that include:

- 📧 Email/SMS Notification
- ⏸ Pausing the print job
- 🔥 Turning off the Extruder Heat
- ⚙ Customized actions created by the user

PrintWatch saves time and material while also giving you peace of mind that your 3D print is printing properly. In addition to detecting defects, PrintWatch has an Anomaly Detection model running in the background that can detect slight changes or anomalies for printers in your fleet. Get notified early and schedule maintenance for the problematic printer, reducing downtime and costs. PrintWatch's Web App allows you to remotely view and manage all of your printers from anywhere in the world.
Current features include:

- Real-time defect detection
- Remote access and management
- Anomalous Printer Detection
- Advanced Analytics
- Resume Print

Upcoming features include:

- G-Code and Speed optimization with ML
- MultiCamming
- ROI selection and slicing
- Local Device

### Setup

1. Open the OctoPrint Web Inferface

2. Open the Settings using the 🔧 (wrench) icon in the top right header

3. Open the Plugin Manager in the left-side selection menu

4. Click on the "+ Get More" button

5. Search for PrintWatch

6. Click Install on the PrintWatch Plugin

7. Restart OctoPrint once Installation is completed

The full installation guide/quickstart can be found here: QuickStart Guide with OctoPrint

### Configuration

Once you have successfully installed PrintWatch, you should configure the settings. To configure the settings:

1. Open the OctoPrint Web Inferface

2. Open the Settings using the 🔧 (wrench) icon in the top right header

3. Scroll down to the Plugin Settings in the left-side selection menu and select 'PrintWatch'

Follow the setup guide on the official [GitHub](https://github.com/printpal-io/OctoPrint-PrintWatch) or the [printpal.io website](https://printpal.io/documentation/quick-start-guide/)


### Authentication

In order to use PrintWatch, you must provide your API key in the settings. Visit the [printpal.io website](https://printpal.io/pricing/) to register your key for your printers.

# Privacy Policy
Read our privacy polich here: [PrintWatch Privacy policy](https://printpal.io/privacy/)
