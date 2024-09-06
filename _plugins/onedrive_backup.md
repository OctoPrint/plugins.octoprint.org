---
layout: plugin

id: onedrive_backup
title: OneDrive Backup
description: Automatically upload OctoPrint backups to Microsoft OneDrive
authors:
- Charlie Powell
license: AGPLv3

date: 2022-01-03

homepage: https://github.com/cp2004/OctoPrint-OneDrive-Backup
source: https://github.com/cp2004/OctoPrint-OneDrive-Backup
archive: https://github.com/cp2004/OctoPrint-OneDrive-Backup/releases/latest/download/release.zip

tags:
- onedrive
- backup
- cloud
- microsoft

# screenshots:     - they are all embedded in the config guide below.
# - url: url of a screenshot, /assets/img/...
#   alt: alt-text of a screenshot
#   caption: caption of a screenshot

featuredimage: /assets/img/plugins/onedrive_backup/config-3.png

compatibility:
  octoprint:
  - 1.5.0

  # Every OS should work

  python: ">=3.7,<4"

attributes:
- cloud

---

## Installation

Install the plugin via the bundled Plugin Manager or manually using this URL:
```
https://github.com/cp2004/OctoPrint-OneDrive-Backup/releases/latest/download/release.zip
```

**Warning**: This plugin requires Python 3.7 or newer to install. To find out more about upgrading your OctoPrint install
to use Python 3, you can take a look at [this post](https://community.octoprint.org/t/upgrading-your-octoprint-install-to-python-3/35158)

## Configuration

Once the plugin is installed and loaded, you can set it up to connect to your Microsoft account.

### Adding your account

![Add account](/assets/img/plugins/onedrive_backup/config-1.png)

Select 'Add account' to generate a login code. Head to the URL linked to login with your account, entering the code
generated and logging in with your Microsoft account. Grant OctoPrint OneDrive Backup access to your files.

Once this is done, return the plugin, and it should show your account name & a success message.

![Login done](/assets/img/plugins/onedrive_backup/config-2.png)

### Configuring the backup upload

![Select Folder](/assets/img/plugins/onedrive_backup/config-3.png)

You can then configure the folder to save backups to. Select 'Change Folder' and then you should be able to navigate
through your OneDrive folders to find somewhere for backups to be saved.

![Backup upload progress](/assets/img/plugins/onedrive_backup/config-4.png)

Maybe give it a test after configuring it - head to the backup & restore tab and create a backup. Upload progress will
be shown in a notification in the UI.

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
