---
layout: plugin

id: PiNozCam
title: OctoPrint-PiNozCam
description: AI-driven FREE monitoring for 3D print failures using Pi Arm CPU.
author: DrAlexLiu
license: AGPLv3

date: 2024-03-03

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

Failure Detection is on Pi CPU

Elevate your 3D printing experience with OctoPrint-PiNozCam, a **free** and powerful plugin that brings **AI-powered monitoring** directly to your Raspberry Pi, **without the need for any subscription**. Process your print jobs **locally** with advanced AI algorithms that detect potential failures, ensuring **privacy and efficiency**. Stay informed with instant **notifications** sent directly to your **Telegram** on **cellphone**, keeping you connected to your prints anytime, anywhere. OctoPrint-PiNozCam is the ultimate, cost-effective solution for optimizing your 3D printing process with the power of AI, right at your fingertips.


**Features include:**

- **Local AI-Powered Monitoring**
- **Configurable Actions for Pause/Stop**
- **Telegram Remote Notification**
- **Performance Optimization On Pi Arm CPU**
- **User-Friendly Interface**

Whether you're running a print farm or a single printer in your workshop, PiNozCam offers peace of mind and a new level of interaction with your 3D printing process.

## Setup

### Installation

You can install the PiNozCam plugin directly through OctoPrint's Plugin Manager by searching for "PiNozCam" in the repository. 

After installation, you can configure PiNozCam via the plugin settings in OctoPrint. Key configuration options include:

- **Action**: Choose the action PiNozCam should take upon detecting a print failure (e.g., notify, pause print, stop print).
- **AI Sensitivity**: Adjust the sensitivity of the AI detection algorithms to suit your printing environment and preferences.
- **CPU Speed Control**: Control the plugin's CPU usage, especially useful for Raspberry Pi users to balance performance and resource utilization.
- **Telegram Bot Token & Chat ID**: Enter your Telegram bot token and chat ID to enable instant notifications.

## Getting Started

Once installed and configured, PiNozCam will automatically start monitoring your prints using your printer's camera feed. You'll receive notifications based on your configured actions and can adjust settings anytime to fine-tune the monitoring performance.

Enjoy a new level of confidence in your 3D printing with OctoPrint-PiNozCam, your AI-powered watchful eye.