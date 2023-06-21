---
title: Customising the editor
layout: home
nav_order: 10
parent: Buggy editor
has_children: false
---


# Customising the Buggy Editor

{: note}
This page is about customising the **buggy editor repo** — you should do this
**before** sharing the URL with your students.

Before you start running the project, you need to prepare the buggy editor
source code that your students will start with. The recommended way to do this
is to fork our "plain" buggy editor repo from
[github.com/buggyrace/buggy-race-editor](https://github.com/buggyrace/buggy-race-editor).

{: .note}
You don't **need** to customise the buggy editor source code before sharing it
with your students, but if you don't it means the students' apps won't link
helpfully back to your race server... which can be confusing.  
We strongly recommend you customise the editor!

To fork the repo, log into your own GitHub account, then go to the
[buggy editor repo](github.com/buggyrace/buggy-race-editor) and click **Fork**
(near the top right). You'll get a (public) copy of the editor repo, which is
the one you can edit. There are two files that you should change:

* **`README.md`**  
  The server can suggest a README for you which incorporates some of your
  config settings (specifically, your race server URL)
* **`app.py`**  
  The basic Python script includes constant `BUGGY_RACE_SERVER_URL` whose value
  should be the URL of your race server

## The server can suggest your custom README

{: .navigation}
**Admin** → **Config** → **Buggy Editor**

The server can recommend a custom README by using the config settings you've
made. The server's buggy editor page provides an example `README.md` that you
can copy, and use to replace the contents of the existing README.

{: .warning}
Check that everything in that README is appropriate and helpful for your
students — some things may depend a little on how and where your students will
be running it.

The details in the README may need to change according to how you anticipate
your students running their editor apps. For example, the default README
directs students to find their running app at `localhost:5000` at Flask's
default port 5000. But if you will be encouraging your students to run on
[pythonanywhere](https://www.pythonanywhere.com) or
[repl.it](https://replit.com)] that might be misleading.

{: .note}
The README suggestion text incorporates your config settings (including,
crucially, `BUGGY_RACE_SERVER_URL`) so make sure those settings are up-to-date
before copying it.


## Fix the SERVER_URL  in app.py

There's a constant called `BUGGY_RACE_SERVER_URL` in `app.py` that is used as
the target of links back to your race server. Change this line:

    BUGGY_RACE_SERVER_URL = "https://RACE-SERVER-URL"

to contain the URL of **your** buggy race server.

## Commit those changes

Remember to commit the changes!

Since these customisations are happening _before_ your project has begun, there
is a case for using `git rebase` to "flatten" the history so it only contains
one commit ("Initial commit"). From the students' point of view, the
relationship between our repo and your customisations isn't relevant detail.

## Update the server GitHub config

If you have forked (and customised) the editor repo, be sure to set the config
to point at **your** fork of the repo, and not ours.

{: .navigation}
**Admin** → **Config** → Config:**GitHub**

These are the config settings you should change/check:

* `BUGGY_EDITOR_GITHUB_URL`
* `BUGGY_EDITOR_REPO_NAME`
* `BUGGY_EDITOR_REPO_OWNER`

Normally, the repo name and the repo owner should also occur within the URL.


---
* Previous: [What is the buggy editor?](the-editor)
* Next: [Distributing the code](distributing-the-code)
