---
layout: plugin

id: crealitycloud
title: OctoPrint-CrealityCloud
description: A OctoPrint-Plugin that connect the Octoprint to Creality Cloud
authors:
- Creality
license: AGPLv3

date: 2022-04-14

homepage: https://github.com/crealitycloud/OctoPrint-CrealityCloud
source: https://github.com/crealitycloud/OctoPrint-CrealityCloud
archive: https://github.com/crealitycloud/OctoPrint-Crealitycloud/archive/master.zip

privacypolicy: https://www.crealitycloud.com/policy?type=policy

tags:
- Remote control
- Online slice
- Models Download
- file management
- Remote webcam

compatibility:

  octoprint:
  - 1.6.1

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=3,<4"

attributes:
- cloud
- commercial
- free-tier

---
# OctoPrint-Crealitycloud


![main](/assets/img/plugins/crealitycloud/main.png)

Creality Cloud plugin needs to be installed in the OctoPrint interface so that you can connect the Creality Cloud APP to the Raspberry Pi device and print or control directly through the APP by operating OctoPrint.

## **Before you start configuring the Plugin:**

The Creality Cloud plugin needs to enable cloud services, and your 3D printing data will be uploaded to the cloud server, such as temperature, printing speed, printing status, etc. More detailed information about the privacy policy can be viewed inside the Creality Cloud App navigating to My Space > About > Privacy Policy

You need a Creality Cloud account to connect octoprint and Creality Cloud App.More detailed information about the privacy policy can be viewed inside the Creality Cloud App navigating to My Space > About > User Agreement

## **Setup Creality Cloud Plugin on OctoPrint:**
1. Copy the following three plugin links or copy them from Creality Cloud Github.



Creality Cloud Plugin:

- [https://github.com/crealitycloud/OctoPrint-Crealitycloud/archive/master.zip](https://github.com/crealitycloud/OctoPrint-Crealitycloud/archive/master.zip)



Plugins that the Creality Cloud Plugin relies on:
**Required installation or it may cause abnormal temperature or incomplete functionality:**

- [https://github.com/SimplyPrint/OctoPrint-Creality2xTemperatureReportingFix/archive/master.zip](https://github.com/SimplyPrint/OctoPrint-Creality2xTemperatureReportingFix/archive/master.zip)
- [https://github.com/OllisGit/OctoPrint-DisplayLayerProgress/releases/download/1.26.0/master.zip](https://github.com/OllisGit/OctoPrint-DisplayLayerProgress/releases/download/1.26.0/master.zip)




2. Paste and install the plugin links one by one via the bundled "Plugin Manager" on OctoPrint.

![Setup2-1](/assets/img/plugins/crealitycloud/Setup2-1.png)
![Setup2-2](/assets/img/plugins/crealitycloud/Setup2-2.png)

3. Restart the OctoPrint server when you get a prompt.

![Setup3](/assets/img/plugins/crealitycloud/Setup3.png)
## **Generate A Key File in Creality Cloud APP:**

1.  Download and open the Creality Cloud APP on your phone, select "Printing" > click the "+" icon to add device > choose "Raspberry Pi" > click "Create Raspberry Pi" > click "Download Key File".
1.  Transmit the Key file to your computer.

![generateKey2-1](/assets/img/plugins/crealitycloud/generateKey2-1.png)
![generateKey2-2](/assets/img/plugins/crealitycloud/generateKey2-2.png)
## **Upload the Key File to OctoPrint:**
Back to the OctoPrint interface on your desktop, click on the OctoPrint setting button > find the "Crealitycloud Plugin" on the left column list > click "Browse" to select and upload the Key file that you transmitted from Creality Cloud APP.
![uploadKey](/assets/img/plugins/crealitycloud/uploadKey.png)
## **Slice & Print:**
Before you start...

1.  Connect your 3D printer with your Raspberry Pi through a USB cable. Here we recommend using a Raspberry Pi 3.
1.  Select the USB serial port detected by OctoPrint to connect to your printer.

![slice&print2-1](/assets/img/plugins/crealitycloud/slice&print2-1.png)
![slice&print2-2](/assets/img/plugins/crealitycloud/slice&print2-2.png)
Start slicing and printing...

1. Open Creality Cloud APP, select My Devices > Raspberrypi (a custom device name)> Select slice.

![slicing&printing1](/assets/img/plugins/crealitycloud/slicing&printing1.png)

2. Choose a model file to slice and start printing.

![slicing&printing2](/assets/img/plugins/crealitycloud/slicing&printing2.png)
Hope this Creality Cloud plugin on OctoPrint will give you a different experience on your 3D printing. Thank you for supporting and happy printing!


By Creality Cloud.
