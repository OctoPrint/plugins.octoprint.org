---
layout: page
title: Registering a new plugin
---

The OctoPrint Plugin Repository is hosted on [Github Pages](https://pages.github.com/).
You can register new plugins by forking [the source](https://github.com/OctoPrint/plugins.octoprint.org) and just 
editing it accordingly:

 1. [Fork the OctoPrint/plugins.octoprint.org repository on Github](https://github.com/OctoPrint/plugins.octoprint.org)
    to your own account.
 2. Clone the repository to your computer:
 
        git clone git@github.com:<your account>/plugins.octoprint.org
 
 3. Change into the just checked out folder `plugins.octoprint.org`:
 
        cd plugins.octoprint.org
 
 4. Create a new file in the `_plugins` folder called `<your plugin's identifier>.md` following this template:

    ```markdown
    ---
    layout: plugin

    id: your plugin's identifier
    title: your plugin's name
    description: short description of your plugin
    author: your name
    license: your plugin's license

    # today's date in format YYYY-MM-DD, e.g.
    date: 2015-06-22

    homepage: your plugin's homepage
    source: your plugin's source repository
    archive: archive link to install your plugin via pip, e.g. from github: https://github.com/username/repository/archive/master.zip

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
      - 1.2.0

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

    ---

    Longer description of your plugin, configuration examples etc. This part will be visible on the page at
    plugins.octoprint.org/plugin/<your plugin identifier>/
    ```
    
    ---
    
    **Note:** If you used the [OctoPrint cookiecutter template](https://github.com/OctoPrint/cookiecutter-octoprint-plugin) for your
    plugin as suggested in the [Getting Started guide](http://docs.octoprint.org/en/master/plugins/gettingstarted.html#growing-up-how-to-make-it-distributable), 
    it created a pre-filled file for you under `extras/<your plugin's identifier>.md` you just have to complete. Then 
    copy it to `_plugins/<your plugin's identifier>`.
    
    ---
    
    If you are unsure how things should look take a look at the existing plugins.
    
    You may add screenshots to `assets/img/plugins/<your plugin's identifier>/` (you'll need to create
    this folder). You can then reference them as `/assets/img/plugins/<your plugin's identifier>/your_image.png` (the
    leading `/` here is important!).
    
    The image you define as `featuredimage` will be included in the plugin repository's RSS feed and plugins.json file. 
    Future versions of the plugin manager might also display it within OctoPrint.
    
    **Important**: Make sure `your plugin's identifier` is the same you will register your plugin
    under with OctoPrint! So if you entered `my_awesome_plugin` for `plugin_identifier` in [cookiecutter](https://github.com/OctoPrint/cookiecutter-octoprint-plugin)
    make sure to use that exactly like that here too.
 5. Ideally, you'll test that your plugin gets listed correctly and the plugin page looks
    as expected. For this you'll need to install [Jekyll](http://jekyllrb.com/), which is what [Github Pages](https://pages.github.com/) and hence
    the plugin repository uses for rendering the static repository from the source files. Make sure you have at least [Ruby 2.0](https://www.ruby-lang.org/en/)
    installed.
    
    Github offers [a nice setup guide](https://help.github.com/articles/using-jekyll-with-pages/) that makes sure you 
    have the exact versions of everything you need to run.
    
    ---
    
    **Note:** If you want to install Jekyll on Windows, you might want to give [this step-by-step guide](http://jekyll-windows.juthilo.com/)
    a look. You might run into some issues with the `hitimes` gem since at the time of writing this it hasn't yet
    been adapted to the changes introduced in Ruby 2.2. If this is the case, take a look [here](http://stackoverflow.com/questions/28985481/hitimes-require-error-when-running-jekyll-serve-on-windows-8-1).
    
    ---
     
    After installing Jekyll, a simple
    
        bundle exec jekyll serve
    
    will start up a server listening on [localhost:4000](http://localhost:4000) serving the whole page.
    Make sure your plugin shows up there under "Recently added" and the other listing types and that it page
    looks as you expected.
 6. Commit your changes:
 
        git add _plugins/<your plugin's identifier>.md
        git add assets/img/plugins/<your plugin's identifier>
        git commit
    
    Please use a meaningful commit message (e.g. "Added plugin <your plugin's identifier").
 7. Push your changes to your fork on Github:
  
        git push
 
 8. Create a pull request on Github against the original repository.

    Note that a Continous Integration server is configured that will test your PR to make sure the site still builds and the generated
    feeds of the plugin repository are still valid. If something turns out to be amiss here, you can find out what's up by clicking on the
    red "X" marking the build of your PR as failed.
 9. Once your pull request is merged, your plugin will be listed. Congratulations!
