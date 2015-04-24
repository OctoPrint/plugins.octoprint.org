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
 
        ---
        layout: plugin
        id: your plugin's identifier
        title: your plugin's name
        description: short description of your plugin
        author: your name
        license: your plugin's license
        date: today's date in format YYYY-MM-DD, e.g. 2015-04-21
        homepage: your plugin's homepage
        source: your plugin's source repository
        archive: archive link to install your plugin via pip
        tags:
        - a list
        - of tags
        - that apply
        - to your plugin
        - (take a look at the existing plugins for what makes sense here)
        screenshots: 
        - url: url of a screenshot
          alt: alt-text of a screenshot
          caption: caption of a screenshot
        - url: url of another screenshot
          alt: alt-text of another screenshot
          caption: caption of another screenshot
        - ...
        featuredimage: url of a featured image for your plugin
        compatibility:
          octoprint:
          - list of compatible versions
          - for example
          - 1.2.0
          os:
          - list of compatible oerating systems
          - possible values are linux, windows, macos, leaving empty defaults to all
        ---
        
        Longer description of your plugin, configuration examples etc. This part will be visible on the page at
        plugins.octoprint.org/plugin/<your plugin identifier>/
    
    If you are unsure how things should look take a look at the existing plugins.
    
    You may add screenshots to `assets/img/plugins/<your plugin's identifier>/` (you'll need to create
    this folder). You can then reference them as `/assets/img/plugins/<your plugin's identifier>/your_image.png`.
    
    **Important**: Make sure `your plugin's identifier` is the same you will register your plugin
    under with OctoPrint! So if you entered `my_awesome_plugin` for `plugin_identifier` in [the Plugin Skeleton](https://github.com/OctoPrint/OctoPrint-PluginSkeleton)
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
 9. Once your pull request is merged, your plugin will be listed. Congratulations!