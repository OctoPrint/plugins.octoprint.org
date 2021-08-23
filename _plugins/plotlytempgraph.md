---
layout: plugin

id: plotlytempgraph
title: OctoPrint-PlotlyTempGraph
description: Display temperature data in a plotly js graph.
author: jneilliii
license: AGPLv3

date: 2021-08-21

homepage: https://github.com/jneilliii/OctoPrint-PlotlyTempGraph
source: https://github.com/jneilliii/OctoPrint-PlotlyTempGraph
archive: https://github.com/jneilliii/OctoPrint-PlotlyTempGraph/archive/master.zip

follow_dependency_links: false

tags:
- temperature
- graph
- UI
- plotly

compatibility:
  octoprint:
  - 1.3.6
  python: ">=2.7,<4"

featuredimage: /assets/img/plugins/plotlytempgraph/screenshot.png

---

# OctoPrint-PlotlyTempGraph

This plugin replaces the default temperature tab of OctoPrint with a [plotly.js](https://plotly.com/javascript/) graph that incorporates other data supplied by the return of plugin's [octoprint-comm-protocol-temperatures-received](https://docs.octoprint.org/en/master/plugins/hooks.html#octoprint-comm-protocol-temperatures-received) callbacks. Useful for other plugins to inject their own data into the temperature graph (ie. Enclosure Plugin Sensor Data).

![screenshot](/assets/img/plugins/plotlytempgraph/screenshot.png)

## Get Help

If you experience issues with this plugin or need assistance please use the issue tracker at the plugin's Homepage linked on the right.

### Additional Plugins

Check out my other plugins [here](https://plugins.octoprint.org/by_author/#jneilliii)

### Support My Efforts
I, jneilliii, programmed this plugin for fun and do my best effort to support those that have issues with it, please return the favor and leave me a tip or become a Patron if you find this plugin helpful and want me to continue future development.

[![Patreon](/assets/img/plugins/plotlytempgraph/patreon-with-text-new.png)](https://www.patreon.com/jneilliii) [![paypal](/assets/img/plugins/plotlytempgraph/paypal-with-text.png)](https://paypal.me/jneilliii)

<small>No paypal.me? Send funds via PayPal to jneilliii&#64;gmail&#46;com</small>
