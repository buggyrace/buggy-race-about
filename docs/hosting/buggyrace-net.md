---
title: buggyrace.net
layout: home
nav_order: 30
parent: Installation and Hosting
---


# Using buggyrace.net

We do not offer any hosting service — either [self host](self-hosting) or
[host in the cloud with Heroku](heroku). But if you have problems setting up a
custom domain, we might be able to add your institution as a subdomain on
`buggyrace.net`, and `CNAME`d it onto your installation.

We provide the certificates to enable your server to self-certify the SSL
certificates it needs (in the `ssl` directory in the repo) — although if
you're hosting on Heroku, then their Automatic Certificate Management (ACM)
system works fine anyway.

If you are running your race server inside your institution's network, there
may well be some firewall configuration needed to let requests to the race
server get through.

