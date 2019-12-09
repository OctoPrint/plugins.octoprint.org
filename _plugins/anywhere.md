---
layout: plugin

id: anywhere
title: OctoPrint Anywhere
description: Remote monitoring and control of your 3D printers over the internet. ANYWHERE. ON YOUR PHONE. No more port forwarding or VPN.
author: Kenneth Jiang
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2017-07-01

homepage: https://github.com/kennethjiang/OctoPrint-Anywhere
source: https://github.com/kennethjiang/OctoPrint-Anywhere
archive: https://github.com/kennethjiang/OctoPrint-Anywhere/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- remote
- monitor
- monitoring
- phone
- control
- webcam
- port forwarding
- internet

featuredimage: /assets/img/plugins/anywhere/screenshot1.png

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
  - 1.3.2

  # List of compatible operating systems
  #
  # Possible values:
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
<p style="color: red; font-weight: bolder">Please note: OctoPrint Anywhere will be succeeded by <a class="link" style="color: #007bff;" href="https://plugins.octoprint.org/plugins/thespaghettidetective/">The Spaghetti Detective</a>, a faster and more powerful remote monitoring tool. It also detects print failures using AI. We strongly urge you to install that plugin instead.</p>

## Why OctoPrint Anywhere?

Do you want to have a quick glance at the realtime webcam feed of your running print while you are at work, grocery-shopping, or from any place with internet access?

Do you wish you had an easy way to remotely adjust the temperature, cancel or pause the print in case things go wrong, all from your phone?

**If so, OctoPrint Anywhere is for you.**

OctoPrint Anywhere streams the webcam feed, bed/nozzle temperature, and other critical status from your 3D printer to your phone via the internet. Now you don't have to be on the same WiFi network as the OctoPrint to monitor and control your 3D printer. No more messing with your router to set up port forwarding (a security risk too) or VPN.

## Highlights of OctoPrint Anywhere

* Webcam feed on your phone. Extremely low latency (usually <3s).
* Real-time feed on temperatures and status of active print. Pause or cancel the active print.
* Bandwidth-efficiency. Streams data only when you are watching. Data transmission immediately stops when browser tab goes to background.
* Sharing realtime webcam feed with your friends with an encrypted link!
* Access to your timelapses anywhere so that you can show them off! Sharing them too!
* Remote control of X/Y/Z movement.
* Seeing the IP address of your OctoPrint.
* Check status of all your 3D printers on the same page at a glance.
* Many more to come...

## Screenshots

<div class="row">
    <div class="span6">
        <img src="/assets/img/plugins/anywhere/screenshot1.png" alt="Webcam Feed"/>
        <div style='text-align: center; margin: 8px 0px 24px 0px;'>
            <i>Webcam Feed</i>
        </div>
    </div>
    <div class="span6">
        <img src="/assets/img/plugins/anywhere/screenshot2.png" alt="Print Status Control"/>
        <div style='text-align: center; margin: 8px 0px 24px 0px;'>
            <i>Print Status Control</i>
        </div>
    </div>
</div>
<div class="row">
    <div class="span6">
        <img src="/assets/img/plugins/anywhere/screenshot3.png" alt="Webcam Sharing"/>
        <div style='text-align: center; margin: 8px 0px 24px 0px;'>
            <i>Webcam Sharing</i>
        </div>
    </div>
    <div class="span6">
        <img src="/assets/img/plugins/anywhere/screenshot5.png" alt="Temperature Adjustment"/>
        <div style='text-align: center; margin: 8px 0px 24px 0px;'>
            <i>Temperature Adjustment</i>
        </div>
    </div>
</div>
<div class="row">
    <div class="span12">
        <img src="/assets/img/plugins/anywhere/screenshot4.png" alt="On iPad or Laptop"/>
        <div style='text-align: center; margin: 8px 0px 24px 0px;'>
            <i>On iPad or Laptop</i>
        </div>
    </div>
</div>

## Installation And Setup In 6 Easy Steps

<div class="row">
    <img src="/assets/img/plugins/anywhere/setup_screenshot0.png" alt="Step 1"/>
    <div style='text-align: center; margin: 8px 0px 48px 0px;'>
        <i>Step 1</i>
    </div>
</div>
<div class="row">
    <img src="/assets/img/plugins/anywhere/setup_screenshot1.png" alt="Step 2"/>
    <div style='text-align: center; margin: 8px 0px 48px 0px;'>
        <i>Step 2</i>
    </div>
</div>
<div class="row">
    <img src="/assets/img/plugins/anywhere/setup_screenshot2.png" alt="Step 3"/>
    <div style='text-align: center; margin: 8px 0px 48px 0px;'>
        <i>Step 3</i>
    </div>
</div>
<div class="row">
    <img src="/assets/img/plugins/anywhere/setup_screenshot3.jpg" alt="Step 4"/>
    <div style='text-align: center; margin: 8px 0px 48px 0px;'>
        <i>Step 4</i>
    </div>
</div>
<div class="row">
    <img src="/assets/img/plugins/anywhere/setup_screenshot4.png" alt="Step 5"/>
    <div style='text-align: center; margin: 8px 0px 48px 0px;'>
        <i>Step 5</i>
    </div>
</div>
<div class="row">
    <img src="/assets/img/plugins/anywhere/setup_screenshot5.jpg" alt="Step 6"/>
    <div style='text-align: center; margin: 8px 0px 48px 0px;'>
        <i>Step 6</i>
    </div>
</div>

Questions? Comments? [Email k@getanywhere.io](mailto:k@getanywhere.io)
