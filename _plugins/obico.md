---
layout: plugin

id: obico
title: "Obico for OctoPrint: Full Remote Access - AI Failure Detection & Smart 3D Printing"
description: "Securely access OctoPrint remotely from anywhere for free with Obico. Get unlimited live webcam streaming, secure remote access, 3D printer status notifications, and a free companion mobile app for iOS and Android. Obico is the easiest plugin to access OctoPi remotely! The best part? Advanced AI-powered failure detection watches your prints so you don’t have to."
author: The Obico team
license: AGPLv3
date: 2019-11-07

homepage: https://www.obico.io
source: https://github.com/TheSpaghettiDetective/OctoPrint-Obico
archive: https://github.com/TheSpaghettiDetective/OctoPrint-Obico/archive/master.zip

tags:
- remote
- monitor
- webcam
- phone
- control
- port forwarding
- safe
- secure
- internet
- remote access
- remote app
- remote camera
- remote printing
- monitoring
- AI
- Machine Learning
- app
- mobile
- mobile app
- notification
- cloud
- free
- plugin support
- alert
- smart
- email
- 3rd party app support
- alerts
- android
- ios
- live streaming
- webcam streaming
- remote monitoring
- vpn
- webhook
- octoapp
- octopod
- octoremote
- polymer
- printoid
- notifications
- secure access
- snapshots
- remote printing
- camera
- discord
- slack
- pushover
- pushbullet
- timelapse
- video streaming
- spaghetti detection
- print failure
- print statistics
- g-code management
- file management
- octopi remote

featuredimage: /assets/img/plugins/obico/featured.png

# TODO
# You only need the following if your plugin requires specific OctoPrint versions or
# specific operating systems to function - you can safely remove the whole
# "compatibility" block if this is not the case.

compatibility:

  # List of compatible versions
  #
  # A single version number will be interpretated as a minimum version requirement,
  # e.g. "1.3.1" will show the plugin as compatible to OctoPrint versions 1.3.1 and up.
  # More sophisticated version requirements can be modelled too by using PEP440
  # compatible version specifiers.
  #
  # You can also remove the whole "octoprint" block. Removing it will default to all
  # OctoPrint versions being supported.

  octoprint:
  - 1.3.8

  # List of compatible operating systems
  #
  # Valid values:
  #
  # - windows
  # - linux
  # - macos
  # - freebsd
  #
  # There are also two OS groups defined that get expanded on usage:
  #
  # - posix: linux, macos and freebsd
  # - nix: linux and freebsd
  #
  # You can also remove the whole "os" block. Removing it will default to all
  # operating systems being supported.

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=2.7,<4"

attributes:
- cloud
- commercial
- free-tier

---

## Welcome to Obico!

Obico is the all-in-one smart 3D printing app for OctoPrint - Connect your 3D printer to [Obico](https://obico.io/) for free to get instant access to AI failure detection, full OctoPrint remote access, a fully featured mobile app rated 4.8+ on iOS and Android, and more smart 3D printing features!

<br/><br/>

## Access OctoPrint Remotely From Anywhere on Any Device

Once connected to [Obico for OctoPrint](https://www.obico.io/octoprint.html), you can use the mobile app for iOS or Android to access your 3D printer on your phone or use Obico’s tunneling feature on your web browser to access the full OctoPrint user interface remotely. No need to worry, you can access OctoPrint everywhere with an internet connection. Take Octoprint to the next level by [getting started](https://obico.io/docs/user-guides/octoprint-plugin-setup/) in less than two minutes.

<br/><br/>

## Advanced AI Failure Detection

Get 3D printing peace of mind with Our AI, which has watched over 80 million hours of 3D printing and has caught almost one million failures for over 100,000 users to date! We are the original creators of AI failure detection (back when we were The Spaghetti Detective), and we are constantly improving the model and working to add additional features!

<br/><br/>

## Features

### 📹 Unlimited Webcam Streaming

Check in on your prints and watch the live webcam stream from anywhere.

### 🪄  AI Failure Detection

AI watches your prints for failures so you don’t have to. Configure settings to pause the print or just notify you when a failure is detected. [Learn more about AI failure detection](https://www.obico.io/failure-detection.html).

### 🛎️ Print Status Notifications

Fully customizable printer status notifications are available via mobile push notifications, email, SMS, Telegram, Discord, and many more channels.

### 🎮 3D Printer Remote Control

Start, stop, pause, and control every aspect of your 3D printer from anywhere on any device. Upload and manage G-Code, check when your print will finish, adjust flow rate, fan speed, and more.

### 📱 Mobile App for OctoPrint

The highly rated Obico mobile app for OctoPrint, available for [iOS](https://apps.apple.com/ae/app/obico-for-octoprint-klipper/id1540646623) and [Android](https://play.google.com/store/apps/details?id=com.thespaghettidetective.android&hl=en_US&gl=US), gives you an easy way to monitor and control your 3D printer at all times whether you are home or away.

If you have a favorite OctoPrint mobile app, Obico’s OctoPrint tunneling feature lets you use OctoApp, Polymer, and OctoPod from anywhere.

### 🔥 Easily Manage Multiple Printers

Manage multiple printers connected to OctoPrint from one easy-to-use application from any device.

### 🤝 Share Prints with Your Friends

Share a secure link to your printer’s live webcam stream with your friends so they can watch your prints come to life.

### 📊 3D Print Statistics

Monitor your 3D printing activity over time. See how much filament you’ve used, how many times, or how many hours you’ve 3D printed.

### 📁 G-Code File Management and Print History

Upload G-Code files to Obico, and manage files stored within OctoPrint remotely through the Obico mobile app or web app. Keep track of how long files take to print and how many times they have been printed.


<br /><br />

![](/assets/img/plugins/obico/obico-for-octoprint-printer-control.gif "Printer Control")

<br /><br />

## Pictures

### Secure OctoPrint Remote Access from Anywhere with OctoPrint Tunneling

![](/assets/img/plugins/obico/octoprint-tunneling.png "Remote Access")

<br />

### AI Failure Detection Watches Your Prints For You

![](/assets/img/plugins/obico/print-failing.png "AI Failure Detection")

<br />

### iOS and Android App

<div class="row-fluid" style="margin-top: 28px;">
  <div class="span6">
    <img style="width: 200px; display: block; margin: auto;" src="/assets/img/plugins/obico/remote-monitor-mobile.png" />
    <h4 style="text-align: center;">Realtime Remote Monitoring</h4>
  </div>
  <div class="span6">
    <img style="width: 200px; display: block; margin: auto;" src="/assets/img/plugins/obico/failure-detection-mobile.png" />
    <h4 style="text-align: center;">Automatic Failure Detection</h4>
  </div>
</div>

<div class="row-fluid" style="margin-top: 28px;">
  <div class="span6">
    <img style="width: 200px; display: block; margin: auto;" src="/assets/img/plugins/obico/multiple-printer-mobile.png" />
    <h4 style="text-align: center;">Easily  Manage Multiple Printers</h4>
  </div>
  <div class="span6">
    <img style="width: 200px; display: block; margin: auto;" src="/assets/img/plugins/obico/remote-control-mobile.png" />
    <h4 style="text-align: center;">Remote 3D Printer Control</h4>
  </div>
</div>

<div class="row-fluid" style="margin-top: 28px;">
  <div class="span6">
    <img style="width: 200px; display: block; margin: auto;" src="/assets/img/plugins/obico/g-code-mobile.png" />
    <h4 style="text-align: center;">Upload G-Code & Start Prints</h4>
  </div>
  <div class="span6">
    <img style="width: 300px; display: block; margin: auto;" src="/assets/img/plugins/obico/full-screen-mobile.png" />
    <h4 style="text-align: center;">Full Screen Webcam Streaming</h4>
  </div>
</div>

<br />

## Curious if the AI Failure Detection Really Works?

As the original creators of AI failure detection for 3D printing (Obico was formerly The Spaghetti Detective), we have the most advanced and established AI Failure detection. To date, our AI failure detection has watched over 80 million hours of 3D printing and caught almost one million 3D printing failures. Here are a few real-life examples:

{% include youtube.html vid="tUmHmVRIF_4" preview="'/assets/img/plugins/obico/video_preview2.png'" %}
Video courtesy of TSD user Jimmy.

<br />

{% include youtube.html vid="uf_oSxS6oI8" preview="'/assets/img/plugins/obico/video_preview3.png'" %}
Video courtesy of TSD user Lila.

<br />

**[More failure detection examples](https://app.obico.io/ent_pub/publictimelapses/).**

<br /><br />

## Is Obico's Remote Access and AI Failure Detection Free?

The Obico Cloud free plan is 100% free! Some features are limited due to the cost required for us to run and maintain the Obico Cloud. The Pro Plan gives you full access to all of Obico’s features for the price of a couple of coffees per month. [See the pricing](https://app.obico.io/ent_pub/pricing/).

Of course, since Obico is open-source, you are **free** (sorry for the pun!) to self-host your own Obico Server! [Compare self-hosting versus Obico Cloud]( https://obico.io/obico-cloud-vs-self-hosted.html), or [read the self-hosting documentation](https://www.obico.io/docs/server-guides/).

<br /><br />

## Is Obico’s OctoPrint Remote Access Secure?

Yes! Unlike port forwarding, your OctoPrint is never exposed to the wild internet when you access it via Obico. Instead, your OctoPrint page is loaded through a SSL-ecrypted tunnel. Check [this article](https://www.obico.io/blog/2021/09/24/octoprint-anywhere/) for detailed explanation.

<br /><br />

## Does Obico Let me access the full OctoPrint interface from anywhere?

Yes, Obico’s tunneling feature allows you to access the full OctoPrint user interface remotely from anywhere without configuring a VPN or using port forwarding. Obico gives you options to access the full OctoPrint interface or to use Obico’s mobile app or in a browser to access the most common features for monitoring and controlling your 3D printer.

<br /><br />

## Getting Started

Setting up Obico is easy! Just install the Obico plugin and follow the steps in the setup wizard! If you run into any trouble getting started, you can check out the [Obico for OctoPrint Setup Guide](https://obico.io/docs/user-guides/octoprint-plugin-setup/).

Create an Obico Cloud account to run Obico with no extra setup required or you can self-host your own Obico Server. [Learn more about the different ways to run Obico](https://obico.io/obico-cloud-vs-self-hosted.html).

![](/assets/img/plugins/obico/setup-wizard.png "Plugin Setup Wizard")
