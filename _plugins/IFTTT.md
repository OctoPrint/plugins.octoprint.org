---
layout: plugin

id: IFTTT
title: OctoPrint-IFTTT
description: Connects OctoPrint events to IFTTT
author: T6
license: AGPLv3

date: 2018-12-29

homepage: https://github.com/tjjfvi/OctoPrint-IFTTT
source: https://github.com/tjjfvi/OctoPrint-IFTTT
archive: https://github.com/tjjfvi/OctoPrint-IFTTT/archive/master.zip

tags:
- notification
- iot
- ifttt
- tp-link
- tplink

screenshots:
- url: /assets/img/plugins/IFTTT/settings.png
  alt: OctoPrint-IFTTT Settings
  caption: OctoPrint-IFTTT Settings

compatibility:
  python: ">=2.7,<4"
  
---

*Note: this plugin has not been tested with versions under 1.3.10; they may not work!*

## Advantages:
 - Allows for multiple IFTTT accounts to be connected
 - Allows for multiple triggers for each event
 - Allows customization of Value[1-3] placeholders; either static or a property of the event payload
 - Allows for default prefixes so you don't have to type in lots of triggers
 - Works with custom events!_*_

_*May not be (officially) supported; see [#2965](https://github.com/foosel/OctoPrint/issues/2965) for more info._

## Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/tjjfvi/OctoPrint-IFTTT/archive/master.zip

## Configuration

### Makerkeys
A unique API key for IFTTT. Go [here](https://ifttt.com/maker_webhooks) and click on "Documentation". On the documentation page it will tell you your key: "Your key is: ...". You can put multiple makerkeys, seperated by newlines, here.

### Default prefixes
Default prefixes for the triggers. If you have an event `MyEvent` and prefixes `prefix1-` and `prefix2-`, it will, by default make the triggers `prefix1-MyEvent` and `prefix2-MyEvent`. Seperate the prefixes with newlines.

### Events
Define events to send to IFTTT.

#### Triggers
A list of triggers to trigger on IFTTT.

#### Values
IFTTT Webhooks allows for a payload with three values. It will interpret this string like so:
 - If the value begins with a dot (`.`), it will use that prop of the event payload (e.g. `.name` for `PrintDone`)
 - If it begins with a colon (`:`) it will use the string after the colon
 - Otherwise it will just send the plain text
