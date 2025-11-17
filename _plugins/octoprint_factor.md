---
layout: plugin

id: octoprint_factor
title: FACTOR Plugin
description: Remote monitoring and control for OctoPrint via QR code setup. Access your 3D printer from anywhere with real-time monitoring, camera streaming, and instant notifications.
authors:
- FACTOR Team
license: AGPLv3

date: 2024-11-17

homepage: https://github.com/kangbyounggwan/octoprint-factor-plugin
source: https://github.com/kangbyounggwan/octoprint-factor-plugin
archive: https://github.com/kangbyounggwan/octoprint-factor-plugin/archive/{target_version}.zip

privacypolicy: https://factor.io.kr/privacy

attributes:
- cloud
- commercial
- free-tier

tags:
- remote access
- monitoring
- mqtt
- camera
- qr code
- notifications
- mobile
- cloud

screenshots:
- url: https://raw.githubusercontent.com/kangbyounggwan/octoprint-factor-plugin/main/docs/screenshot-wizard.png
  alt: FACTOR Plugin Setup Wizard
  caption: Simple 20-second QR code setup wizard
- url: https://raw.githubusercontent.com/kangbyounggwan/octoprint-factor-plugin/main/docs/screenshot-settings.png
  alt: FACTOR Plugin Settings
  caption: Clean settings interface with multilingual support

featuredimage: https://raw.githubusercontent.com/kangbyounggwan/octoprint-factor-plugin/main/docs/logo.png

compatibility:
  octoprint:
  - 1.4.0

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=3.8,<4"

---

# FACTOR Plugin

Remote monitoring and control for OctoPrint via MQTT, featuring instant QR code setup.

## Features

### 🚀 **20-Second Setup**
- Scan QR code with your mobile device
- Complete registration on FACTOR web dashboard
- Start monitoring immediately - no complex configuration needed

### 📱 **Remote Access Anywhere**
- Access your full OctoPrint portal from desktop, laptop, tablet, or phone
- Works with your favorite OctoPrint mobile apps
- Secure cloud connection via MQTT

### 📹 **Camera Streaming**
- Full framerate webcam streaming
- Multiple format support (MJPEG, WebRTC, RTSP, HLS)
- Real-time monitoring of your prints

### 🔔 **Instant Notifications**
- Print completion alerts
- Error notifications
- Real-time status updates
- Multiple notification channels (Push, Telegram, Discord, Email)

### 🌐 **Multilingual Support**
- English and Korean (한국어) built-in
- Automatic language detection
- Easy to add more languages

### 🎨 **Modern UI**
- Clean, intuitive interface
- Follows OctoPrint design standards
- Responsive design for all screen sizes
- Setup wizard for first-time users

## Setup

### From Plugin Manager (Recommended)

1. Open OctoPrint Settings
2. Go to **Plugin Manager**
3. Click **"Get More..."**
4. Search for **"FACTOR"**
5. Click **"Install"**
6. Restart OctoPrint

### From URL

Install manually via this URL:
```
https://github.com/kangbyounggwan/octoprint-factor-plugin/archive/main.zip
```

### From Command Line

```bash
pip install https://github.com/kangbyounggwan/octoprint-factor-plugin/archive/main.zip
```

## Configuration

After installation, the **Setup Wizard** will guide you through configuration:

1. **Scan QR Code**: Use your mobile device to scan the displayed QR code
2. **Web Registration**: Complete device registration on the FACTOR web dashboard at [factor.io.kr](https://factor.io.kr)
3. **Start Monitoring**: Return to OctoPrint and start using FACTOR

That's it! No MQTT broker configuration, no complex settings - just scan and go! 🎉

## Requirements

- OctoPrint 1.4.0 or higher
- Python 3.8 or higher
- Internet connection for cloud features
- FACTOR account (free registration at [factor.io.kr](https://factor.io.kr))

## Support

- **Website**: [https://factor.io.kr](https://factor.io.kr)
- **GitHub Issues**: [Report a bug](https://github.com/kangbyounggwan/octoprint-factor-plugin/issues)
- **Documentation**: [GitHub README](https://github.com/kangbyounggwan/octoprint-factor-plugin)

## Privacy & Security

- All connections are encrypted via TLS/SSL
- Data is transmitted securely via MQTT protocol
- No credentials stored locally
- AGPLv3 licensed - fully open source

## What's New in v2.0.0

- ✨ **QR Code Setup Wizard** - 20-second setup process
- 🌐 **Full Internationalization** - English and Korean support
- 🎨 **Redesigned UI** - Modern, clean interface
- 📱 **Mobile-First Design** - Optimized for all devices
- 🔧 **Simplified Configuration** - No manual MQTT setup needed

---

**Made with ❤️ by FACTOR Team**
