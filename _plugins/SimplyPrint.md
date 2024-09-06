---
layout: plugin

id: SimplyPrint
title: SimplyPrint Cloud
description: 3D print online anywhere; elevate your 3D printing experience from your computer or phone, with smart features like filament manager, livestream, print queue, and much more. Simple, beautiful, smart.
authors:
- SimplyPrint
license: GNU General Public License v3.0

date: 2021-02-02

homepage: https://simplyprint.io/
source: https://github.com/SimplyPrint/OctoPrint-SimplyPrint/
archive: https://github.com/SimplyPrint/OctoPrint-SimplyPrint/archive/master.zip

privacypolicy: https://simplyprint.io/legal/en/privacy

tags:
- cloud
- simplyprint
- remote monitoring
- remote access
- print local files
- print queue
- control
- webcam

screenshots:
- url: /assets/img/plugins/SimplyPrint/control_panel.png
  alt: SimplyPrint printer control panel
  caption: The SimplyPrint control panel for your 3D printer

- url: /assets/img/plugins/SimplyPrint/filament_management.png
  alt: SimplyPrint filament management system
  caption: Keep track of all your filament and how much there's left

- url: /assets/img/plugins/SimplyPrint/file_system.png
  alt: SimplyPrint file manager
  caption: Store all your 3D files securely in the cloud, and access them anywhere

- url: /assets/img/plugins/SimplyPrint/statistics.png
  alt: SimplyPrint statistics
  caption: See statistics for your 3D print

featuredimage: /assets/img/plugins/SimplyPrint/showcase_feature_image.png

compatibility:
  python: ">=2.7,<4"

attributes:
- cloud
- commercial
- free-tier

---

# Connect your printer to the SimplyPrint cloud in minutes
{% include youtube.html vid="_Kd8KhLn1Rc" preview="https://i.ytimg.com/vi/_Kd8KhLn1Rc/maxresdefault.jpg" %}

Installing SimplyPrint on your Raspberry Pi instantly elevates your 3D printing experience. You will get full control of your printer from anywhere in the world.

- Manage multiple printers from one unified panel
- Start, stop, pause and monitor your prints from anywhere _(see webcam, estimated finish, current print %)_
- Use a slicer that knows your printer, and what filament is in use
- Manage your filament from the filament management system
- Bring your 3D files with you anywhere, in your personal, secure file storage
- Queue the prints you can't wait to print!
- _And much more..._

Read more about SimplyPrint and its features on [https://simplyprint.io/](https://simplyprint.io/?utm_source=octoprint)

# SimplyPrint installation

![installation](/assets/img/plugins/SimplyPrint/installation.gif "The SimplyPrint installation")
- Install the `SimplyPrint Cloud` plugin
- Follow the instruction that appears after install _(finish install on the [SimplyPrint website](https://simplyprint.io/?utm_source=octoprint))_
- You're done in less than 2 minutes!

## Companion app

Bring your printer with you in your pocket, at all times, using our Android or iOS app.

![app](/assets/img/plugins/SimplyPrint/app.gif "The SimplyPrint app")

## Does it cost anything?
We have a **free** plan called "Basic", which will remain free forever. This plan includes the use of 2 printers connected to the cloud, accessible even when you're not home.

For those who want a little more out of their 3D printer, we have two subscription plans with features like; _smart filament changing, smart-rotation in slicer, up to 1 FPS webcam stream, SMS notifications, statistics, print queue_ & much more

See the full list of features that our different subscription plans have on the [SimplyPrint website](https://simplyprint.io/?utm_source=octoprint).


## Future plans for SimplyPrint

We have _a lot_ of stuff planned for the near future, we're **still in beta**, so this is just the beginning!
Check out our public roadmap at; [https://simplyprint.io/roadmap](https://simplyprint.io/roadmap?utm_source=octoprint)

<hr />

## How does SimplyPrint change OctoPrint?

To enhance the user experience as much as possible, SimplyPrint takes control of two core OctoPrint features;
- **GCODE scripts**
    - If you use the _"GCODE scripts"_ feature, the _"cancel", "pause"_ and "resume" GCODE scripts will be syncronized to SimplyPrint and stored in our _"GCODE profiles"_ system. So they won't disappear, you'll just have to modify them via the SimplyPrint platform instead.
- **Printer profiles**
    - When you select which printer you have in SimplyPrint, we know what its details are _(print volume, nozzle, etc.)_, and you can modify it as much as you want. We **automatically create a printer profile** with all the details your printer has in SimplyPrint, and set it as your default profile. Your old profile(s) will _not_ be removed :)
- **_That's it!_** You can use OctoPrint just like before. There's even a _"Go to OctoPrint"_ button on your printer, that takes you to OctoPrint when you're on the same network as your Pi. When you're out, SimplyPrint has got your back!


### Questions, comments or want to join the community?

We have a live chat support on our website _(open 5 hours all week days, in our local timezone, GMT+1, sorry, we're just 3 guys on the project, living in Denmark :))_. You can also always [send us an email at contact@simplyprint.io](mailto:contact@simplyprint.io)

Also, come hang out with us in our [Facebook group](https://facebook.com/groups/simplyprint/)! A strong community is important to us, and we always listen to suggestions _(and often implement them),_ we and usually fix problems _lighning fast_ ;)


<a href="https://www.facebook.com/simplyprintDK"><i class="fab fa-facebook fa-2x" style="color:#29ABE2;"></i></a>&nbsp;<a href="https://www.youtube.com/channel/UC-fVuu_ny14RV3COTi0CVDw"><i class="fab fa-youtube-square fa-2x" style="color:#29ABE2;"></i></a>&nbsp;<a href="https://twitter.com/SimplyPrint3D"><i class="fab fa-twitter-square fa-2x" style="color:#29ABE2;"></i></a>
