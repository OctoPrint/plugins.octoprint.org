---
layout: plugin

id: buildbee
title: BuildBee Cloud Dock
description: Turns your Octoprint installation into a Cloud Dock and connects to BuildBee's super simple cloud printing service.
author: Me3D
license: AGPLv3

date: 2020-09-25

homepage: https://buildbee.com
source: https://octoprint-buildbee-source.buildbee.com
archive: https://octoprint-buildbee-source.buildbee.com/dist/OctoPrint-BuildBee-latest.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- cloud
- cloud printing
- remote access
- design management
- fleet management
- user management
- buildbee

screenshots:
- url: /assets/img/plugins/buildbee/buildbee_screen_1.png
  alt: BuildBee's model select screen, showing a series of 3D printing workflow steps, user uploaded models and controls. You can start print jobs from this screen.
  caption: Upload, share and start printing your models from anywhere with BuildBee
- url: /assets/img/plugins/buildbee/buildbee_screen_2.png
  alt: The buildbee printer maintenance panel replaces Octoprint's standard UI. This screen shows direct printer controls, including directional buttons and manual temperature overrides. There is also a Find Me button, which tells your printer to wave at you!
  caption: The Octoprint-BuildBee plugin connects your printer to the cloud, but your printer controls are still available in the local network.
- url: /assets/img/plugins/buildbee/buildbee_screen_3.png
  alt: BuildBee fast printing, high quality print parameter presets. On this screen, you choose a print quality preset, and optionally tweak settings like whether or not to use support, or print in fine detail.
  caption: Take advantage of BuildBee's print quality presets, or make your own. Tweaks make quick work of tiny changes from build to build.
- url: /assets/img/plugins/buildbee/buildbee_enterprise.png
  alt: Four views of BuildBee's enterprise tools, showing fleet monitoring analytics, print job queue management, printer fleet overview and a printer's detailed information screen.
  caption: Enterprise tools make it easy to manage a fleet of printers and many users in your school, office, makerspace and home.

featuredimage: /assets/img/plugins/buildbee/buildbee_featured.png

# You only need the following if your plugin requires specific OctoPrint versions or
# specific operating systems to function - you can safely remove the whole
# "compatibility" block if this is not the case.

compatibility:

  octoprint:
  - 1.3.4
  
  python: ">=2.7,<4"

---

## BuildBee CloudDock

Install this plugin to convert your Octoprint installation into a BuildBee CloudDock, connecting your printer to BuildBee's online services. You can then manage, monitor and print wirelessly to your OctoPrint enabled 3D printer from anywhere via [BuildBee.com](https://buildbee.com) or the BuildBee Desktop app.

---

<div style="text-align:center">
  <img style="text-align:center" src="/assets/img/plugins/buildbee/buildbee_feature.png" alt="BuildBee"/>
</div>

## What is BuildBee?

BuildBee is the simplest solution for managing 3D printing at home, schools, makerspaces, universities, small workshops and offices. Our aim is to make 3D printing accessible to everyone: no walls of inscrutable settings, no trawling forums to find out which G-code instruction turns the fan on, no gatekeepers. BuildBee streamlines the 3D printing process into a structured workflow to get new makers started building first and worrying about the minutiae of settings second.

## Getting started

Install the BuildBee plugin directly from the Octoprint plugin manager, or from the [latest bundle](https://octoprint-buildbee-source.buildbee.com). Reboot once the plugin is installed - congratulations, you have a CloudDock now!

### Add your CloudDock to a BuildBee account

[Log into BuildBee](https://app.buildbee.com/sign-in) or [create a new account](https://app.buildbee.com/create-account). Don't worry, it's _free_ unless you want to upgrade to use pro/enterprise features.

Take a second to run through the tour if this is your first time, then click on the printer tab ![BuildBee printer tab button icon](/assets/img/plugins/buildbee/printers_tab_button.png) at the top right. This is where your CloudDocks will appear when they're connected. You have a couple of options for connecting depending on whether your CloudDock is already connected to your network or if you need to connect through a proxy.

#### If you're running on OctoPi headless and you can't connect to your network easily

Click the printers button in the top bar, then the Add or Set Up Printer link. Choose the CloudDock option and follow the prompts to select the kind of network you'd like to connect to, then download a unique, encrypted configuration file.

Copy the configuration file onto a USB drive (FAT/ExFAT formatted), plug the USB drive into your OctoPi based CloudDock and cycle the power by unplugging the power from the raspberry/orange/whatever pi. The BuildBee plugin will remove the configuration file from the USB drive, connect to your network and bind to your BuildBee account using the credentials embedded in the config file. After a few minutes you should see your CloudDock appear in your BuildBee printers list. You'll also find that the config file has been removed from the USB drive and replaced with a log bundle that will indicate whether the configuration file was successful or not.

#### If your CloudDock is already connected to the internet and you just need to add it to your account

If you've added the BuildBee plugin to an existing OctoPrint installation that you could access over your local network or you're otherwise able to connect to your Octoprint instance directly via it's IP address in a browser or a zeroconf/bonjour name like `octoprint.local`, then your CloudDock is probably already connected to the internet.

In this case, simply log into your local octoprint interface as you did before, and you'll see the BuildBee Local Maintenance screen. If you see a line that says "Unregistered..." you can click the link to add this printer to your account - you'll be redirected back to [the BuildBee web app](https://app.buildbee.com/) with a one-time link and prompted to add the printer to whichever BuildBee account is currently logged in. Easy.

![If you are part of a multi-user enterprise or education team you can add the printer to your enterprise account](/assets/img/plugins/buildbee/buildbee_screen_add_printer.png)

### Select your printer type

By default your new CloudDock is setup with a printer profile for a [Me3D Me2](https://me3d.com.au) (BuildBee is developed by the team at Me3D. Hi there! 👋 ), but BuildBee now has built in profiles for a huge range of printers.

#### To change printer profiles

1. Make sure you're connected to the same network as your CloudDock.
2. From the printer list in the BuildBee app, click the `Maintenance` button (or, if you know the IP address of your CloudDock open a browser tab and navigate to `http://<ip address>:5000`)
3. Click the `System Info` button
4. Select your printer's manufacturer and model from the drop-down list.

Don't see your printer in the list? Let us know and we'll add it straight away. If you have a Cura or Slic3r friendly config file it should only take us a few business hours.

## What next?

Head over to [the BuildBee web app](https://app.buildbee.com/), log in, click the + button to add your files, select the material and quality presets you desire, then click print. That's it.

If you're having trouble getting a CloudDock up and running you can also try out the [BuildBee Desktop App](https://buildbee.com/landing/setup).

You can also:

- Control your 3D printer remotely, from any device with a browser.
- Securely store and sync your 3D models across all of your devices.
- Easily and securely share your 3D models with others.
- Manage groups of users with delegated access to printers and job queues.
- Monitor analytics for your fleet and all your users.
- Manage multiple kinds of 3D printers with ease.

and more…

Have fun! ❤️🐝