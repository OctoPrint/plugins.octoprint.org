---
layout: plugin

id: thespaghettidetective
title: Access Anywhere - The Spaghetti Detective
description: 3D Print With Peace of Mind
author: TSD Team
license: AGPLv3

# TODO
date: 2019-11-07

homepage: https://www.thespaghettidetective.com
source: https://github.com/TheSpaghettiDetective/OctoPrint-TheSpaghettiDetective
archive: https://github.com/TheSpaghettiDetective/OctoPrint-TheSpaghettiDetective/archive/master.zip

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

# TODO
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
- cloud printing
- free
- plugin support


featuredimage: /assets/img/plugins/thespaghettidetective/hero.png

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

---

<p class="lead">Whether you're worried about print failures, fire hazards, or network security, The Spaghetti Detective has got your back.</p>

<div class="row-fluid" style="margin-top: 28px;">
  <div class="span4">
    <img style="width: 100px; display: block; margin: auto;" src="/assets/img/plugins/thespaghettidetective/TSDBenefitIcons-03.svg" />
    <div style="text-align: center;font-weight: bolder; margin: 12px 0 18px 0;">Save time and money</div>
  </div>
  <div class="span4">
    <img style="width: 100px; display: block; margin: auto;" src="/assets/img/plugins/thespaghettidetective/TSDBenefitIcons-04.svg" />
    <div style="text-align: center;font-weight: bolder; margin: 12px 0 18px 0;">Catch print hazards early</div>
  </div>
  <div class="span4">
    <img style="width: 100px; display: block; margin: auto;" src="/assets/img/plugins/thespaghettidetective/EquipmentDamageIcon-11.svg" />
    <div style="text-align: center;font-weight: bolder; margin: 12px 0 18px 0;">Lower equipment damage risk</div>
  </div>
</div>
<div class="row-fluid" style="margin-bottom: 18px;">
  <div class="span4">
    <img style="width: 100px; display: block; margin: auto;" src="/assets/img/plugins/thespaghettidetective/TSDBenefitIcons-05.svg" />
    <div style="text-align: center;font-weight: bolder; margin: 12px 0 18px 0;">Secure remote access </div>
  </div>
  <div class="span4">
    <img style="width: 100px; display: block; margin: auto;" src="/assets/img/plugins/thespaghettidetective/TSDBenefitIcons-08.svg" />
    <div style="text-align: center;font-weight: bolder; margin: 12px 0 18px 0;">Manage printer on your phone </div>
  </div>
  <div class="span4">
    <img style="width: 100px; display: block; margin: auto;" src="/assets/img/plugins/thespaghettidetective/TSDBenefitIcons-07.svg" />
    <div style="text-align: center;font-weight: bolder; margin: 12px 0 18px 0;">Get the most out of OctoPrint</div>
  </div>
</div>

## Features

* <span style="font-weight: bold; font-size: 1.2em;">AI-powered failure detection.</span> The Detective will watch your prints so you don't have
  to.

* **Unlimited webcam streaming.** Pro users get 25 fps premium webcam streaming. Free users get
  unlimited streaming at a lower frame rate.

* **Secure OctoPrint remote access/control.** No port-forwarding or VPN required. Full
  OctoPrint access from anywhere with an internet connection.

* **Free companion iOS and Android app.** Progress and webcam feed pushed to your phone while printing. No need to open the app or even unlock the screen.

* **Printer feed sharing.** Show off your print with an encrypted link. Easy. Secure.

<br />

## Does the AI really work?

The Spaghetti Detective has caught thousands of failures for the 3D printing enthusiasts
around the globe. Here are some examples:

{% include youtube.html vid="tUmHmVRIF_4" preview="'/assets/img/plugins/thespaghettidetective/video_preview2.png'" %}
Video courtesy of TSD user Jimmy.

<br />

{% include youtube.html vid="uf_oSxS6oI8" preview="'/assets/img/plugins/thespaghettidetective/video_preview3.png'" %}
Video courtesy of TSD user Lila.

<br />

*If you can't have enough spaghetti (pun intended), head to [The Spaghetti Gallery](https://app.thespaghettidetective.com/publictimelapses/) for more time-lapses.*

<br />

## Screenshots

#### Unlimited webcam streaming

Pro users get 25 fps premium webcam streaming. Free users get unlimited streaming at a lower frame rate.

#### Printer control

![Printer control](/assets/img/plugins/thespaghettidetective/screenshot1.jpg "Printer
control")

#### iOS and Android apps

<div class="row-fluid" style="margin-top: 28px;">
  <div class="span4">
    <img style="width: 200px; display: block; margin: auto;" src="/assets/img/plugins/thespaghettidetective/screenshot4.png" />
    <div style="text-align: center; margin: 0 0 18px 0;">Print progress</div>
  </div>
  <div class="span4">
    <img style="width: 200px; display: block; margin: auto;" src="/assets/img/plugins/thespaghettidetective/screenshot2.png" />
    <div style="text-align: center; margin: 0 0 18px 0;">Temperature controls</div>
  </div>
  <div class="span4">
    <img style="width: 200px; display: block; margin: auto;" src="/assets/img/plugins/thespaghettidetective/screenshot3.png" />
    <div style="text-align: center; margin: 0 0 18px 0;">G-Code remote upload and printing</div>
  </div>
</div>
<div class="row-fluid" style="margin-top: 28px;">
  <div class="span4">
    <img style="width: 200px; display: block; margin: auto;" src="/assets/img/plugins/thespaghettidetective/screenshot5.png" />
    <div style="text-align: center; margin: 0 0 18px 0;">Push notifications on lock screen</div>
  </div>
  <div class="span4">
    <img style="width: 200px; display: block; margin: auto;" src="/assets/img/plugins/thespaghettidetective/screenshot6.png" />
    <div style="text-align: center; margin: 0 0 18px 0;">Full-screen webcam streaming</div>
  </div>
  <div class="span4">
    <img style="width: 200px; display: block; margin: auto;" src="/assets/img/plugins/thespaghettidetective/screenshot7.png" />
    <div style="text-align: center; margin: 0 0 18px 0;">Multiple printers at one glance</div>
  </div>
</div>


## Install and setup

Setting up The Spaghetti Detective is quite straightforward. Just install this plugin and follow the steps on the wizard screen and you will be all set.

If you run into any difficulties, check out the [Setup
Guide](https://help.thespaghettidetective.com/kb/guide/en/setup-the-spaghetti-detective-using-the-web-app-dbCcgiR0Tr/Steps/291120).

![wizard](/assets/img/plugins/thespaghettidetective/plugin_wizard.png "The Spaghetti Detective Set up Wizard")

## Does it cost anything?

Yes and No.

* First and foremost, The Spaghetti Detective is an [open source project](https://github.com/TheSpaghettiDetective). You can always grab the code and run the server yourself.
* If you want to skip the hassle and risk of setting up the server and exposing it to internet, you can use The Spaghetti Detective cloud. You can have a free account with limited service, or upgrade to a paid account for a couple coffees a month if you want unrestricted access and features. Check out the [pricing](https://app.thespaghettidetective.com/ent/pricing/).

<hr />

*Questions? Comments? Run into problems? [Reach out to us](mailto:support@thespaghettidetective.com).*
