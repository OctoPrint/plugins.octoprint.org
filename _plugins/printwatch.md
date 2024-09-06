---
layout: plugin

id: printwatch
title: Abort Failures - Printwatch
description: PrintWatch monitors your prints for defects in real-time and optimizes your 3D printers using Artificial Intelligence for Free. PrintWatch allows you to remotely view and manage your printers from anywhere in the world. Save wasted material and time with our AI monitoring system that notifies you and/or pauses the print when something goes wrong. Go about your day with the peace of mind that your 3D printer is working as it should.
author: printpal.io
license: AGPLv3

date: 2022-01-31

homepage: https://github.com/printpal-io/OctoPrint-Printwatch
source: https://github.com/printpal-io/OctoPrint-Printwatch
archive: https://github.com/printpal-io/OctoPrint-Printwatch/archive/master.zip

privacypolicy: https://printpal.io/privacy/

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
- free


screenshots:
- url: /assets/img/plugins/printwatch/printwatch-tab.jpg
  alt: PrintWatch monitors your prints with Artificial Intelligence and saves you time and material
  caption: PrintWatch watches your prints and shows you the status of your print in real-time
- url: /assets/img/plugins/printwatch/printwatch.png
  alt: PrintWatch monitors your prints with Artificial Intelligence and saves you time and material
  caption: PrintWatch monitors your prints with Artificial Intelligence
- url: /assets/img/plugins/printwatch/printwatch-notification.png
  alt: Get notified when something goes wrong with your print. Reduce downtime and loss
  caption: PrintWatch notifies you when something goes wrong. Let AI do the watching for you while you enjoy your day
- url: /assets/img/plugins/printwatch/printwatch-settings.jpg
  alt: Configurable settings allow you to customize how PrintWatch works for you.
  caption: Configure your settings the way you like.
- url: /assets/img/plugins/printwatch/printwatch-web-app-main-page.jpg
  alt: Manage all your printers from one place, anywhere in the world.
  caption: Manage all your printers from anywhere in the world.
- url: /assets/img/plugins/printwatch/printwatch-web-app-individual-printer.jpg
  alt: Preview your printers and make changes on the fly.
  caption: Preview your printers and make changes on the fly.

featuredimage: /assets/img/plugins/printwatch/printwatch-web-app-individual-printer.jpg


compatibility:

  octoprint:
  - 1.3.2

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=3.6,<4"

attributes:
- cloud
- commercial
- free-tier

---

# PrintWatch - Free AI monitoring and remote management
In a little over a year during the BETA program phase, PrintWatch has saved users over $1,000,000 and 7,000 lbs of plastic that would have gone to waste. Our goal is to make 3D printing as simple and seamless as possible for all, regardless of experience. With a quick and easy setup that takes less than 5 minutes, you can enjoy the power of AI for Free today!

### How does it work?
PrintWatch uses Artificial Intelligence to monitor your 3D prints for any defects that begin to form. The plugin takes the video feed from any camera compatible with OctoPrint and runs it through a Machine Learning model that detects print defects in real-time. The plugin takes actions set by the user once a failure is positively detected that include:

- 📧 Email/SMS Notification
- ⏸ Pausing/Stopping the print job
- 🔥 Turning off the Extruder Heat
- ⚙ Customized actions created by the user

### How safe is it?

printpal.io only uses top of the line cloud compute providers that follow the strictest security standards to ensure that our system is safe for you to use. PrintWatch servers comply to all of the leading industry standards, including, but not limited to:
- SSL/TLS encryption
- Zero-Trust
- GDPR compliance
- DDOS protection
- WAF/PCI DSS 3.2 Compliance
 
### Watch the AI in action
Our AI uses the fastest and the strongest Machine Learning model for detecting 3D print failures. It works with all filaments, colors, printers, and what ever combination of factors you throw at it.

![](/assets/img/plugins/printwatch/ai-example-1.gif "Bambu labs P1P fail")

### Features and roadmap
In addition to detecting defects, PrintWatch has an Anomaly Detection model running in the background that can detect slight changes or anomalies for printers in your fleet. Get notified early and schedule maintenance for the problematic printer, reducing downtime and costs. PrintWatch's Web App allows you to remotely view and manage all of your printers from anywhere in the world.
Current features include:

- Real-time defect detection
- Remote access and management
- Anomalous Printer Detection
- Advanced Analytics
- Resume Print

Upcoming features include:

- Pre+post print bed check - currently in BETA. Contact us to join.
- Live QC/QA - currently in BETA. Contact us to join.
- G-Code and Speed optimization with ML
- MultiCamming - currently available using the API Client repository
- ROI selection and slicing - currently available using the API Client repository
- Local Device - currently in pilot program phase. Contact us to get a copy

### Setup

1. Open the OctoPrint Web Inferface

2. Open the Settings using the 🔧 (wrench) icon in the top right header

3. Open the Plugin Manager in the left-side selection menu

4. Click on the "+ Get More" button

5. Search for PrintWatch

6. Click Install on the PrintWatch Plugin

7. Restart OctoPrint once Installation is completed

The full installation guide/quickstart can be found here: [QuickStart Guide with OctoPrint](https://printpal.io/documentation/quick-start-guide/)

### Configuration

Once you have successfully installed PrintWatch, you should configure the settings. To configure the settings:

1. Open the OctoPrint Web Inferface

2. Open the Settings using the 🔧 (wrench) icon in the top right header

3. Scroll down to the Plugin Settings in the left-side selection menu and select 'PrintWatch'

Follow the setup guide on the official [GitHub](https://github.com/printpal-io/OctoPrint-PrintWatch) or the [printpal.io website](https://printpal.io/documentation/quick-start-guide/)


### Authentication

In order to use PrintWatch, you must provide your API key in the settings. Either use your Free API key, or visit the [printpal.io website](https://printpal.io/pricing/) to register your key for your printers.

# Privacy Policy
Read our privacy policy here: [PrintWatch Privacy policy](https://printpal.io/privacy/)
