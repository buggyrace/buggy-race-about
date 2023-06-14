---
title: Tech notes
layout: home
nav_order: 20
parent: Static content
---


# The tech notes

The **tech notes** provide supporting and explanatory material about some of
the technology and tasks.

{: .note}
**You cannot edit the tech notes** because they are produced as static content
(HTML pages) from files in the source code repo. If you want to change or
customise them, you can extract them and host them yourself (for example, as
GitHub Pages).

 
{: .screenshot}
![Screenshot of example tech note page](/docs/img/screenshots/tech-notes-example.png)

{: .caption}
Example tech note page ("How Flask works as a webserver"). The tech notes are
styled to be clearly distinguished from other pages on the race server.
 
## Publishing the tech notes on the race server

{: .navigation}
**Admin** → **Config** → **Tech notes** → **Publish tech notes**

This is the default behaviour: the race server generates the HTML files using
the static site-generator [Pelican](https://getpelican.com), and subsequently
serves them from `/tech-notes`.

The tech notes are served as _static content_: when you complete the set-up
phase, you must publish them, which generates the HTML pages. If you change any
config settings that appear within the tech notes, you should re-publish them
(as a rule of thumb: if you change any config settings, re-publish the tech
notes, just to be sure).

### If you don't publish the tech notes — 404!

If you are using the default set-up, with the tech notes being served by the
race server, but you don't publish them — or your hosting platform (e.g.,
Heroku) does not preserve them when you redeploy the software — the students
will get 404 errors when they follow links to them. You must re-publish them
manually. The [admin dashboard](../running/dashboard) and [set-up
summary](../running/setup-summary) both show warnings if the tech note pages
are missing.

{: .screenshot}
![Screenshot of admin dashboard showing tech note warning](/docs/img/screenshots/tech-notes-warning.png)

{: .caption}
A warning is displayed at the top of the admin dashboard if the tech notes are
missing. Students visiting the tech notes link will see a 404 error.


## Publishing the tech notes yourself

If you want to change, customise, or add to the tech notes — which we
encourage, of course! — you first have to extract them and host them yourself.

{: .todo}
The tech note extraction feature is not implemented yet!  
[GitHub issue #135](https://github.com/buggyrace/buggy-race-server/issues/135) 

The default tech notes use [Pelican](https://getpelican.com), which is a static
site generator written in Python.

Once you've published them on an external server, you need to change the 
config settings so that the race server will redirect all requests for tech
notes to the external site URL. See the [tech note config settings](../customising/tech-notes)
for details.

{: .note}
The redirection using `TECH_NOTES_EXTERNAL_URL` preserves the page path of the
URL, so although you're free to change the tech notes as much as you like, some
existing links might use the default page paths. When you self-host the
tech-notes by editing the default ones, be sure to check that all the links are
still correct.

### Behind the scenes on the race server

If you're self-hosting the tech notes using Pelican, it might be helpful to see
how we produce the HTML on the race server. The relevant files are in the
server repo here:

* [`tech_notes/`](https://github.com/buggyrace/buggy-race-server/tree/main/tech_notes)  
  Contains the config and source for the Pelican build.
  * [`content/`](https://github.com/buggyrace/buggy-race-server/tree/main/tech_notes/content)  
    Contains all the source (markdown) and static assets (CSS and images)
  * [`pelicanconf.py`](https://github.com/buggyrace/buggy-race-server/blob/main/tech_notes/pelicanconf.py)  
    The example default config file which the race server copies when building
    the pages — note the `JINJA_GLOBALS` dictionary which is how the config
    settings are passed into the static site build.
  * `pelicanconflive.py`  
    The "live" version of `pelicanconf.py` that's created dynamically, with the
    current values of config settings (the [config setting](../customising/tech-notes)
    `IS_ALL_CONFIG_IN_TECH_NOTES` controls whether _all_ config settings are
    included in that, or just a minimal subset).
  * [`buggyjinja2content`](https://github.com/buggyrace/buggy-race-server/blob/main/tech_notes/plugins/buggyjinja2content/buggyjinja2content.py)  
    A custom plugin that preserves the table of contents behaviour that is
    otherwise lost.








