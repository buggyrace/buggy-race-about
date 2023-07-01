---
title: Environment variables
layout: home
nav_order: 5
parent: Customising
has_children: false
---


# Environment variables

The race server stores nearly all of its configuration in its database. The
name of each config setting is shown when you set it (go to **Admin** →
**Config** to see them all). You can change them during
[the setup phase](setup-phase) or later by editing them.

However, you can also set any config setting explicitly by declaring it as an
environment variable. Declaring any config setting in this way **overrides**
the current setting in the database.

When the server starts up, any config settings declared via environment
variables are written to the database, overriding any existing values for those
settings.

{: .note}
Other than during installation, you might never need to do this! Normally, you
change config settings via the web interface: **Admin** → **Config**.

There are two ways to pass environment variables like this: both require you to
have access to the server:

* Set or export environment variables
* Use the `.env` file


## Set or export environment variables

If you export an environment variable in the process that then launches the
server, it will be picked up that way.

If you're using Heroku, go to the race-server app, find **Settings** and click
**Reveal config settings**.


## Use the `.env` file

Any declarations in a file called `.env` in the project root directory will be
used. See the file `env.example` for some notes and examples.

If you edit this file, then restart the server, settings made here will be
written into the database. Remember to then edit the .env file again to remove
them so that you can — if you ever need to — subsequently change them through
the web interface.


## Environment settings are saved to the database

If you launch (or restart) the race server with any config set by environment
variables, those values will be saved in the database. That is, they _will_
persist in subsequent runs (until you edit them via **Admin** → **Config**).

When you go to edit config entries in the web interface, you'll be warned if it
was set via an environment variable.

{: .warning}
If you leave an environment variable declaration in place in the `.env` file
after you've restarted the server, any changes to that setting made through the
web interface will be lost when you next restart the server... because this env
setting is going to override it (again). This is why it's generally best to
remove any changes you made in the `.env` file once they've been applied.


## Other "system" settings

{: .navigation}
**Admin** → **Dashboard** → **System info**

There are some config settings that the admin **Config** interface on the race
server doesn't let you edit. You can see them by looking on the **System
information** page. Many of the config settings shown there can be declared as
environment variables if you need to change them.

{: .note}
Unlike changes made through the web interface, any changes you make to
environment variables won't get noticed until you restart the race server.

---
* Previous: [Set-up phase](setup-phase)
* Next: [Authorisation config](auth)