---
layout: plugin

id: pinozcam
title: OctoPrint-PiNozCam
description: AI-driven FREE monitoring for 3D print failures using Pi Arm CPU.
author: DrAlexLiu
license: AGPLv3

date: 2024-03-06

homepage: https://github.com/DrAlexLiu/OctoPrint-PiNozCam
source: https://github.com/DrAlexLiu/OctoPrint-PiNozCam
archive: https://github.com/DrAlexLiu/OctoPrint-PiNozCam/archive/master.zip

follow_dependency_links: false

tags:
- ai
- failure detection
- machine learning
- computer vision
- ai on pi
- monitor
- telegram
- free
- no subscription
- secure
- privacy

compatibility:
  # List of compatible versions
  octoprint:
  - 1.4.0

  # List of compatible operating systems
  os:
  - linux
  - windows
  - macos
  - freebsd

  # Compatible Python version
  python: ">=3.7,<4"
---

# OctoPrint-PiNozCam

![failure_detection1](/assets/img/plugins/pinozcam/failure_detection1.jpg)

## Introduction

Failure Detection Performed on your Pi CPU

Unlock advanced 3D printing monitoring with PiNozCam, your go-to solution for **AI-powered surveillance** — all **without a subscription or email registration**. Designed to enhance your printing process, PiNozCam introduces cutting-edge **edge computing** right on your Raspberry Pi. This ensures your **privacy** and the protection of your 3D model **copyrights**, while enabling you to receive instant failure alerts directly on your mobile via **Telegram**. Best of all, PiNozCam is entirely free, offering you peace of mind at no extra cost. 

**Features include:**

- **AI-Powered Edge Computing for Monitoring**
- **Configurable Actions for Pause/Stop**
- **Instant Telegram Error Notifications**
- **Performance Optimization On Pi Arm CPU**
- **User-Friendly Interface**
- **Privacy First, No email register/sign up/subscription**

Download PiNozCam today and enjoy uninterrupted, worry-free 3D printing forever.


## 🔧 Setup


### Hardware Setup

#### **Raspberry Pi with Cooling Fan**


- Raspberry Pi 5(>=4GB): 30 images / minute (Highly Recommand)
  
  Example: Use [Octoprint_deploy](https://github.com/paukstelis/octoprint_deploy) to install the octoprint and then install PiNozCam
- Raspberry Pi 4B(>=2GB) : 9 images / minute (Recommand)
  
  Example: Use (RPi Imager to flash OctoPi)[https://www.raspberrypi.com/tutorials/set-up-raspberry-pi-octoprint/] and install the PiNozCam

- Raspberry Pi 3B(>=2GB) : 5 images / minute (Acceptable)

  It is advised to adjust the **Max Failure Count to 1** for quick failure stop when operating at this rate of inference.

We strongly recommend **fan cooling** to maintain optimal performance. Although PiNozCam can run on PiZero W 2, their longer inference times make them less recommended options.

⚠️ **Limitation**: Please note, PiNozCam is optimized for **stable OctoPi images** (Bullseye in 32-bit OS system) and all **64-bit OS systems**. For those utilizing other 32-bit Debian platforms, such as OctoPi Nightly (Bookworm armhf platforms) or older OctoPi images (Buster armhf platforms), it's essential to select arm64 builds for compatibility. This ensures a seamless experience and maintains the high performance of PiNozCam in diverse environments.

However, PiNozCam can run other CPUs. If you want to use other methods:

- **PC with Intel i5 10600** (x64, Ubuntu) : 150 images / minute
  
  Example: Use [Octoprint docker](https://hub.docker.com/r/octoprint/octoprint) and install the PiNozCam

- **OrangePi Zero 2/3** (x64, Ubuntu) : 7 images / minute
  
  PiNozCam supports Allwinner (>=H616) and Rockchip (>=RK3566) series. Make sure the memory is at least 1GB. Recommanded >=2GB. 


#### **Endoscope Camera**

Most market-available endoscope cameras are compatible with this setup. Ensure your camera:
- Operates at a [16:9 30Hz](https://community.octoprint.org/t/how-can-i-change-mjpg-streamer-parameters-on-octopi/203) frequency to minimize motion blur and better experience.
- Supports a minimum resolution of **480P**.
- Features built-in lighting for enhanced detection quality.
- Is positioned **approximately 10 cm** from the nozzle. 

⚠️ **Cleaning the camera lens** before each print is crucial as dust can accumulate and affect detection accuracy.


The setup would be like this:

![nozzle_cam_setup](/assets/img/plugins/pinozcam/nozzle_cam_setup.jpg)

### **Software Configuration**

Screenshot:


Go to PiNozCam Tab in Octoprint:

![Tab](/assets/img/plugins/pinozcam/tab.png)

The screenshot would be:

![screenshot](/assets/img/plugins/pinozcam/screenshot.png)


**Key Parameters:**

- **Action:** Specifies the action PiNozCam should take when a print failure is detected (e.g., notify only, pause print, stop print). Detected failures are displayed in the video stream for 5 seconds, allowing for immediate visual verification.
- **Image Sensitivity:** Adjust the sensitivity to ensure accurate detection of print failures. Set the threshold to balance between premature stopping for minor issues and delaying action for significant errors. A starting value of 0.08 or 8% is recommended for optimal balance.
- **Failure Scores Threshold:** Define the confidence level at which an anomaly is considered a print failure. This setting helps in reducing false alarms by setting a minimum probability threshold for errors, ensuring that only genuine failures prompt action.
- **Max Failure Count:** Specify the number of detections required in **Failure Consider Time** before PiNozCam takes the configured action. A value above 1 is recommended to avoid false positives.
- **Failure Consider Time (s):** Implement a time buffer to focus on recent failures, ignoring older detections that may no longer be relevant. This dynamic consideration helps in adapting to the current state of the print.
- **CPU Speed Control:** Offers options for running the CPU at half or full speed. Half speed is recommended in warmer conditions without adequate cooling to prevent overheating. Full speed is optimal with enforced cooling.


To enable notifications, enter your [Telegram bot token and chat ID](https://gist.github.com/nafiesl/4ad622f344cd1dc3bb1ecbe468ff9f8a)
. Following a successful configuration, a welcome message will be sent to your Telegram after you click "Save". An example notification will be sent like this:

![Telegram_notification](/assets/img/plugins/pinozcam/telegram_notification.jpg)

## Final Step: Start Printing

Once everything is set up, you can relax and rely on Telegram notifications to alert you of any issues during printing.
