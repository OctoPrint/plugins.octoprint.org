---
layout: plugin

id: ikea_tradfri
title: Ikea Tradfri
description: Control Ikea Tradfri outlet
author: Mathieu "ralmn" HIREL
license: AGPLv3

date: 2020-05-24

homepage: https://github.com/ralmn/OctoPrint-Ikea-tradfri
source: https://github.com/ralmn/OctoPrint-Ikea-tradfri
archive: https://github.com/ralmn/OctoPrint-Ikea-tradfri/archive/master.zip

tags:
- ikea
- tradfri
- outlet

screenshots:
- url: /assets/img/plugins/ikea_tradfri/navbar.png
  alt: Navbar of plugin
  caption: Navbar of plugin
- url: /assets/img/plugins/ikea_tradfri/settings.png
  alt: Settings of plugin
  caption: Settings of plugin

featuredimage: /assets/img/plugins/ikea_tradfri/navbar.png

compatibility:
  octoprint:
  - 1.3.1
  - 1.4.0
  python: ">=2.7,<4"
  os:
  - linux
  - windows
  - macos
  - freebsd

---

Turn on your printer with Ikea Tradfri Outlet.

## Requierements

1. [Ikea Tradfri Gateway](https://www.ikea.com/us/en/catalog/products/00337813/)
2. [Ikea Tradfri Outlet](https://www.ikea.com/us/en/catalog/products/30356169/)

## Setup

## Install libcoap

You need libcoap for communicate with your Ikea Gateway.

    git clone --recursive https://github.com/obgm/libcoap.git
    cd libcoap
    git checkout dtls
    git submodule update --init --recursive
    ./autogen.sh
    ./configure --disable-documentation --disable-shared --without-debug CFLAGS="-D COAP_DEBUG_FD=stderr"
    make
    make install

## Install plugin

Install manually using this URL:

    https://github.com/ralmn/OctoPrint-Ikea-tradfri/archive/master.zip


## Configuration

1. Indicate your gateway ip and your security code (found under your gateway)
2. Save
3. Select your outlet
4. Save
