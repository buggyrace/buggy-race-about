---
title: Environment variables
layout: home
nav_order: 5
parent: Customising
has_children: false
---


# Environment variables

The race server stores nearly all of its configuration in the database. The names of each config setting is shown when you set them (go to **Admin** → **Config** to see them). You can change them during [the setup phase](setup-phase) or later by editing them.

However, you can also set them explicitly as environment variables. Declaring any config setting in this way **overrides** the current setting in the database. In this way, setting config via environment variables always takes priority.

{: .highlight}
Other than during installation, you might never need to do this!  
Normally, change config settings via the web interface: **Admin** → **Config**.

There are two ways to pass environment variables like this: both require you to have access to the server.

## Set or export environment variables

If you export an environment variable in the process that then launches the server, it will be picked up that way.

If you're using Heroku, go to the race-server app, find **Settings** and click **Reveal config settings**.

## Use the `.env` file

Any declarations in a file called `.env` in the project root directory will be used. See the file `env.example` for some notes and examples.

## Environment settings are saved to database

If you launch (or restart) the race server with any config set by environment variables, those values will be saved in the database. That is, they _will_ persist in subsequent runs (until you edit them via **Admin** → **Config**).

When you go to edit config entries in the web interface, you'll be warned if it was set via an environment variable.

## Other "system" settings

There are some config settings that the admin interface doesn't let you edit. You can see them by going to **Admin** → **Dashboard** → **System info**. Many of the config settings shown there can be declared as environment variables.

Config set via environment variable is only read when the race server starts up (so you may need to restart it after changing variables).
