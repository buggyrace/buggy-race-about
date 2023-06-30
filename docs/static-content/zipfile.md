---
title: The editor zipfile
layout: home
nav_order: 40
parent: Static content
---


# The Buggy Editor zipfile

The **buggy editor zipfile** contains the source code for the
[Buggy Editor](../buggy-editor/the-editor) application that each student works
on and develops.

{: .note}
You **only** need this if you have chosen to distribute the source to the students
on the race server (this is
"[method A](../buggy-editor/distributing-the-code#method-a)", which is the
default and simplest method you can choose).  
<br>
For example, if you're distributing the code via GitHub, **you do not need to
publish the zipfile**. 
 

## Publishing the zipfile on the race server

{: .navigation}
**Admin** → **Config** → **Buggy editor** → **Publish editor zipfile**

This is the default behaviour: you customise the README, and add the URL for
this race server to the Python (<code>app.py</code>) when you publish the 
zipfile.

### If you don't publish the zipfile — 404!

If you are using the default set-up, with the buggy editor being served by the
race server, but you don't publish them — or your hosting platform (e.g.,
Heroku) does not preserve them when you redeploy the software — the students
will get 404 errors when they follow links to download it. You must re-publish 
the zipfile manually. The [admin dashboard](../running/dashboard) and [set-up
summary](../running/setup-summary) both show warnings if the zipfile is missing.


