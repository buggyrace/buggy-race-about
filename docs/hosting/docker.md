---
title: With Docker
layout: home
nav_order: 20
parent: Installation and Hosting
---

<details open markdown="block">
  <summary>
    Contents of this page:
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

# Self-hosting with Docker

The buggy race server is a Python Flask application that connects to an SQL
database.

This page describes hosting the server using [Docker](https://www.docker.com),
which is a tool that helps you manage deployment by wrapping the services in
containers. You don't need to do this — if you prefer to self-host directly,
see the page about self-hosting the server [without Docker](without-docker).

The [race server repo](https://github.com/buggyrace/buggy-race-server) includes
the necessary files to deploy using Docker containers. These files are ignored
if you're not using Docker. Docker is not a requirement, but you may find it
convenient to use it.

{: .note}
**This page assumes you are familiar with Docker!**  
Self-hosting the race server requires either you or your tech team to be
familiar with the underlying technology to set up and run the webserver and its
database. If you're not confident with this, we recommend [hosting in the cloud
with Heroku](heroku).

## Consider creating a virtual machine

This isn't a requirement for deployment, but — especially if you are running
the race server as one service amongst others on your institution's machine —
it's a good policy to create a VM and run everything within that. Setting that
up is beyond the scope of this documentation but if you or your tech team are
comfortable doing that — and exposing port 443 to the outside world — then that
is a recommended solution.

{: .rhul}
In the 2023 buggy racing at RHUL, we ran the race server as a dockerised
application within a VM... and it worked fine :-)  Previously we'd run with
Heroku, so we've trialed both approaches.

## Create a .env file

The Dockerfile _can_ contain `environment` sections but we've not used them,
in favour of the `.env` file. Create your `.env` by copying the `env.example`
file in the repo.

You need to edit that according to the comments inside it. Specifically,
find the section marked "Docker" and uncomment those settings. Your `.env`
file will look something like this:

```
POSTGRES_USER=superuser
POSTGRES_PASSWORD=changeme
POSTGRES_DB=buggy_race
DB_HOST=buggy-race-db
DB_PORT=5432
DB_USER=buggy
DB_PASSWORD=you_can_change_this
DATABASE_URL=postgres://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$POSTGRES_DB
FLASK_APP=buggy_race_server/app.py
BUGGY_RACE_SERVER_URL=http://buggy.example.com
```

{: .note}
Look inside the example `env.example` for a breakdown of what each of those
declarations is doing.

See [more about using environment variables](../customising/env) to customise
your race server.

{: .note}
If you get into a pickle with environment variables (for example if you ignored
our advice and did edit the `environment` section in your Docker files),
remember that — once your server is running — as an admin, you can inspect the
settings through the web interface: see [system
info](../customising/env#other-system-settings-system-info).

## Compose the Dockerised containers

To kick everything off, do:

    docker-compose up

There are four containers in the Dockerised application:

* the Flask webserver
* the PostgreSQL database
* a persistent file volume (`published/` within the application file structure)
  where generated [static content](../static-content) is saved
* the `node_modules` used to run [webpack](https://webpack.js.org)

The first time you run this, it may take a while (for example, there's a lot of
material to download in the node modules). Docker checks the timestamps as it's
building and doesn't reload files it's already got — so subsequent runs will
usually be much quicker.

## There's a (small) delay in the build process

The Flask application uses SQLAlchemy to handle any database schema migrations,
but it also stores its config settings in the database. This means there's a
slight chicken-and-egg situation when the app is launched. We've solved this
problem (for now) by imposing a short delay (about 10 seconds) to allow any
migrations to run their course on the database before the Flask application
launches. You don't need to worry about this, but it explains why, if you're
watching a deployment — and if you're issuing `docker-compose` commands, you
probably are — it looks like nothing's happening for a few seconds.

