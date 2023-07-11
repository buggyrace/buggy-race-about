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
database. It is possible to run these "[without Docker](bnarewithout-docker)",
but the [race server repo](https://github.com/buggyrace/buggy-race-server)
includes the necessary [Docker](https://www.docker.com) files to deploy using
Docker containers. The rest of this page describes hosting the server using
Docker.

{: .note}
**This page assumes you are familiar with Docker!**  
Self-hosting the race server requires either you or your tech team to be
familiar with the underlying technology to set this up. If you're not
confident with this, we recommend [hosting in the cloud with Heroku](heroku).

## Consider creating a virtual machine

This isn't a requirement for deployment, but — especially if you are running
the race server as one service amongst others your institution's machine, it's
a good policy to create a VM and run everything within that. Setting that up
is beyond the scope of this documentation but if you or your tech team are
comfortable setting that up — and exposing port 443 to the outside world —
then that is a recommended solution.

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

To run kick everything off, do:

    docker-compose up

There are four containers in the Dockerised application:

* the Flask webserver
* the PostgreSQL database
* a persistent file volume (`published/` within the application file structure)
  where generated static content is saved
* the node_modules used to run [webpack](https://webpack.js.org)




