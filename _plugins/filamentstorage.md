---
layout: plugin

id: filamentstorage  
title: OctoPrint-Filamentstorage  
description: Plugin for OpenSource Filament Storage Containers that report Temp, Humidity, and scale values over USB.  
author: Walt Moorhouse  
license: AGPLv3  
date: 2019-10-23

homepage: https://github.com/waltmoorhouse/OctoPrint-Filamentstorage  
source: https://github.com/waltmoorhouse/OctoPrint-Filamentstorage  
archive: https://github.com/waltmoorhouse/OctoPrint-Filamentstorage/archive/master.zip

tags:
- filament
- usb

screenshots:
- url: /assets/img/plugins/filamentstorage/main.png
  alt: Main screen  
  caption: Main View  
- url: /assets/img/plugins/filamentstorage/settings.png
  alt: Settings screen  
  caption: Settings View  
- url: /assets/img/plugins/filamentstorage/tab_connected.png
  alt: Tab when connected  
  caption: Tab when connected  
- url: /assets/img/plugins/filamentstorage/tab_disconnected.png
  alt: Tab when disconnected  
  caption: Tab when disconnected


featuredimage: /assets/img/plugins/filamentstorage/main.png

---

Connects to any Filament Storage Box supporting the below serial communications:
1) sends periodic updates in the following format: 
    H:xx.xx% T:xx.xxC S1:x.xxkg S2:x.xxkg S3:x.xxkg S4:x.xxkg P:\[ON|OFF\]
1) accepts the following commands:
    1) SET H=xx (sets maxHumidity to xx)
    1) SET T=xx (sets maxTemperature to xx)
    1) TARE y (Tares scale y, 0<y<5)
