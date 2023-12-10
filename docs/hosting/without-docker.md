---
title: Without Docker
layout: home
nav_order: 40
parent: Installation and Hosting
---


# Self-hosting without Docker

{: .warning}
We do not recommend this as a way to run the server for most people. We
recommend either [cloud-hosting with Heroku](heroku), or using
[the Dockerised race server](docker) as the best way of self-hosting.

Nonetheless, if you really do want to run the application with its bare bones
then look in the `DEVELOPMENT.md` document in the server's repo, because that
describes some of the details that we've used when running the server locally
during our dev work.

See [more about using environment variables](../customising/env) to customise
your race server.

It's certainly possible to run the race server locally (for experimentation,
development, or just curiosity). Remember you'll need to set up a database too
(although if you're just testing, sqlLite might be OK).

Check that you're using Python 3.9 or above — there are some dependencies on
the `timezones` module that was introduced to the standard library in that
version.

It might be a good idea to create a virtual environment. Do:

    python -m venv venv

and then activate it, for example with:

    source venv/bin/activate

The Python requirements are, as is standard, listed in `requirements.txt`, so
you'll need to use `pip` to load them:

    pip install -r requirements.txt

You must set some environment variables: two crucial ones are `FLASK_APP`
which locates the `app.py` file, and `DATABASE_URL` which containes the
criteria needed for connecting to the database.

You _can_ export the environment variables, but the simplest way to set this
up is to make a copy of `env.example` called `.env`, and edit that.

The project requires `webpack` which is a node.js (not Python) tool. To set
that up you'll need to do:

    npm install

If everything is in place — and you've set up the database service that you're
connecting to with `DATABASE_URL` — you can run the server up with:

    npm run start

{:. note}
Remember this is also described, in a little more detail, in `DEVELOPMENT.md`
in the race server repo.

## Database migrations

We use SQLAlchemy's schema migrations to keep the database in synch with
changes in the source code (specifically, this is the relationship between
the Python code of the `models` within the app, and how that's implemented
in the SQL database). If you're self-hosting and not using Docker, then you'll
need to run these migrations if the code ever changes (either because you
edited it, or you git-pulled changes from us). See the notes in `DEVELOPMENT.md`
for guidance on that.

## Disclaimer: consider using Heroku or Docker

We think that the Heroku and Docker mechanisms are the most helpful for the two
use-cases of deployment (in the cloud, or self-hosted respectively), so if
you've decided to self-host the bare bones yourself instead that's your choice,
because you know what you're doing :-) We don't/can't really support that in
the face of all the ways it might get complicated.

Nonetheless, if you run into problems, get in touch and we'll try to help out.





