---
layout: page
title: Registering a new plugin
---

The OctoPrint Plugin Repository is hosted on [Github Pages](https://pages.github.com/).
You can register new plugins by forking [the source](https://github.com/OctoPrint/plugins.octoprint.org) and just
editing it accordingly.

---

**Before registering your plugin, please consider whether you are actually willing and able to _actively_ maintain it.**

This means you will be around after registration too, keep up with changes in OctoPrint's plugin API and adjust your plugin as necessary
in new releases, fix bugs that are reported to you by the community, fix _security issues_ reported to you and maybe also implement the
one or other feature request.

You should _not_ register a plugin just to make it easier for you to install it. We expect plugins on
the official repository to be actively maintained. That doesn't necessarily mean a lot of work, it very much depends on the complexity
and size of your plugin. But you should be clear that **publishing your plugin on the official repository means it becomes your responsibility**
-- and, when you no longer can take care of it, notifying us and ideally also helping find someone else who can continue your work is also
something you should consider your responsibility as a plugin maintainer.

This _also_ means that you should be capable of fixing issues in your plugin even if your favourite genAI is down,
and that you understand why your plugin works in the first place -- meaning that **completely vibe coded plugins
are _not_ something we will accept here**.

**tl;dr: By publishing a plugin on the official OctoPrint Plugin Repository, you become responsible of
properly maintaining it. Be sure you are both willing and able to do this _before_ you register your plugin.**

---

Once you are clear on whether you want to and can maintain your plugin, also check the following.

- Your plugin doesn't have any additional code in its <code>setup.py</code> that would run directly on
  plugin installation, or any additional code in its <code>**init**.py</code> that would run outside of
  OctoPrint's plugin framework just by loading it.

- Your plugin doesn't attempt to modify the user's system without their knowledge, e.g. by trying to install
  additional system packages, services or the like. If your plugin needs additional steps like this to function,
  add a wizard dialog that prompts the user to do these things, do <em>not</em> do them automatically.

  Exception: Fetching additional Python dependencies from the Python Package Index through `plugin_requires` in your
  `setup.py` is fine.

- If your plugin heavily interacts with any kind of cloud services, your plugin must now link to a Privacy Policy through
  `privacypolicy` in your registration file and `__plugin_privacypolicy__` in your `setup.py`. The goal is to give
  users access to your Privacy Policy and thus information on how you use their data and what data you use in
  what fashion _prior_ to them installing your plugin.

- If your plugin interacts with external services it will do so over secured connections with a valid certificate only
  (`https://someservice.com` instead of `http://130.47.11.15`). This also includes embedding any kinds of iframes in
  the web interface. Also include this kind of information in the plugin's long description (see below)!

- If your plugin requires the use of external services, and those services are unreachable (say for example a user's
  internet is down or the OctoPrint instance runs offline in general), your plugin must fail in a way that does
  not cause OctoPrint to malfunction.

- If your plugin contains any kind of tracking code, e.g. for anonymous user statistics to help with
  development, use an _opt-in_ mechanism for this. Also include this kind of information in the plugin's long
  description (see below)!

  The privacy of your users always takes precedence over your need for usage data!

- If your plugin makes use of the [`octoprint.plugin.softwareupdate.check_config` hook](http://docs.octoprint.org/en/main/bundledplugins/softwareupdate.html#octoprint-plugin-softwareupdate-check-config)
  so that it may be updated through OctoPrint on a new release (highly recommended!) make sure that that hook's handler uses your plugin's identifier
  and points to your plugin's repository.

- Your plugin is compatible to Python 3. Python 2 is EOL. OctoPrint 1.4.0 does support Python 2 and Python 3, plugins
  will be expected to do so as well (or at least support Python 3) during a transition period of roughly a year after
  the release of OctoPrint 1.4.0 to allow a migration of the whole ecosystem. Read more on how to test this [in this forum post](https://community.octoprint.org/t/towards-python-3-and-octoprint-1-4-0/12382).

Be aware that plugins that don't follow the above will not be allowed to register on the repository. If you have any questions
about any of these points, feel free to get in touch [on the forum](https://community.octoprint.org/c/development).

---

If all is in the green, follow these steps:

1.  [Fork the `OctoPrint/plugins.octoprint.org` repository on Github](https://github.com/OctoPrint/plugins.octoprint.org)
    to your own account.

2.  Clone the repository to your computer and change into it:

        git clone git@github.com:<your account>/plugins.octoprint.org
        cd plugins.octoprint.org

3.  Create a new file in the `_plugins` folder called `<your plugin's identifier>.md`.

    <div class="alert alert-danger">
        <strong>Important:</strong> Make sure <code>your plugin's identifier</code> is the same you will register your plugin under with OctoPrint! So if you
        used <code>my_awesome_plugin</code> as <code>plugin_identifier</code> during plugin creation
        make sure to use that exactly like that here too. Take also care of upper vs. lower case here, <code>MY_awesOmE_PlUGIN</code>
        is not the same as <code>my_awesome_plugin</code>.
    </div>

    Use this template:

    ```markdown
    ---
    layout: plugin
    
    id: your plugin's identifier
    title: your plugin's name
    description: short description of your plugin
    #authors:
    #- first author name
    #- second autor name
    license: your plugin's license
    
    # today's date in format YYYY-MM-DD, e.g.
    date: 2015-06-22
    
    homepage: your plugin's homepage URL
    source: your plugin's source repository URL
    archive: archive link to install your plugin via pip, e.g. from github: https://github.com/username/repository/archive/master.zip
    
    # Set this if your plugin heavily interacts with any kind of cloud services.
    #privacypolicy: your plugin's privacy policy URL
    
    # Set this to true if your plugin uses the dependency_links setup parameter to include
    # library versions not yet published on pypi. SHOULD ONLY BE USED IF THERE IS NO OTHER OPTION!
    #follow_dependency_links: false
    
    tags:
    - a list
    - of tags
    - that apply
    - to your plugin
    - (take a look at the existing plugins for what makes sense here)
    
    screenshots:
    - url: url of a screenshot, /assets/img/...
      alt: alt-text of a screenshot
      caption: caption of a screenshot
    - url: url of another screenshot, /assets/img/...
      alt: alt-text of another screenshot
      caption: caption of another screenshot
    - ...
    
    featuredimage: url of a featured image for your plugin, /assets/img/...
    
    # You only need the following if your plugin requires specific OctoPrint versions or
    # specific operating systems to function - you can safely remove the whole
    # "compatibility" block if this is not the case.
    
    compatibility:
    
      # List of compatible versions
      #
      # A single version number will be interpretated as a minimum version requirement,
      # e.g. "1.3.1" will show the plugin as compatible to OctoPrint versions 1.3.1 and up.
      # More sophisticated version requirements can be modelled too by using PEP440
      # compatible version specifiers.
      #
      # You can also remove the whole "octoprint" block. Removing it will default to all
      # OctoPrint versions being supported.
    
      octoprint:
      - 1.3.0
    
      # List of compatible operating systems
      #
      # Possible values:
      #
      # - windows
      # - linux
      # - macos
      # - freebsd
      #
      # There are also two OS groups defined that get expanded on usage:
      #
      # - posix: linux, macos and freebsd
      # - nix: linux and freebsd
      #
      # You can also remove the whole "os" block. Removing it will default to all
      # operating systems being supported.
    
      os:
      - linux
      - windows
      - macos
      - freebsd
    
      # Compatible Python version
      #
      # Plugins should aim for compatibility for Python 2 and 3 for now, in which case the value should be ">=2.7,<4".
      #
      # Plugins that only wish to support Python 3 should set it to ">=3,<4".
      #
      # If your plugin only supports Python 2 it will no longer be accepted on the plugin repository.
      #
      # Uncomment the appropriate setting
    
      #python: ">=2.7,<3" # Python 2 & 3
      #python: ">=3,<4" # Python 3 only
    
    # TODO
    # If any of the below attributes apply to your project, uncomment the corresponding lines. This is MANDATORY!
    
    attributes:
    #  - cloud  # if your plugin requires access to a cloud to function
    #  - commercial  # if your plugin has a commercial aspect to it
    #  - free-tier  # if your plugin has a free tier
    #  - ai-developed # if your plugin was developed with the use of Artificial Intelligence
    
    ---

    Longer description of your plugin, configuration examples etc. This part will be visible on the page at
    plugins.octoprint.org/plugin/<your plugin identifier>/

    Use Markdown for formatting.
    ```

    <div class="alert">
        <strong>Note:</strong> If you used <code>octoprint dev plugin:new</code> or the <a href="https://github.com/OctoPrint/cookiecutter-octoprint-plugin">OctoPrint cookiecutter template</a> for your
        plugin as suggested in the <a href="http://docs.octoprint.org/en/main/plugins/gettingstarted.html#growing-up-how-to-make-it-distributable">Getting Started guide</a>,
        it created a pre-filled file for you under <code>extras/&lt;your plugin's identifier&gt;.md</code> you just have to complete. Then
        copy it to <code>_plugins/&lt;your plugin's identifier&gt;</code>.
    </div>

    You may add screenshots to `assets/img/plugins/<your plugin's identifier>/` (you'll need to create
    this folder). You can then reference them as `/assets/img/plugins/<your plugin's identifier>/your_image.png` (the
    leading `/` here is important!).

    The image you define as `featuredimage` will be included in the plugin repository's RSS feed and plugins.json file.
    Future versions of the plugin manager might also display it within OctoPrint.

    **Some general guidelines:**
    - Your **short description** should give a user scrolling through the repository a quick idea of what your plugin provides.
      Don't write a novel here, but if possible be a bit more verbose than just basically repeating your plugin's name.

    - Use the **long description** to really explain what your plugin does. Don't just repeat the short description here.
      If your plugin has additional requirements (e.g. specific hardware or software), include that here and also
      explain how to get those. Use [Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) for formatting.

    - Make sure you **your plugin is Python 3 compatible and mark it as such** using the `compatibility.python`
      property. Newly registered plugins will be expected to be compatible _at least_ to Python 3, ideally to
      _both Python 2 and 3_ during a transition period of roughly a year after release of OctoPrint 1.4.0.

    - **Include screenshots and a featured image!** The best way to show users what your plugin does and what they may
      expect from it is to simply include some screenshots that show exactly that. A picture is worth more than a
      thousand words as they say. If your plugin doesn't visually modify OctoPrint in any way, please include that
      fact in the long description.

    - **Do not directly embed third party screenshots/widgets/iframes!** Thanks to the EU's
      [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation) this could cause us severe
      legal problems. If you want to embed a YouTube video showing off your plugin, use the provided `youtube.html`
      include:

      ```
      {% raw %}{% include youtube.html vid="<youtube video id>" preview="<preview image, '/assets/img/...'>" %}{% endraw %}
      ```

      That will make sure that no connection to YouTube is done without the user's consent. You can fetch the
      preview image of your video at `https://i.ytimg.com/vi/<youtube video id>/maxresdefault.jpg` or with the
      `fetch_yt_preview` bash script included in the repository. If you use the latter you can leave out the
      `preview` parameter to the include.

    - Make sure the `archive` URL is **always pointing to the latest release**. OctoPrint uses that URL for initial installation
      of the plugin from the Plugin Manager (regardless of the version shown there). If you are using GitHub and the URL points
      to `<project url>/archive/your_branch.zip` (`master`, `main` are commonly used as branch name) adjust your
      branching strategy to **only** have latest release there.

    - If your plugin **requires a cloud to function, has a commercial aspect to it and/or has a free tier** you _must_
      mark it as such using the `attributes` property. If you are unsure about whether your plugin qualifies as being
      commercial, ask for clarification on that in your registration pull request. Please note that commercial plugins are
      excluded from the public stats after some cases of manipulation.

    - If your plugin **was developed with the aid of Artificial Intelligence** you _must_
      mark it as such using the `attributes` property. 

    If you are unsure about how something should be structured, take a look at the existing plugins or
    [ask on the forum](https://community.octoprint.org/c/development) or in your registration pull request.

4.  Ideally, you'll test that your plugin gets listed correctly and the plugin page looks
    as expected. For this you'll need to install [Jekyll](http://jekyllrb.com/), which is what the plugin repository uses for
    rendering the static repository from the source files.

    <div class="alert">
        <strong>Note:</strong> If you want to install Jekyll on Windows, you might want to give <a href="https://jekyllrb.com/docs/installation/windows/">this guide</a>
        a look.
    </div>

    After installing Jekyll, a simple

        bundle exec jekyll serve

    will start up a server listening on [localhost:4000](http://localhost:4000) serving the whole page.
    Make sure your plugin shows up there under "Recently added" and the other listing types and that it page
    looks as you expected.

5.  Commit your changes:

        git add _plugins/<your plugin's identifier>.md
        git add assets/img/plugins/<your plugin's identifier>
        git commit

    Please use a meaningful commit message (e.g. "Added plugin <your plugin's identifier").

6.  Push your changes to your fork on Github:

        git push

7.  Create a pull request on Github against the original repository.

    Note that a Continous Integration server is configured that will test your PR to make sure the site still builds and the generated
    feeds of the plugin repository are still valid. If something turns out to be amiss here, you can find out what's up by clicking on the
    red "X" marking the build of your PR as failed.

8.  Once your pull request is merged, your plugin will be listed. Congratulations! 🎉
