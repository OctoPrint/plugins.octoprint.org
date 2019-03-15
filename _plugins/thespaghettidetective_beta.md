---
layout: plugin

id: thespaghettidetective_beta
title: The Spaghetti Detective (Beta)
description: AI-based open source project for 3D printing failure detection.
author: The Spaghetti Detective Team
license: AGPLv3

# TODO
date: 2019-03-15

homepage: https://www.thespaghettidetective.com
source: https://github.com/TheSpaghettiDetective/OctoPrint-TheSpaghettiDetective
archive: https://github.com/TheSpaghettiDetective/TheSpaghettiDetective/archive/beta.zip

# TODO
# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on PyPi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

# TODO
tags:
- AI
- Machine Learning
- remote
- monitoring
- alert
- webcam

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
  - 1.3.2

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

* Can't sleep well whenever your 3D printer is printing at night?
* Compulsive at checking your prints every 10 minutes?

[The Spaghetti Detective](https://www.thespaghettidetective.com) constantly watches your prints in the background so you don't have to.

{% include youtube.html vid="ZpDw9mNBngU" preview="'/assets/img/plugins/thespaghettidetective_beta/video_preview1.png'" %}

<br />

## Sounds cool! But how does it work?

<div class="row">
  <div class="span9 offset1" style="display: flex;">
    <div style="display: flex; flex-flow: column; align-items: center; justify-content: space-between; padding: 0 24px;">
      <img style="max-width: 75px; max-height: 75px; margin-bottom: 16px; vertical-align: middle;" alt="Webcam" src="/assets/img/plugins/thespaghettidetective_beta/webcam.png">
      <i class="fas fa-arrow-down fa-3x" style="color: #6c757d;"></i>
    </div>
    <div>
      <h4>Capture</h4>
      <div style="color: #6c757d;">Webcam captures real time 3D print images and sends them to The Spaghetti
        Detective.</div>
    </div>
  </div>
</div>
<div class="row">
  <div class="span9 offset1" style="display: flex;">
    <div style="display: flex; flex-flow: column; align-items: center; justify-content: space-between; padding: 0 24px;">
      <img style="max-width: 75px; max-height: 75px; margin: 16px 0px; vertical-align: middle;" alt="Gauge" src="/assets/img/plugins/thespaghettidetective_beta/gauge.png">
      <i class="fas fa-arrow-down fa-3x" style="color: #6c757d;"></i>
    </div>
    <div style="margin-top: 16px;">
      <h4>Gauge</h4>
      <div style="color: #6c757d;">The Spaghetti Detective gauges the likelihood of a failure by analyzing the images.</div>
    </div>
  </div>
</div>
<div class="row">
  <div class="span9 offset1" style="display: flex;">
    <div style="display: flex; flex-flow: column; align-items: center; justify-content: space-between; padding: 0 24px;">
      <img style="max-width: 75px; max-height: 75px; margin: 16px 0px; vertical-align: middle;" alt="Alert" src="/assets/img/plugins/thespaghettidetective_beta/icon_sms.png">
      <i class="fas fa-arrow-down fa-3x" style="color: #6c757d;"></i>
    </div>
    <div style="margin-top: 4px;">
      <h4>Alert</h4>
      <div style="color: #6c757d;">If a possible failure is detected, it will pause the printer, turn off the heaters,
        and alert you via email or text.</div>
    </div>
  </div>
</div>
<div class="row">
  <div class="span9 offset1" style="display: flex;">
    <div style="display: flex; flex-flow: column; align-items: center; justify-content: space-between; padding: 0 24px;">
      <img style="max-width: 75px; max-height: 75px; margin: 16px 0px; vertical-align: middle;" alt="Save" src="/assets/img/plugins/thespaghettidetective_beta/save.png">
    </div>
    <div style="margin-top: 2px;">
      <h4>Save</h4>
      <div style="color: #6c757d;">You cancel the print from your phone if failure is confirmed. Save time, $, and
        your worries.</div>
    </div>
  </div>
</div>

## Install and setup

Setting up The Spaghetti Detective is quite striaghtforward. Just install this plugin and follow the steps on the wizard screen and you will be all set.

![wizard](/assets/img/plugins/thespaghettidetective_beta/plugin_wizard.png "The Spaghetti Detective Set up Wizard")

If you run into any difficulties, check out the [Setup Guide](https://thespaghettidetective.com/guide.html).

## Does it cost anything?

Yes and No.

* First and foremost, The Spaghetti Detective is an [open source project](https://github.com/TheSpaghettiDetective). You can always grab the code and run the server yourself. Commercial use of the source code is restricted.
* If you want to skip the hassle of setting up the server, you can use The Spaghetti Detective cloud, which will be free to all beta testers during beta testing.
* After we come out of beta, you can choose to stay as a free account with limited service, or upgrade to a paid account if you want unrestricted access and features. Check out [how the future pricing will look like](https://www.thespaghettidetective.com/#pricing).

## Will it work for me?

The Spaghetti Detective is still at its very beginning so it doesn't always get it right. But many beta testers have already written to us and told us "hey it worked!". Here are a few time-lapses from our beta testers:

{% include youtube.html vid="znI9_Vs6X9c" preview="'/assets/img/plugins/thespaghettidetective_beta/video_preview2.png'" %}
From beta tester **Torsten**

{% include youtube.html vid="btNtCFfFYk0" preview="'/assets/img/plugins/thespaghettidetective_beta/video_preview3.png'" %}
From beta tester **Lila**

If you can't have enough spaghetti (pun intended), head to our [Spaghetti Gallery](https://app.thespaghettidetective.com/publictimelapses/) for more time-lapses.

*Questions? Comments? Run into problems? [Reach out to us](mailto:support@thespaghettidetective.com).*

<hr />

**Support us by liking us or following us on social media:** &nbsp;<a href="https://www.facebook.com/pg/thespaghettidetective/posts/"><i class="fab fa-facebook fa-2x" style="color: rgb(121, 53, 241);"></i></a>&nbsp;<a href="https://www.youtube.com/channel/UCbAJcR6t5lrdZ1JXjPPRjGA/featured?view_as=subscriber"><i class="fab fa-youtube-square fa-2x" style="color: rgb(121, 53, 241);"></i></a>&nbsp;<a href="https://twitter.com/thespaghettispy"><i class="fab fa-twitter-square fa-2x" style="color: rgb(121, 53, 241);"></i></a>
