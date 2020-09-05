---
layout: plugin

id: preprintservice
title: OctoPrint-PrePrintService
description: This service supports your 3D printing workflow by providing auto-rotation and slicing functionality.
author: Christoph Schranz
license: AGPLv3

date: 2019-05-12

homepage: https://github.com/christophschranz/OctoPrint-PrePrintService
source: https://github.com/christophschranz/OctoPrint-PrePrintService
archive: https://github.com/christophschranz/OctoPrint-PrePrintService/archive/master.zip

follow_dependency_links: false

tags:
- slic3r
- slicing
- gcode
- stl
- tweak
- auto-rotate
- orientation


featuredimage: /assets/img/plugins/preprintservice/workflow.png

compatibility:

  octoprint:
  - 1.3.0

  os:
  - linux
  - windows
  - macos

---

# OctoPrint-PrePrintService

This service supports your 3D printing workflow by utilizing **auto-orientation**
and **slicing** functionality.

The PrePrint Service is based on:
* The **auto-rotation** software for FDM 3D printing [Tweaker-3](https://github.com/ChristophSchranz/Tweaker-3)
* The **slicing** software [Slic3r](https://slic3r.org/)

You can also use a similar and prefered tool-chain by using [Cura](https://ultimaker.com/software/ultimaker-cura)
as the Slicing software and with the Plug-Ins
[Auto-Orientation](https://github.com/Ultimaker/Cura/wiki/Plugin-Directory)
and [Octoprint Connection](https://github.com/Ultimaker/Cura/wiki/Plugin-Directory).

## Workflow

The full workflow can be deployed either on a single machine or more generally
 on two separated nodes as described below:

![Workflow](/assets/img/plugins/preprintservice/workflow.png)

The following steps will be done:

1. Upload a model on Octoprint and click on the `Slice` button in the `file bar`.
2. The model will be auto-rotated for a proper 3D print by the [Tweaker-3](https://github.com/ChristophSchranz/Tweaker-3) software.
4. The optimized model will be sliced using [Slic3r](https://slic3r.org/).
5. The final machine code will be sent back to the octoprint server.
6. The printing can be started.

Each step can be adjusted as described in the settings.

## Requirements

1. One server node that is connected to your 3D printer, like a Raspberry Pi.
2. One server node for pre-processing, which has at least 2GHz CPU frequency.
   If the node connected to the printer is strong enough, one server suffices.
3. Optional: Install [Docker](https://www.docker.com/) version **1.10.0+**
   and [Docker Compose](https://docs.docker.com/compose/install/) version **1.6.0+**
   on the more powerful node.


## Setup

### 1. Install the Plugin

Install the **Octoprint-PrePrint Service** in the [Plugin Manager](http://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
, e.g., from the archive's URL `https://github.com/christophschranz/OctoPrint-PrePrintService/archive/master.zip`
or manually using the git's URL on the Printer-Controller


### 2. Set up the (external) preprocess services in Docker

In order to make the service highly available, it is recommended to deploy the
PrePrint-Service in Docker. If you are not familiar with docker yet,
have a quick look at the links in the [requirements-section](#requirements).

Then run the application locally with:

    git clone https://github.com/christophschranz/OctoPrint-PrePrintService
    cd OctoPrint-PrePrintService
    docker-compose up --build -d
    docker-compose logs -f

**Optional:** The `docker-compose.yml` is also configured to run in a given docker swarm,
 adapt the `docker-compose.yml` to your setup and run:

    docker-compose build
    docker-compose push
    docker stack deploy --compose-file docker-compose.yml preprintservice

The service is available on [localhost:2304/tweak](http://localhost:2304/tweak)
(from the hosting node),
where a simple UI is provided for testing the PrePrint Service.
Use `docker-compose down` to stop the service. (If you ever wish :wink: )

![PrePrint Service](/assets/img/plugins/preprintservice/PrePrintService.png)


## Configuration

Configure the plugin in the settings and make sure the url for the PrePrint service is set
correct:

![settings](/assets/img/plugins/preprintservice/settings3.png)

Note that the **octoprint URL must not be localhost**, as the `tweak-service` is deployed in
a docker network where it is unable to locate it's hosts local network.

Finally, go back to the home UI, **click** on the **`Slice`-Button** of uploaded STL-Models and
**produce printable machinecode** via this Preprocessing-Plugin.


## Testing
To test the whole setup, do the following steps:

1. Visit [localhost:2304/tweak](http://localhost:2304/tweak), select a stl model file
   and make an extended Tweak (auto-rotation) `without` slicing. The output should be
   an auto-rotated (binary) STL model. If not, check the logs of the docker-service
   using `docker-compose logs -f` in the folder where the `docker-compose.yml` is located.

2. Now, do the same `with` slicing, the resulting file should be a gcode file of the model.
   Else, check the logs of the docker-service using `docker-compose logs -f` in the
   same folder.

3. Visit the Octoprint server, click on the **`Slice`-Button** of the uploaded
STL-Model in the `file bar` and **produce printable machinecode** via this
PrePrint-Service Plugin.. After some seconds a `.gco` file should be uploaded. Note that in a small time frame a
   `.gco` file with only one line and 83 bytes can appear. This is expected and should be overwritten
   afterwards after a short time.
   If this doesn't work, start the octoprint server per CLI with `octoprint serve`
   and track the logs. The following two lines are expected:

        2019-04-07 22:28:44,301 - octoprint.plugins.preprintservice - INFO - Connection to PrePrintService on http://192.168.48.81:2304/tweak is ready, status code 200
        2019-04-07 22:28:44,321 - octoprint.plugins.preprintservice - INFO - Connection to Octoprint server on http://192.168.48.43:5000/api/version?apikey=A943AB47727A461F9CEF9EXXXXXXXX is ready, status code 200

   If the the Octoprint Server's URL is invalid, you will see this:

        2019-04-07 22:27:34,746 - octoprint.plugins.preprintservice - WARNING - "Connection to Octoprint server on http://192.168.48.43:5000 couldn't be established"

   If you see instead the following, please check the APIKEY: (403 - forbidden)

        2019-04-07 22:30:09,570 - octoprint.plugins.preprintservice - WARNING - Connection to Octoprint server on http://192.168.48.43:5000/api/version couldn't be established, status code 403

   If the the PrePrint Server can't be reached, you will see this:

        2019-04-07 22:27:34,746 - octoprint.plugins.preprintservice - WARNING - Connection to PrePrint Server on http://192.168.48.81:2304/asdf couldn't be established

   Make also sure that your selected `profile` file is correct.

If you have any troubles in setting this plugin up or tips to improve this instruction,
 please let me know!


## PrePrint-Service API

You can use this API to preprocess your models for 3D printing.

```python
import requests

url = "http://localhost:2304/tweak"
model_path = 'preprintservice_src/uploads/model.stl'
profile_path = 'preprintservice_src/profiles/profile_015mm_brim.profile'
output_path = 'gcode_name.gcode'

# Auto-rotate file without slicing
r = requests.post(url, files={'model': open(model_path, 'rb')},
                  data={"tweak_actions": "tweak"})

# Only slice the model to a gcode
r = requests.post(url, files={'model': open(model_path, 'rb'),
                              'profile': open(profile_path, 'rb')},
                data={"machinecode_name": output_path,
                        "tweak_actions": "slice"})
# Auto-rotate and slice the model file
r = requests.post(url, files={'model': open(model_path, 'rb'), 'profile': open(profile_path, 'rb')},
                  data={"machinecode_name": output_path, "tweak_actions": "tweak slice"})
print(r.status_code)
object = r.text
```

The resulting object, either a tweaked stl file or a gcode file is
accessible via `r.text` which can be some MB large.

Information of how to interact with Octoprint's API is depicted [here](http://docs.octoprint.org/en/master/api/files.html#upload-file-or-create-folder).
For example, you can test the file upload API like this:

```python
import json
import requests

# Octoprint's URL using the default port 5000 and the API including the API-key
url = "http://192.168.48.43:5000/api/files/local?apikey=A943AB47727A461XXXXXXXXXXXX"
model_path = 'preprintservice_src/uploads/model.stl'
files = {'file': open(model_path, 'rb')}

# Upload a file using Octoprint's API
r = requests.post(url=url, files=files)
print(r.status_code)
print(json.dumps(r.json(), indent=2))
```

I hope this workflow for 3D print preprocessing helps you!


## Donation

This plugin, as well as the auto-rotation module 
[Tweaker-3](https://github.com/ChristophSchranz/Tweaker-3) was developed in my spare time.
If you like it, I would be thankful about a cup of coffee :) 

[![More coffee, more code](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=RG7UBJMUNLMHN&source=url)

Happy Printing!
