---
layout: plugin

id: bitbang
title: OctoPrint-BitBang
description: Remote OctoPrint access with live H.264 video via BitBang WebRTC. No account, no port forwarding, one shareable link.
authors:
- Rich LeGrand
license: MIT
date: 2026-05-25

homepage: https://github.com/richlegrand/OctoPrint-BitBang
source: https://github.com/richlegrand/OctoPrint-BitBang
archive: https://github.com/richlegrand/OctoPrint-BitBang/archive/main.zip

privacypolicy: https://github.com/richlegrand/OctoPrint-BitBang/blob/main/PRIVACY.md

tags:
- remote access
- webrtc
- webcam
- video
- h264
- raspberry pi
- timelapse

screenshots:
- url: /assets/img/plugins/bitbang/bitbang_config.png
  alt: BitBang settings panel
  caption: Settings → BitBang configuration
- url: /assets/img/plugins/bitbang/camera_select.png
  alt: Camera selection dropdown
  caption: Auto-detected cameras
- url: /assets/img/plugins/bitbang/resolution_select.png
  alt: Resolution dropdown
  caption: Pick resolution up to 720p
- url: /assets/img/plugins/bitbang/bitbang_url.png
  alt: Shareable BitBang URL
  caption: Click the BitBang menu item to get the URL
- url: /assets/img/plugins/bitbang/bitbang_video.png
  alt: Live video in the Control tab
  caption: Hardware-encoded H.264 in the Control tab

featuredimage: /assets/img/plugins/bitbang/bitbang_default.png

attributes:
- cloud
- ai-developed

compatibility:
  octoprint:
  - 1.9.0
  os:
  - linux
  python: ">=3.10,<4"

---

OctoPrint-BitBang gives you full remote access to your OctoPrint instance — including live H.264 video — over a single secure HTTPS shareable link. It uses [BitBang](https://github.com/richlegrand/bitbang) to create a peer-to-peer connection that requires no account, no subscription, no port forwarding, no tunnel, and no VPN.

## What you get

- **Full remote access:** Configure, upload G-code, start jobs, see live video — from anywhere, through a secure HTTPS URL.
- **One link, no account set-up:** Share the URL, share your printer.
- **Live H.264 video:** Hardware-encoded on Pi 4 (`/dev/video11` V4L2 M2M), software-encoded on Pi 5 or any other Linux host. Packetized by aiortc and delivered as a WebRTC media stream. CPU footprint is around 40% (single core) on Pi 4.
- **BitBang URL access is optional:** Video streaming also works with local-network URL access.
- **Pi CSI camera or USB webcam:** Auto-detected (IMX477, IMX219, IMX708, or any V4L2-capable USB webcam).
- **Camera controls:** Camera selection, live brightness slider, fullscreen button, image flip H/V buttons, and resolution selection (VGA up to 720p).
- **Snapshots and timelapse:** Integrates with OctoPrint's `WebcamProviderPlugin` API — snapshots are grabbed from the live stream, so no second camera pipeline to configure.
- **Mobile friendly:** BitBang URL works on phones and tablets.
- **PIN protection:** Optional PIN required to access the remote URL.

## How it works

- The `bitbang-python` package handles WebRTC signaling, identity, and the ASGI interface.
- This plugin wraps it with OctoPrint integration: settings UI, `WebcamProviderPlugin` hooks, camera auto-detect, CSRF-safe cookie handling, and the JavaScript that injects the `<video>` element into OctoPrint's Control tab.
- The `bitba.ng` cloud acts purely as a signaling relay to broker a direct peer-to-peer connection. If a direct connection isn't available, `bitba.ng` will use TURN instead.

## Privacy

The plugin connects through the `bitba.ng` cloud signaling service to broker peer-to-peer connections. `bitba.ng` sees only your public key, derived UID, and connection metadata — not your video or OctoPrint traffic. Once peers connect, media and HTTP flow over an encrypted WebRTC channel directly. If a direct connection cannot be established, `bitba.ng` may relay the encrypted stream via TURN; it still cannot decrypt the contents.

See the [full privacy policy](https://github.com/richlegrand/OctoPrint-BitBang/blob/main/PRIVACY.md) for details and opt-out instructions.

## Supported hardware

- **Raspberry Pi 4** — hardware H.264 via V4L2 M2M; tested with IMX477, IMX219
- **Raspberry Pi 5** — software H.264 via picamera2's `LibavH264Encoder`; 720p@30 comfortably
- **Generic Linux PC / laptop / SBC with webcam** — software H.264 via aiortc
- **USB webcams** — any device that offers a V4L2 capture format; aiortc software-encodes to H.264

## Credits

Built on [aiortc](https://github.com/aiortc/aiortc), [picamera2](https://github.com/raspberrypi/picamera2), and the [bitbang-python](https://github.com/richlegrand/bitbang-python) library.
