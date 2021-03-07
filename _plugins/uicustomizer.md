---
layout: plugin

id: uicustomizer
title: UI Customizer
description: Customize Octoprint with 5+ awesome themes, webcam and gcode widgets, rearrange layout and support mobile/tablets and much more...
authors:
- Mikkel Skovgaard
license: AGPLv3


date: 2020-11-30

homepage: https://github.com/LazeMSS/OctoPrint-UICustomizer
source: https://github.com/LazeMSS/OctoPrint-UICustomizer
archive: https://github.com/LazeMSS/OctoPrint-UICustomizer/archive/main.zip


tags:
- theme
- themes
- skin
- skins
- dark
- style
- styling
- responsive
- mobile
- webcam
- zoom
- fixed
- settings

screenshots:
- url: /assets/img/plugins/uicustomizer/responsive.png
  alt: overview
  caption: responsive layouts
- url: /assets/img/plugins/uicustomizer/camwidget.png
  alt: overview
  caption: Overview with webcam widget on the right
- url: /assets/img/plugins/uicustomizer/floating.png
  alt: floating webcam
  caption: Floating resizeable webcam overlay
- url: /assets/img/plugins/uicustomizer/settings.png
  alt: theme
  caption: Select themes


featuredimage: /assets/img/plugins/uicustomizer/responsive.png

---
## UI Customizer
![feature](/assets/img/plugins/uicustomizer/responsive.png)

A [OctoPrint](https://github.com/foosel/OctoPrint) plugin that allows you to customize the look and feel of the user interface.
It also features a lot of other fixes and improvements:
* Themes/skins - choose between 6 themes and more are coming soon
* Customize tabs: Change icon, labels, order, show/hide
* Change width of the columns
* Sort the order to icons in the menu bar (top icons)
* Move "widgets" around in columns
* Turn on/off responsive layout
* Improved settings window
* Fixed header/topbar
* Fixed footer/bottombar
* Fluid/full width layout
* Hide temperature background graphics
* Zoomed/Floating webcam option
* Extra Webcam "widget"
* Extra Gcode viewer "widget"
* [Compact Navbar temp](https://plugins.octoprint.org/plugins/navbartemp/) icons
* Hide widgets
* Hide main camera
* Center top bar icons
* Realtime preview of changes

### Setup

Install via the bundled [Plugin Manager](https://github.com/foosel/OctoPrint/wiki/Plugin:-Plugin-Manager)
or manually using this URL:

    https://github.com/LazeMSS/OctoPrint-UICustomizer/archive/main.zip


### Configuration
The configuration is split into 6 tabs - all have an preview option in the top right menu

#### General
* Improve mobile/responsive - enable the improved responsive modes including settings for mobile screens etc.
* Fluid/full width layout - should the entire screen width be used or not
* Fixed header/topbar - should the top menubar stay fixed when scrolling or not
* Hide temp. graph background - Hide temperature background graphics
* Fixed footer/bottombar - should the bottom bar stay fixed when scrolling or not
* Hide main camera - should the main camera be hidden - only acive if the webcam widget is enabled
* Compact menu - should the "dropdown" menu be a single compact menu
* Zoom/float webcam icon - will add an zoom icon to the webcam live feed that will popup out the webcam video feed into a floating resizeable overlay
* Gcode full-size - maximize the main gcode viewer to take up as much space as possible
* Compress temp. controls - compress/minimize the temperature controls in the temperature main tab

#### Themes
Select a theme - notice you can enable preview and see the theme in a realtime preview


#### Layout
The layout of the screen can be made into 1,2 or 3 columns and the size of the columns can be adjusted. The total width of the columns added together must not be greater than 12. Each column can contain zero or more widgets, widgets are the diffent "containers" for all the user interface, ie. the webcam, files etc.
If you want a two or one column layout then just drag the "widgets" all the widgets into the left hand side columns.
Each widget can be moved by draging. The widgets can also be hidden by clicking the eye on the right hand side of the widget.
Notice there is 2 extras widgets include with UI Customizer:
- Webcam widget which allows you to have a webcam outside the main tabs
- Gcode widget which allows you to have a gcode viewer outside the main tabs

#### Main tabs
The main/center tabs can be changed using this settings panel.
* The up and down arrow is used to change the order of the tabs when they are displayed
* The first field is for entering a custom name for the tab, if left blank it will use default.
* The "eye" icon can show or hide the entire tab and its content - click to toggle show/hide.
* The next icon is used to the change the icon and color of icon, shown in the tab. If no icon is selected then a blue magnifying glass is shown. Click the icon to get a dialog up for searching icons and picking a color. Enter a searchword and the icon you want and color using the "eye-dropper". Click the trashcan icon if you dont want to select an icon.
* The last dropdown is to change what is shown on the tab: Icon + Text (Icon on the left - text on the right), Text + Icon, Icon only, Text only - notice its not possible to make "empty" tabs ie. selecting "Icon only" and then no icon is selected.


#### Top icons
This allows you to change the look & feel of the top icons in top menu
* Compact ["Navbar temperature plugin"](https://plugins.octoprint.org/plugins/navbartemp/) - will add icons and shrink the temperature display on this awesome plugin
* Center topbar icons - will horizontal center the extra plugins/top icons in the topbar
* Icon order - change the order in which the icons are displayed in the top menu bar - notice some icons can be hidden. Turn on "Preview" to see them

### Advanced
* Disable terminal when hidden - Disables the terminal update when the terminal tab is in the background - gives a small perfomance boost.