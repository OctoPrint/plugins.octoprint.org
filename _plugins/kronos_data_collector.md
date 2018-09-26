---
layout: plugin

id: octoprint_kronos_data_collector
title: Project Kronos Data Collector
description: Help build the Project Kronos print-failure autodetection neural network 
author: Jacob Paniagua
license: AGPLv3

# today's date in format YYYY-MM-DD, e.g.
date: 2018-09-26

homepage: https://github.com/MrBreadWater/project-kronos-data-collector
source: https://github.com/MrBreadWater/project-kronos-data-collector
archive: https://github.com/MrBreadWater/project-kronos-data-collector/archive/master.zip

# Set this to true if your plugin uses the dependency_links setup parameter to include
# library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
#follow_dependency_links: false

tags:
- dataset
- data
- Kronos
- neural
- network


---

#Project Kronos

Project Kronos is an effort to create a webcam-based Neural Network to classify snapshots from a 3D Printer as "Failed" or "Successful". 
This will be implemented in real-time as an Octoprint plugin to automatically pause the printer and alert the user of the potential error.


#The Project Kronos Data Collector

As you may know, training a neural network requires a massive amount of data to create a complete model that can accurately classify an input. 
In this case, Project Kronos will need thousands, possibly hundreds of thousands, of images to train the model with. 
While there are plenty of timelapses and succesful print photos available on the internet, it's very hard to find any failed prints. 
The point of this plugin is to allow users to automatically upload images and timelapses of their prints in the background, helping to create Project Kronos.
Everything is done in the background, never bothering the user with pop-ups or the like. It can, of course, be easily disabled within the plugin settings. 
