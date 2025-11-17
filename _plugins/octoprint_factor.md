---
layout: plugin

id: octoprint_factor
title: FACTOR Plugin
description: Remote monitoring and control for OctoPrint. Access your 3D printer from anywhere with real-time monitoring, camera streaming, and instant notifications via cloud connection.
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
- notifications
- mobile
- cloud

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

Remote monitoring and control for OctoPrint via cloud-based MQTT connection.

## Features

### 🚀 **Easy Setup**
- Simple web-based registration
- Automatic MQTT connection configuration
- Start monitoring immediately - no complex broker setup needed

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

## What's New in v2.6.3

- 🌍 **English Logging** - All logging statements now in English for international users
- 🔒 **Secure MQTT Connection** - TLS/SSL encryption enabled by default
- 🌐 **Cloud Integration** - Pre-configured broker connection to FACTOR cloud
- 🔧 **Simplified Setup** - No manual MQTT broker configuration needed
- 📱 **Multi-language Support** - English and Korean interfaces
- 🎨 **Clean Modern UI** - Intuitive settings and monitoring interface

---

**Made with ❤️ by FACTOR Team**
