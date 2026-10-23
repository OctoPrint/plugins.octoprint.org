---
layout: plugin

id: git_backup
title: Git Backup Plugin
description: Automatically push OctoPrint backups to a remote Git repository after each backup is created.
authors:
- Mauro Druwel
license: MIT

date: 2026-05-14

homepage: https://github.com/MauroDruwel/OctoPrint-Git-Backup
source: https://github.com/MauroDruwel/OctoPrint-Git-Backup
archive: https://github.com/MauroDruwel/OctoPrint-Git-Backup/archive/main.zip

tags:
- backup
- git
- github
- configuration
- automation
- version control

screenshots:
- url: /assets/img/plugins/git_backup/settings.png
  alt: Git Backup Plugin settings panel showing repo URL, status checks and tips
  caption: Settings panel with live auth status and one-click setup
- url: /assets/img/plugins/git_backup/backup-repo.png
  alt: GitHub repository receiving automatic OctoPrint backup commits
  caption: Every backup becomes a git commit in your private repo

featuredimage: /assets/img/plugins/git_backup/settings.png

compatibility:
  octoprint:
  - 1.6.0

  os:
  - linux
  - windows
  - macos
  - freebsd

  python: ">=3.7,<4"

---

Automatically pushes OctoPrint backups to a remote Git repository every time a backup is created. Once configured with a repo URL, every new backup is committed and pushed, keeping a full version-controlled history of your printer's configuration.

While GitHub is the primary target (with built-in GitHub CLI setup helpers), **any git remote works**, GitLab, Gitea, Bitbucket, self-hosted, as long as the host running OctoPrint is authenticated at the OS level (SSH key, credential manager, or `gh auth login` for GitHub).

## Features

- **Automatic**, listens for backup events and pushes without any manual steps
- **Version-controlled history**, every backup is a git commit; roll back any time
- **No stored credentials**, uses your OS-level GitHub CLI token (`gh auth login`), nothing is saved in the plugin
- **Optional auto-delete**, remove the local `.zip` after a successful push to save disk space
- **README-safe**, existing `README.md` in the repo is never overwritten by backup contents
- **Live auth status panel**, shows git/gh CLI status and credential helper setup in the OctoPrint settings UI
- **Guided GitHub CLI setup**, trigger `gh auth login` directly from the settings panel with device code flow

## Setup

1. Create a **private** GitHub repository (backups may contain API keys and credentials)
2. Enter the repository URL in the plugin settings
3. Authenticate: configure git authentication at the OS level (SSH key, credential helper, or use the guided GitHub CLI login in the settings panel)
4. Trigger a backup from OctoPrint, the plugin pushes it automatically

## Tips

- Exclude **timelapses** and **uploads** from your OctoPrint backups (Settings, Backup & Restore, Create backup) to keep the repo small. GitHub rejects files over 100 MB.
- Want timelapses without the storage cost? [YouTube Timelapse](https://plugins.octoprint.org/plugins/youtube_timelapse/) uploads them directly to YouTube.
- Want scheduled backups? [Backup Scheduler](https://plugins.octoprint.org/plugins/backup_scheduler/) triggers OctoPrint backups on a timer, this plugin will push each one automatically.
