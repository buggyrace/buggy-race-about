---
title: Technical details
layout: home
nav_order: 110
---


# Technical details

{: .note}
The documentation you are reading applies to Buggy Race Server
version **{{ site.content.server_version }}**.


## How to check your race server version

{: .navigation}
**About** (version is below the hamser)
<br>or<br>
**Admin** → **Dashboard** → **System info**

If you're looking in the source code, the latest version string should be in
`buggy_race_server/config.py` as `MANUAL_LATEST_VERSION_IN_SOURCE`. You should
also find releases on the [GitHub repo](https://github.com/buggyrace/buggy-race-server).


## Summary of technical specs

For general requirements for running this project, see
[these requirements](overview/requirements).

The Race Server is a Python Flask application.

> GitHub repo: [buggyrace/buggy-race-server](https://github.com/buggyrace/buggy-race-server)

See the server's
[`requirements.txt`](https://github.com/buggyrace/buggy-race-server/blob/main/requirements.txt)
for the Python libraries it uses.

There's a [`Dockerfile`](https://github.com/buggyrace/buggy-race-server/blob/main/Dockerfile)
so you can [deploy it with Docker](../hosting/docker).

It was built on the
[flask-cookiecutter](https://github.com/cookiecutter-flask/cookiecutter-flask)
webserver, which comes with [Bootstrap](https://getbootstrap.com) and the
[JQuery](https://jquery.com) JavaScript utility library. The cookiecutter
also brought [webpack](https://webpack.js.org) along, which means the server
needs [node.js](https://nodejs.org/en) (to package up the JavaScript and CSS)
as well as Python.

Python version 3.9+ is required.

{: .note}
The Race Server is licensed under the GNU Affero GPL: it is **free and open
source software**.  Some components from other projects may have different
licensing: see [more about the licensing](about/software).

---
> See the [about pages](about/software) for more about the software behind
> project.

