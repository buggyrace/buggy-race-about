---
title: Technical details
layout: home
nav_order: 110
---


# Technical details

{: .note}
For general requirements for running this project, see
[these requirements](overview/requirements).

The Race Server is a Python Flask application.

> GitHub repo: [buggyrace/buggy-race-server](https://github.com/buggyrace/buggy-race-server)

See the server's
[`requirements.txt`](https://github.com/buggyrace/buggy-race-server/blob/main/requirements.txt)
for the Python libraries it uses.

There's a [`Dockerfile`](https://github.com/buggyrace/buggy-race-server/blob/main/Dockerfile)
so you can [deploy it with Docker](../hosting/self-hosting).

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
source software**.  
Some components from other projects may have different licensing.

---
> See the [about pages](about/software) for more about the software behind
> project.

