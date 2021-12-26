---
layout: plugin

id: BLOCKS
title: Blocks
description: Theme for Blocks 3D printers and extended functionalities.
authors:
- Hugo C. Lopes Santos Costa
license: AGPLv3

date: 2021-12-24

homepage: https://github.com/HugoCLSC/OctoPrint-BLOCKS
source: https://github.com/HugoCLSC/Octoprint-BLOCKS
archive: https://github.com/HugoCLSC/Octoprint-BLOCKS/archive/main.zip

tags:
- wifi
- UI
- Grid
- theme
- Blocks Printers
- Notifications

screenshots:
- url: /assets/img/plugins/BLOCKS/wifi_screenshot.jpg
  alt: New wifi connection
  caption: Wifi configuration
- url: /assets/img/plugins/BLOCKS/ScreenShot1.PNG
  alt: Light Disconnected
  caption: Light
- url:  /assets/img/plugins/BLOCKS/ScreenShot2.PNG
  alt: Dark Disconnected
  caption: Dark
- url:  /assets/img/plugins/BLOCKS/ScreenShot3.PNG
  alt:  Light Connected
  caption: Light connected
- url:  /assets/img/plugins/BLOCKS/ScreenShot4.PNG
  alt:  Dark Connected
  caption: Dark connected




compatibility:

  octoprint:
  - 1.7.2

  os:
  - linux

  python: ">=3.3,<4"

featuredimage: /assets/img/plugins/BLOCKS/Blocks_VECTORIZADOpreto.png

---
## About
- This plugin was made with the intention of offering a different experience to users with Blocks 3D printers.
The plugin reorganizes the user interface in order to display all relevant information in a grid.
Adding to this, users can also add new network connections with Octoprint!

- This functionality works best with the automatic creation of hotspots on a raspberry pi when no internet connection was made.
Check out https://medium.com/@kennethjiang/painless-wi-fi-for-octoprint-4e6b68005400 for more information about that.

- If the 3D printer is from Blocks additional functionality is available.
For example, if run with the Blocks R21 printer additional wifi reporting from octoprint to the printer is enabled.

- The plugin is in constant development.

## More
### Known Issues
- There are some compatibility issues with other plugins on the repository.
An example of this are plugins that make use of the classic octoprint control tab and the consolidated tabs plugin

### Get Help
- Any issues or requests can be made on the main homepage located on the right.


### Acknowledgments
- I'd like to express my gratitude to the OctoPrint devs and the community.
- I recommend joining the official discord channel for OctoPrint, help is always given to those who ask.


- Used and studied the code from:

 https://github.com/LazeMSS/OctoPrint-UICustomizer/
 https://github.com/ManuelMcLure/OctoPrint-WiFiStatus/


## Also See
[![Blocks](/assets/img/plugins/BLOCKS/tinyBlocks.png)](https://www.blockstec.com/)
[![Youtube](/assets/img/plugins/BLOCKS/youtube_icon.png)](https://www.youtube.com/c/BlocksTec)
[![Instagram](/assets/img/plugins/BLOCKS/instagram_icon.png)](https://www.instagram.com/blockstec/)
[![Twitter](/assets/img/plugins/BLOCKS/twitter_icon.png)](https://twitter.com/blockstec)
[![Facebook](/assets/img/plugins/BLOCKS/facebook_icon.png)](https://www.facebook.com/blockstec)
