---
layout: plugin

id: obico
title: Obico for OctoPrint
description: Securely monitor and control your OctoPrint-connected printer from anywhere for free with Obico. Get unlimited live webcam streaming, full OctoPrint remote access, printer status notifications, and a free companion mobile app for iOS and Android. The best part? AI-powered failure detection watches your prints so you don’t have to. (Obico is the successor of The Spaghetti Detective.)
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

---

**Obico is the successor of The Spaghetti Detective.**

<br />

<p class="lead">Welcome to <a href="https://obico.io">Obico</a>, the all-in-one smart 3D printing platform!</p>

Connecting your 3D printer to Obico makes your 3D printer smarter and gives you peace of mind through many great features.

<br />

### Features

#### 📹 Unlimited Webcam Streaming

Check in on your prints and watch the livestream from anywhere.

#### 🪄  AI Failure Detection

AI watches your prints for failures so you don’t have to.  Configure settings to pause the print or just notify you when a failure is detected.

#### 🛎️ Print Status Notifications

Fully customizable printer status notifications are available via mobile push notifications, email, SMS, Telegram, Discord and many more channels.

#### 🎮 3D Printer Remote Control

Start, stop, pause, and control every espect of your 3D printer from anywhere.

#### 📱 Mobile App

The obico mobile app for iOS and Android gives you an easy way to monitor and control your 3D printer at all times.

If you have a favorite OctoPrint mobile app, Obico’s OctoPrint tunneling feature lets you use OctoApp, Polymer, and OctoPod from anywhere.

#### 🔥 Easily Manage Multiple Printers

Manage multiple printers from one easy to use application from any device.

#### 🤝 Share Prints with Your Friends

Share a secure link of your printer’s live webcam stream with your friends so they can watch your prints come to life.

<br />

![](/assets/img/plugins/obico/obico-for-octoprint-printer-control.gif "Printer Control")

<br />

### Pictures

#### Secure OctoPrint Remote Access from Anywhere with OctoPrint Tunneling

![](/assets/img/plugins/obico/octoprint-tunneling.png "Remote Access")

<br />

#### AI Failure Detection Watches Your Prints For You

![](/assets/img/plugins/obico/print-failing.png "AI Failure Detection")

<br />

#### iOS and Android App

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

### Curious if the AI Failure Detection Really Works?

To date, our AI failure detection has watched over **60-million hours** of 3D priting and caught hundreds of thousands of failures. Here are a few real-life examples:

{% include youtube.html vid="tUmHmVRIF_4" preview="'/assets/img/plugins/obico/video_preview2.png'" %}
Video courtesy of TSD user Jimmy.

<br />

{% include youtube.html vid="uf_oSxS6oI8" preview="'/assets/img/plugins/obico/video_preview3.png'" %}
Video courtesy of TSD user Lila.

<br />

**[More failure detection examples](https://app.obico.io/ent_pub/publictimelapses/).**

<br />

### Getting Started

Setting up Obico is easy! Just install the Obico plugin and follow the steps in the setup wizard! If you run into any trouble getting started, you can check out the [Obico for OctoPrint Setup Guide](https://obico.io/docs/user-guides/octoprint-plugin-setup/).

Create an Obico Cloud account to run Obico with no extra setup required or you can self-host your own Obico Server. [Learn more about the different ways to run Obico](https://obico.io/obico-cloud-vs-self-hosted.html).

![](/assets/img/plugins/obico/setup-wizard.png "Plugin Setup Wizard")

<br />

### Is Obico Free?

The Obico Cloud free plan is 100% free! Some features are limited due to the cost required for us to run and maintain the Obico Cloud. The Pro Plan gives you full access to all of Obico’s features for the price of a couple of coffees per month. [See the pricing](https://app.obico.io/ent_pub/pricing/).

Of course, since Obico is open-source, you are **free** (sorry for the pun!) to self-host your own Obico Server! [Compare self-hosting versus Obico Cloud]( https://obico.io/obico-cloud-vs-self-hosted.html), or [read the self-hosting documentation](https://www.obico.io/docs/server-guides/).

<br />
<br />
