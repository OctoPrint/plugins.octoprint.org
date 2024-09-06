---
layout: plugin

id: onedrive_files
title: OneDrive File Sync
description: Automatically sync your OctoPrint files with OneDrive
authors:
    - Charlie Powell
license: AGPLv3

date: 2023-01-07

homepage: https://github.com/cp2004/OctoPrint-OneDriveFileSync
source: https://github.com/cp2004/OctoPrint-OneDriveFileSync
archive: https://github.com/cp2004/OctoPrint-OneDriveFileSync/releases/latest/download/release.zip

tags:
- onedrive
- file sync
- sync
- cloud
- microsoft

featuredimage: /assets/img/plugins/onedrive_files/config-3.png

compatibility:
    octoprint:
        - 1.6.0
    python: ">=3.7,<4"

attributes:
- cloud

---

# OctoPrint OneDrive File Sync

Sync your OctoPrint files with OneDrive automatically.

## Installation

Install the plugin via the bundled Plugin Manager or manually using this URL:

```
https://github.com/cp2004/OctoPrint-OneDriveFileSync/releases/latest/download/release.zip
```

**Warning**: This plugin requires Python 3.7 or newer to install. To find out more about upgrading your OctoPrint install
to use Python 3, you can take a look at [this post](https://community.octoprint.org/t/upgrading-your-octoprint-install-to-python-3/35158)


## Configuration

Once the plugin is installed and loaded, you can set it up to connect to your Microsoft account.

### Adding your account

![Add account](/assets/img/plugins/onedrive_files/config-1.png)

Select 'Add account' to generate a login code. Head to the URL linked to login with your account, entering the code
generated and logging in with your Microsoft account. Grant OctoPrint OneDrive File Sync access to your files.

Once this is done, return the plugin, and it should show your account name & a success message.

![Login done](/assets/img/plugins/onedrive_files/config-2.png)

### Setting up a synced folder

You can use the built in file browser to find which folder in OneDrive you would like to sync with OctoPrint.
Files will be synced to an 'OneDrive' folder in your OctoPrint uploads.

![Select folder](/assets/img/plugins/onedrive_files/config-3.png)

### Syncing settings

Out of the box a sync will be run every hour, but you can set this interval much much lower if you would like.

The plugin does not upload whilst printing by default, to avoid issues with prints being interrupted should a file need
to be downloaded/uploaded and this takes away resources from printing.

![Sync settings](/assets/img/plugins/onedrive_files/config-4.png)

## Supporting Development

I work on OctoPrint, OctoPrint plugins and help support the community in my spare time. It takes a lot of work, so if
you are interested you can support me through [GitHub Sponsors](https://github.com/sponsors/cp2004). You can contribute monthly or one time for
any amount, you choose!

## Important Security Notice

Please be aware that this plugin stores its tokens for accessing your Microsoft account in OctoPrint's
configuration folder, as expected. As a result, if your OctoPrint install (or the server it is running on) is
compromised, your files in OneDrive are at risk.

**It is not recommended to install this plugin on OctoPrint installs accessible directly from the
internet, or multi-user installs where you may not trust every user.**

The author of this plugin is not responsible for any damage caused as a result of using this plugin.
