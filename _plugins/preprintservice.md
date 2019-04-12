---
layout: plugin

id: preprintservice
title: OctoPrint-PrePrintService
description: This plugin supports your 3D printing routine by featuring **auto-rotation** and **slicing**.
author: Christoph Schranz
license: AGPLv3

date: 2019-04-12

homepage: https://github.com/christophschranz/OctoPrint-PrePrintService
source: https://github.com/christophschranz/OctoPrint-PrePrintService
archive: https://github.com/christophschranz/OctoPrint-PrePrintService/archive/master.zip


follow_dependency_links: false

tags:
- slic3r
- gcode
- stl
- tweak
- auto-rotate


featuredimage: /assets/img/plugins/preprintservice/tweaker.png

compatibility:

  octoprint:
  - 1.3

  os:
  - linux
  - windows
  - macos

---

# OctoPrint-PrePrintService

This plugin supports your 3D printing routine by featuring **auto-rotation** and **slicing**.
As both tasks are very computation-intensive, they can optionally be outsourced to 
external docker containers.


## Requirements

0. One server node that is connected to your 3D printer
1. One server node for pre-processing, which has at least 2GHz CPU frequency. If the node connected
   to the printer is strong enough, one server suffices.
1. Install [Docker](https://www.docker.com/community-edition#/download) version **1.10.0+**
   on the more powerful node.
2. Install [Docker Compose](https://docs.docker.com/compose/install/) version **1.6.0+**
   on the more powerful node.
3. Optionally: [Docker Swarm](https://www.youtube.com/watch?v=x843GyFRIIY)


## Setup

### 1. Install the Plugin

Install the PrePrint Server plugin via the bundled [Plugin Manager](http://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL on the Printer-Controller

    pip install "https://github.com/christophschranz/OctoPrint-PrePrintService/archive/master.zip"
    
When opening octoprint, you see that everything worked, if you see the label `Using PrePrint Service`
in the navigation bar.
![OctoPrint_navbar](/assets/img/plugins/preprintservice/OctoPrint_navbar.png)


### 2. Install the PrePrint Service

In order to make the service highly available, the PrePrint Service should be deployed
 in docker. If you are
not yet familiar with docker, have a quick look at the links in the 
[requirements-section](#requirements) and install it on a performant server node.

Then run the application locally with:

    git clone https://github.com/christophschranz/OctoPrint-PrePrintService
    cd OctoPrint-PrePrintService
    docker-compose up --build -d
    docker-compose logs -f
     
Optional: The `docker-compose.yml` is also configured to run in a given docker swarm,
 adapt the `docker-compose.yml` to your setup and run:

    docker-compose build
    docker-compose push
    docker stack deploy --compose-file docker-compose.yml preprintservice


The service is in either way on [localhost:2304/tweak](http://localhost:2304/tweak) 
(from the hosting node), 
where a simple UI is provided for testing the PrePrint Service.
Use `docker-compose down` to stop the service.

![PrePrint Service](/assets/img/plugins/preprintservice/PrePrintService.png)


## Configuration

Configure the plugin in the settings and make sure the url for the PrePrint service is 
correct:

![settings](/assets/img/plugins/preprintservice/settings2.png)

To test the whole setup, do the following steps:

1. Visit [localhost:2304/tweak](http://localhost:2304/tweak), select a stl model file
   and make an extended Tweak (auto-rotation) `without` slicing. The output should be
   the auto-rotated binary STL model. Else, check the logs of the docker-service
   using `docker-compose logs -f` in the same folder.

2. Now do the same `with` slicing, the resulting file should be a gcode file of the model.
   Else, check the logs of the docker-service using `docker-compose logs -f` in the 
   same folder.

3. Visit the octoprint server and try to slice an uploaded stl model file. After
   some seconds a `.gco` file should be uploaded. Note that in a small time frame a
   `.gco` file with only one line and 83 bytes can appear. This one should be overwritten
   soon afterwards.
   If this doesn't work, start the octoprint server per CLI with `octoprint serve`
   and track the logs. The following two lines are expected:
   
        2019-04-07 22:28:44,301 - octoprint.plugins.preprintservice - INFO - Connection to PrePrintService on http://192.168.48.81:2304/tweak is ready, status code 200
        2019-04-07 22:28:44,321 - octoprint.plugins.preprintservice - INFO - Connection to Octoprint server on http://192.168.48.43:5000/api/version?apikey=A943AB47727A461F9CEF9EXXXXXXXX is ready, status code 200

   If you see instead the following, please check the APIKEY: (403 - forbidden)
        
        2019-04-07 22:30:09,570 - octoprint.plugins.preprintservice - WARNING - Connection to Octoprint server on http://192.168.48.43:5000/api/version?apikey=asdf couldn't be established, status code 403

   If the the PrePrint Server can't be reached, you will seee this:
   
        2019-04-07 22:27:34,746 - octoprint.plugins.preprintservice - WARNING - Connection to PrePrint Server on http://192.168.48.81:2304/asdf couldn't be established

   
If you have any troubles in setting this plugin up or tips to improve this instruction,
 please let me know!

## Donation

If you like this plugin, I would be thankful about a cup of coffee :) 

[![More coffee, more code](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=RG7UBJMUNLMHN&source=url)

Happy Printing!

