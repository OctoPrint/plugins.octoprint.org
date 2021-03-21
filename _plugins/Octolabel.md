---
layout: plugin

id: octolabel
title: OctoPrint-OctoLabel
description: Label printing plugin for OctoPrint
author: Lowie Goossens
license: MIT

date: 2020-03-19

homepage: https://github.com/LowieGoossens/octolabel
source: https://github.com/LowieGoossens/octolabel
archive: https://github.com/LowieGoossens/octolabel/archive/master.zip


tags:
- label
- notifications
- brother


compatibility:
  octoprint:
  - 1.4.2
  python: ">=2.7,<4"


  
---
OctoLabel is a plugin allowing Octoprint to print labels.

Work based on the amazing plugins [Octorant](https://plugins.octoprint.org/plugins/octorant/) by @bchanudet, [Octotweet](https://plugins.octoprint.org/plugins/octotweet/) by @Jean Pierre GARCIA, and the amazing api [label_api](https://github.com/pklaus/label_api) by @Philipp Klaus. 

### Install the plugin
Included in the folder [label print api](https://github.com/LowieGoossens/octolabel/tree/master/label_print_api), there you find the api writen by Philipp Klaus.
Run this api on a seperate raspberry connected to a brother label printer and modify the namebadge plugin.
It is possible to change the lettertype, textposition, of label type,...
It is important to change the ip-adres and printer settings in the file label_api (Do not change the port).

The following printers are claimed to be supported (✓ means verified by the author or by contributors):

QL-500 (✓), QL-550 (✓), QL-560 (✓), QL-570 (✓), QL-580N, QL-650TD, QL-700 (✓), QL-710W (✓), QL-720NW (✓), QL-800 (✓), QL-810W (✓), QL-820NWB (✓), QL-1050 (✓), and QL-1060N (✓).
The new QL-800 series can print labels with two colors (black and red) on DK-22251 labels.

Note: If your printer has an 'Editor Lite' mode, you need to disable it if you want to print via USB. Make sure that the corresponding LED is not lit by holding the button down until it turns off.

The available label names can be listed with `brother_ql info labels`:

     Name      Printable px   Description
     12         106           12mm endless
     29         306           29mm endless
     38         413           38mm endless
     50         554           50mm endless
     54         590           54mm endless
     62         696           62mm endless
     102       1164           102mm endless
     17x54      165 x  566    17mm x 54mm die-cut
     17x87      165 x  956    17mm x 87mm die-cut
     23x23      202 x  202    23mm x 23mm die-cut
     29x42      306 x  425    29mm x 42mm die-cut
     29x90      306 x  991    29mm x 90mm die-cut
     39x90      413 x  991    38mm x 90mm die-cut
     39x48      425 x  495    39mm x 48mm die-cut
     52x29      578 x  271    52mm x 29mm die-cut
     62x29      696 x  271    62mm x 29mm die-cut
     62x100     696 x 1109    62mm x 100mm die-cut
     102x51    1164 x  526    102mm x 51mm die-cut
     102x152   1164 x 1660    102mm x 153mm die-cut
     d12         94 x   94    12mm round die-cut
     d24        236 x  236    24mm round die-cut
     d58        618 x  618    58mm round die-cut


### Label Settings
Here you can customize the timing of every Label handled by OctoPrint.

![screen octolabel setup 1](/assets/img/plugins/octolabel/setup1.png)
![screen octolabel setup 1](/assets/img/plugins/octolabel/setup2.png)

- **Toggle the message** : by unchecking the checkbox in front of the time title, you can disable printing the label.
- **Message** : you can change the default content here. See the section [Message format](#message-format) for more information.
- **Notify every `XX`%** : specific to the `printing progress` message, this setting allows you to change the frequency of the notification:
    - `10%` means you'll receive a message at 10%, 20%, 30%, 40% ... 80%, 90% of the printing process.
    - `5%` means you'll receive a message at 5%, 10%, 15%, 20% ... 80%, 85%, 90%, 95% of the printing process.
    - etc.

### Scripts Settings

OctoLabel allows you to launch scripts everytime a message is sent:

- Before sending: perfect for turning some LED on to ensure the webcam will always have enough light when taking the snapshot.
- After sending: perfect for turning the same LED off :smiley:.

Script configuration was deliberately made a little harder, as running scripts exposes much more of the host computer. You can find more information on the [OctoRatn wiki](https://github.com/bchanudet/OctoPrint-Octorant/wiki/Launching-scripts).

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
