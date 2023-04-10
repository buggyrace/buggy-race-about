---
title: Self-hosting
layout: home
nav_order: 10
parent: Installation & Hosting
---


# Self-hosting

The buggy race server is a Python Flask application that connects to an SQL database. It is possible to run these "natively" but the [race server repo](https://github.com/buggyrace/buggy-race-server) includes the necessary Docker files to deploy within a Docker container. If you're self-hosting this can make things easier.

## Environment variables

The application needs to connect to a database, which is specified by the environment variable `DATABASE_URL`.


## Running locally

If you want to run the race server locally (for experimentation, development,
or just curiosity) you can do so — remember you'll need to set up a database too (although if you're just testing, sqlLite might be OK).

The Python requiresments are, as is standard, listed in `requirements.txt`, so you'll need to use `pip` to load them:

    pip install -r requirements.txt


