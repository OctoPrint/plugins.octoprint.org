---
layout: plugin

id: octotweet
title: OctoPrint-Octotweet
description: Twitter plugin for OctoPrint
author: Jean Pierre GARCIA
license: MIT

compatibility:
  octoprint:
  - 1.4.2
  python: ">2.7,<4"


# TODO
date: 2020-08-08

homepage: https://github.com/jpg32/OctoPrint-Octotweet
source: https://github.com/jpg32/OctoPrint-Octotweet
archive: https://github.com/jpg32/OctoPrint-Octotweet/archive/master.zip

# tags
tags:
- twitter
- notifications
- snapshots

# screenshots
screenshots:
- url: /assets/img/plugins/octotweet/twitter.jpg
  alt: Post octoprint's events on Twitter
  caption: Post octoprint's events on Twitter
- url: /assets/img/plugins/octotweet/settings.jpg
  alt: Customize the text Octotweet sends to Twitter
  caption: Customize the text Octotweet sends to Twitter

# Featured image
featuredimage: /assets/img/plugins/octotweet/twitter.jpg

attributes:
- cloud

---

# Octoprint-OctoTweet 1.0.0

OctoTweet is a plugin allowing Octoprint to send notifications to Twitter.
This is a fork of the amazing plugin [Octorant](https://plugins.octoprint.org/plugins/octorant/) by @bchanudet.

![twitter result](/assets/img/plugins/octotweet/twitter.jpg)


## SETUP
### Install the plugin
Install manually using this url :
https://github.com/jpg32/OctoPrint-Octotweet/archive/master.zip

### Create Twitter App
Login with your Twitter account on [developer.twitter.com](https://developer.twitter.com/en).

Click on *App* and then on *Create an app*:
![screen twitter setup 1](/assets/img/plugins/octotweet/twitter_setup_1.JPG)

Select *Student*:
![screen twitter setup 2](/assets/img/plugins/octotweet/twitter_setup_2.JPG)

Follow steps to complete the subscription to Twitter's Developer Program:
![screen twitter setup 3](/assets/img/plugins/octotweet/twitter_setup_3.JPG)

Now you can create a new app:
![screen twitter setup 4](/assets/img/plugins/octotweet/twitter_setup_4.JPG)

The next step show you your API Key & API secret keys:
![screen twitter setup 4](/assets/img/plugins/octotweet/twitter_setup_5.JPG)

Copy them to the OctoTweet plugin configuration:
![screen octoprint 1](/assets/img/plugins/octotweet//octoprint_1.JPG)

Edit app's permissions:
![screen twitter setup 6](/assets/img/plugins/octotweet/twitter_setup_6.JPG)
![screen twitter setup 7](/assets/img/plugins/octotweet/twitter_setup_7.JPG)

Go to *Keys and tokens* :
![screen twitter setup 8](/assets/img/plugins/octotweet/twitter_setup_8.JPG)

Generate *Access Token & Secret*:
![screen twitter setup 11](/assets/img/plugins/octotweet/twitter_setup_11.JPG)

Copy generated tokens to Octoprint :
![screen twitter setup 4](/assets/img/plugins/octotweet/twitter_setup_12.JPG)
![screen twitter setup 5](/assets/img/plugins/octotweet/octoprint_2.JPG)

### Message Settings

Here you can customize every message handled by Octoprint.

- **Toggle the message** : by unchecking the checkbox in front of the message title, you can disable the message. It won't be sent to Twitter.
- **Message** : you can change the default content here. See the section [Message format](#message-format) for more information.
- **Include snapshot** : if you have a snapshot URL defined in the Octoprint settings, you can choose to upload a snapshot with the message to Twitter.
- **Notify every `XX`%** : specific to the `printing progress` message, this setting allows you to change the frequency of the notification :
    - `10%` means you'll receive a message at 10%, 20%, 30%, 40% ... 80%, 90% of the printing process.
    - `5%` means you'll receive a message at 5%, 10%, 15%, 20% ... 80%, 85%, 90%, 95% of the printing process.
    - etc.

### Scripts Settings

Octotweet allows you to launch scripts everytime a message is sent:

- Before sending: perfect for turning some LED on to ensure the webcam will always have enough light when taking the snapshot.
- After sending: perfect for turning the same LED off :smiley:.

Script configuration was deliberately made a little harder, as running scripts exposes much more on the host computer. You can find more indications on the [wiki](https://github.com/bchanudet/OctoPrint-Octorant/wiki/Launching-scripts).

## Message format

Messages are regular twitter messages, which means you can use:
- `:emoji:` shortcuts to display emojis.
- `@mentions` to notify someone.

Some events also support variables, here is a basic list:

**Printing process : started event**
- `{name}`: name of the file that is being printed
- `{path}`: path of the file in its origin location
- `{origin}`: the origin storage location

**Printing process : failed event**
- `{name}`: name of the file that is being printed
- `{path}`: path of the file in its origin location
- `{origin}`: the origin storage location

**Printing process : done event**
- `{name}`: name of the file that is being printed
- `{path}`: path of the file in its origin location
- `{origin}` : the origin storage location
- `{time}`: time needed for the print (in seconds)
- `{time_formatted}` : same as `{time}`, but in a human-readable format (`HH:MM:SS`)

**Printing process : failed event**
- `{name}`: name of the file that is being printed
- `{path}`: path of the file in its origin location
- `{origin}`: the origin storage location
- `{position}`: position of the hotend

**Printing process : paused event**
- `{name}`: name of the file that is being printed
- `{path}`: path of the file in its origin location
- `{origin}`: the origin storage location
- `{position}`: position of the hotend

**Printing process : resumed event**
- `{name}`: name of the file that is being printed
- `{path}`: path of the file in its origin location
- `{origin}`: the origin storage location
- `{position}`: position of the hotend

**Printing progress event**
- `{progress}` : progress in % of the print
- `{spent}`: time spent since the start of the print (in seconds)
- `{spent_formatted}` : same as `{spent}`, but in a human-readable format (`HH:MM:SS`)
- `{remaining}`: time remaining until the end of the print (in seconds)
- `{remaining_formatted}` : same as `{remaining}`, but in a human-readable format (`HH:MM:SS`)

**Printer state : error**
- `{error}` : The error received

For more reference, you can go to the [Octoprint documentation on Events](http://docs.octoprint.org/en/master/events/index.html#sec-events-available-events).
