---
layout: plugin

id: inlineconfirm
title: OctoPrint-InlineConfirm
description: Removes the confirm cancel print dialog and replaces it with confirmation by clicking the cancel buton twice.
authors:
- j7126
license: AGPLv3

date: 2021-02-14

homepage: https://github.com/j7126/OctoPrint-InlineConfirm
source: https://github.com/j7126/OctoPrint-InlineConfirm
archive: https://github.com/j7126/OctoPrint-InlineConfirm/archive/master.zip

tags:
- ui
- control
- cancel

screenshots:
- url: /assets/img/plugins/inlineconfirm/cancel_print_button.gif
  alt: Screen recording. On click of cancel button, it says click again to confirm cancel.
  caption: Screen recording showing the behaviour of the cancel button

featuredimage: /assets/img/plugins/inlineconfirm/cancel_print_button.gif

---

This plugin changes the behaviour of the cancel print button, so that instead of bringing up a dialog to confirm you want to cancel the print, the cancel print button will expand and say 'click again to confirm cancel'. 

To confirm canceling the print, press the button again. If it is not clicked again within 5 seconds it will not cancel the print.

This allows you to quickly and easily cancel a print with a double click, while being more likley to prevent an acidental cancelation than disabling confirm cancel in octoprint settings.