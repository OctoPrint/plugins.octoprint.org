---
layout: plugin

id: mattacloud
title: Mattacloud Beta
description: Making 3D printers intelligent. Remote 3D printer control and management from anywhere with advanced AI error detection and informative notifications.
author: Mattalabs
license: AGPLv3

# TODO
date: 2020-10-17

homepage: https://github.com/Mattalabs/OctoPrint-Mattacloud
source: https://github.com/Mattalabs/OctoPrint-Mattacloud
archive: https://github.com/Mattalabs/OctoPrint-Mattacloud/archive/master.zip

tags:
- remote monitoring
- cloud printing
- webcam
- print queue
- remote control
- ai
- machine learning
- error detection
- beta

screenshots:
- url: /assets/img/plugins/mattacloud/mattacloud.png
  alt: Mattacloud Plugin - Add complete remote control and monitoring and AI error detection to your 3D printer with Mattacloud by Mattalabs
  caption: Add complete remote control and monitoring and AI error detection to your 3D printer
- url: /assets/img/plugins/mattacloud/ai_detection.jpg
  alt: Mattacloud Plugin - AI Error Detection
  caption: Personal and industrial versions of Mattacloud come with state-of-the-art AI error detection (still being tested internally).
- url: /assets/img/plugins/mattacloud/communication.png
  alt: Mattacloud Plugin - Communication and notifications
  caption: Keep informed by receiving notifications and updates from the Mattacloud to your device.

featuredimage: /assets/img/plugins/mattacloud/mattacloud.png

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

# What is Mattacloud

Full remote control, management and access from anywhere in addition to automatic and intelligent error detection and process monitoring for your OctoPrint-enabled 3D printer. Additionally, receive notifications and updates alerting you of failures and keeping you updated on the state of your 3D print. Overview your print history and gain insights into filament use, print times and your printer reliability.

Learn more about **Mattacloud** and its features - [https://mattalabs.com/products/mattacloud/](https://mattalabs.com/products/mattacloud/)

_Note: **Mattacloud** is currently still in development so users may experience changes and errors during use._

### Printer Setup

The setup progress takes less than 5 minutes and consists of 5 simple steps. If you follow these, all the benefits of **Mattacloud** will apply to your printer. Happy printing!

1. [Sign up](https://cloud.mattalabs.com/accounts/signup/) to the **Mattacloud Free Plan** currently undergoing beta testing. If you already have, just [login](https://cloud.mattalabs.com/accounts/login/). This plan will remain free after the beta testing period has finished.
2. Select your membership type - at this stage you can only choose the free beta membership.
3. Add a printer to your **Mattacloud** by following the setup guide.
4. After installing the OctoPrint-Mattacloud Plugin on your OctoPrint enabled device, copy the authorization token from your newly created printer on **Mattacloud** into the authorization token input box presented in the OctoPrint-Mattacloud plugin settings. You can see all of your printers and their respective tokens [here](https://cloud.mattalabs.com/printer-dashboard/).
5. Test your token using the **Activate** button adjacent to the input box.
6. You are all setup. Happy printing!

### Installation with WebRTC for live video streams

OctoPrint-Mattacloud uses WebRTC to enable real-time video streams from the printer to your device. In order to utilise this capability a few additional packages need to be installed on your Raspberry Pi (or other device) running OctoPrint. These packages are not required for using the main features of the plugin.

If you are not using the Mattacloud SD image then you need to install the following packages:

```
sudo apt-get install libavformat-dev libavcodec-dev libavdevice-dev libavutil-dev libavfilter-dev libswscale-dev libswresample-dev python-dev python3-dev libsrtp2-dev libsrtp2-1 libopus-dev libvpx-dev pkg-config
```

These packages are required for OpenCV and are also needed to build `pylibsrtp` a requirement of `aiortc` for WebRTC.

Once you have installed the above packages you can activate your Python 3 virtualenv where OctoPrint is installed. It will be something like ```source oprint/bin/activate```. Then install the following using `pip`:

```
pip install aiohttp==3.6.2 aiortc==0.9.7 numpy==1.19.1 opencv-python==4.4.0.40
```

or if you have the plugin downloaded / cloned you can use:

```
pip install -r webrtc_requirements.txt
```

When the plugin has installed, restart OctoPrint and begin the Printer Setup process outlined below.

### Report problems

If something does not appear to be working correctly and you think you may have found a bug in the OctoPrint-Mattacloud Plugin, please create an issue on the official page [here](https://github.com/dougbrion/OctoPrint-Mattacloud/issues). In this way your issue can be understood and fixed quickly.

Or feel free to contact us via [whatsthematta@mattalabs.com](mailto:whatsthematta@mattalabs.com).

### Error detection and process monitoring

3D printers are not the most reliable of machines. All of us have suffered from errors whilst printing and many users find themselves _handcuffed_ to their printers, having to constantly check the printer every 5 minutes to make sure that the print is _still_ okay! If this sounds familiar to you... hopefully this plugin will help.

Numerous computer vision techniques are used to determine if an error has occurred during your 3D print. Using a mixture of machine learning, 3D printing heuristics and the direct comparison of g-code to the current state of the 3D print, an errors are reliably determined in an image of the print.

Errors that the personal and industrial plans are capable of detecting are:

- Detatchment from print bed
- Offset
- Warping
- Poor bed adhesion
- Spaghetti
- Blocked extruder / out of filament
- Hotend too close to print bed

At present, the Beta plan does not support error detection as we are still testing our AI models in house. To be released by the end of 2020!

### Remote control and management

Access your 3D printer from anywhere in the world (provided that there is an internet connection...) via the OctoPrint-Mattacloud Plugin.

At present, the plugin enables you to do the following:

- View and update hotend, bed and chamber temperatures
- Control and home X, Y and Z axes
- Select prints to retrieve information
- Start, cancel, pause, resume and restart 3D prints
- Upload g-code files remotely to your printer for printing
- Delete g-code files remotely
- Receive the latest images/snapshots from your printer
- See your prints progress (time remaining and percentage completion)

### Notifications and updates

By installing this plugin and linking a printer to your **Mattacloud** account, you can receive useful notifications and updates concerning your 3D printer via various channels. When an error occurs during the 3D printing process, you will receive an alert with an attached image showing the error in addition to current progress, material usage and other useful statistics; you can then deside to take action. Additionally, you can also set up other checkpoints to receive notifications, such as upon object completion, or when a print has reached the half way mark. 

The communication channels which are currently supported are:

- Email (in Beta plan)
- SMS (personal and industrial plans)
- WhatsApp (personal and industrial plans)
- Facebook Messenger (personal and industrial plans)

### License

View the [OctoPrint-Mattacloud plugin license](https://github.com/Mattalabs/OctoPrint-Mattacloud/blob/master/LICENSE)
