---
layout: plugin
id: mqtt
title: MQTT
description: Adds support for subscribing and publishing to MQTT topics.
author: Gina Häußge
license: AGPLv3
homepage: https://github.com/OctoPrint/OctoPrint-MQTT
source: https://github.com/OctoPrint/OctoPrint-MQTT
archive: https://github.com/OctoPrint/OctoPrint-MQTT/archive/master.zip
tags: 
- mqtt
- helper
- notification
screenshots:
- url: /assets/img/plugins/mqtt/mqtt_spy_example.png
  alt: MQTT messages in MQTT-spy
  caption: Example messages in MQTT-spy
date: 2015-04-11
compatibility:
  octoprint:
  - 1.2.0
---

This is an OctoPrint Plugin that adds support for [MQTT](http://mqtt.org/) to OctoPrint.

Out of the box OctoPrint will send all [events](http://docs.octoprint.org/en/devel/events/index.html#available-events)
including their payloads to the topic `octoprint/event/<event>`, where `<event>` will be the name of the event. The message
payload will be a JSON representation of the event's payload, with an additional property `_event` containing the name
of the event.

Examples:

| Topic                        | Message                                                          |
|------------------------------|------------------------------------------------------------------|
| octoprint/event/ClientOpened | `{"_event": "ClientOpened", "remoteAddress": "127.0.0.1"}`       |
| octoprint/event/Connected    | `{"baudrate": 250000, "_event": "Connected", "port": "VIRTUAL"}` |
| octoprint/event/PrintStarted | `{"origin": "local", "_event": "PrintStarted", "file":"/home/pi/.octoprint/uploads/case_bp_3.6.v1.0.gco", "filename": "case_bp_3.6.v1.0.gco"}` |

The print progress and the slicing progress will also be send to the topic `octoprint/progress/printing` and
`octoprint/progress/slicing` respectively. The payload will contain the `progress` as an integer between 0 and 100.
Print progress will also contain information about the currently printed file (storage `location` and `path` on storage),
slicing progress will contain information about the currently sliced file (storage `source_location` and `destination_location`,
`source_path` and `destination_path` on storage, used `slicer`). The published progress messages will be marked as
retained.

Examples:

| Topic                        | Message                                                          |
|------------------------------|------------------------------------------------------------------|
| octoprint/progress/printing  | `{"progress": 23, "location": "local", "path": "test.gco"}`      |
| octoprint/progress/slicing   | `{"progress": 42, "source_location": "local", "source_path": "test.stl", "destination_location": "local", "destination_path": "test.gcode", "slicer": "cura"}` |

The plugin however also offers several helpers that allow other plugins to both publish as well as subscribe to
MQTT topics, see below for details and a usage example.

## Configuration

The plugin currently offers no settings dialog, configuration needs to be done by manually editing `config.yaml`. The
following options are available:

{% highlight yaml %}
plugins:
    mqtt:
        broker:
            # the broker's url, mandatory, if not configured the plugin will do nothing
            url: 127.0.0.1

            # the broker's port
            #port: 1883

            # the username to use to connect with the broker, if not set no user
            # credentials will be sent
            #username: unset

            # the password to use to connect with the broker, only used if a
            # username is supplied too
            #password: unset

            # the keepalive value for the broker connection
            #keepalive: 60

            # tls settings
            #tls:
                # path to the server's certificate file
                #ca_certs: unset

                # paths to the PEM encoded client certificate and private keys
                # respectively, must not be password protected, only necessary
                # if broker requires client certificate authentication
                #certfile: unset
                #keyfile: unset

                # a string specifying which encryption ciphers are allowable for this connection
                #ciphers: unset

            # configure verification of the server hostname in the server certificate.
            #tls_insecure: false

            # configure protocol version to use, valid values: MQTTv31 and MQTTv311
            #protocol: MQTTv31

        publish:
            # base topic under which to publish OctoPrint's messages
            #baseTopic: octoprint/

            # topic for events, appended to the base topic, '{event}' will
            # be substituted with the event name
            #eventTopic: event/{event}

            # topic for print and slicer progress, appended to the base topic,
            # '{progress}' will be substituted with either 'printing' or 'slicing'
            #progressTopic: progress/{progress}
{% endhighlight %}
