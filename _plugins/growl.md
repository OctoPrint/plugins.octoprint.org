---
layout: plugin
id: growl
title: Growl
description: Get Growl notifications from your OctoPrint installation.
author: Gina Häußge
source: https://github.com/OctoPrint/OctoPrint-Growl
archive: https://github.com/OctoPrint/OctoPrint-Growl/archive/master.zip 
screenshots:
- url: https://i.imgur.com/glZq5zJ.png
  alt: Settings dialog
  caption: Growl plugin settings dialog
- url: https://i.imgur.com/cqYpfR4.png
  alt: Example notification
  caption: Example notification for a started print job
featuredimage: https://i.imgur.com/cqYpfR4.png
date: 2015-04-14
tags: 
- notification
---

The Growl plugin for OctoPrint allows to send notifications about certain printing events to a Growl instance on your
local network. Right now it sends notifications for the following events:
 
  * Printjob started
  * Printjob done
  * File uploaded (optional)
  * Timelapse done (optional)
 
Please note that it's a work in progress.

## Configuration

You'll have to configure the host your Growl service is running on (which is probably not the same machine that 
your OctoPrint installation is running on), the port it is listening on and - if you secured your growl instance against
notifications from the network with a password - also the password needed to connect to it.

You can do all this via the settings dialog under "Plugins > Growl". If you have your OctoPrint installation's 
[bundled discovery plugin](https://github.com/foosel/OctoPrint/wiki/Plugin:-Discovery) also 
[configured with pybonjour support](https://github.com/foosel/OctoPrint/wiki/Plugin:-Discovery#installing-pybonjour) 
you'll also be able to see all the Growl instances on your local network that OctoPrint was able to discover there.

By default only the notifications for "Printjob started" and "Printjob done" are enabled. If you also want to get 
notification about the other events, you'll have to **tell Growl**. OctoPrint will send them all, but your local Growl
instance needs to be told to also display them. You can do this in the configuration of your Growl service. For example,
this is how it looks in [Growl for Windows](http://www.growlforwindows.com/gfw/):

![Growl Plugin: Example of granular notification configuration in Growl for Windows](http://i.imgur.com/Z0wJy8Bl.png)
