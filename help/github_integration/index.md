---
layout: page
title: Github Integration on plugins.octoprint.org
---

The Plugin Repository has an integration with GitHub set up that allows you to star
and thus show appreciation for plugins that you like right on GitHub.

### How do I star plugins?

If you see "GitHub stats" on a plugin's details page, it means that this plugin is hosted
on GitHub and you can give it a star!

To do so, all you need is to click the Login button, login with your GitHub account and
then you will be able to star all plugins that you like and that are hosted on GitHub.

If you do not have a GitHub account yet, you can also create one right from the login
dialog.

### Why does the integration require repository access?

In order to be able to star repositories, GitHub requires a user session with the "repo"
scope. There sadly does not seem to be a way around this.

### Where do you store my credentials?

Neither the Plugin Repository nor the integration store your credentials. The token used for
authenticating against GitHub's API is stored as an encrypted cookie in your browser.
If you delete your cookies, your login will also be removed.

### How can I revoke the integration's access to my GitHub account?

If you just want to temporarily log out, click "Logout". If you want to permanently
revoke access again then please [do so in your GitHub settings](https://docs.github.com/en/free-pro-team@latest/github/authenticating-to-github/reviewing-your-authorized-applications-oauth).
