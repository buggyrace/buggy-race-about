---
title: Authorisation config
layout: home
nav_order: 10
parent: Customising
has_children: false
---


# Configuring authorisation

{: .highlight}
Go to **Admin** → **Config** → Config:**Auth**

You need to know the _current_ authorisation code in order to change it.

## About the authorisation code

The race server allows administrators to make operational changes, but some
actions _also_ require the authorisation code to be supplied. It's effectively
an extra level of "are-you-sure?" safety against hard-to-undo changes. Depending
on how you're running your site, and how many staff accounts you have, you might
not need to share the authorisation code with all staff.

In general, you need the authorisation code to change **configuration**
and **user details** (including registration).

## Initial set-up

The first step of the [set-up phase](setup-phase) forces you to set the
authorisation code for your site. By default, its initial value is `CHANGEME`.
If you're nervous about this, you can launch the set-up phase with a different
authorisation code by setting it to something secret via an
[environment variable](env) _before_ you start the server for the first time.

## Forgotten the code?

If forget the authorisation code, you can use the mechanism for overriding
_any_ configuration settings: explicitly set `AUTHORISATION_CODE` as an
[environment variable](env) and restart the server.

The authorisation code (like users' passwords) is hashed (that is, it is not
stored in plaintext on the server). So if you do forget it you can't simply
look it up backstage. Likewise, if you set it via an environment variable
declaration, remember to remove this declaration once you've restarted the
server.
