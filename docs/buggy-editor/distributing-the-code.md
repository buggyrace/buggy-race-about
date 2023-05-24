---
title: Distributing the code
layout: home
nav_order: 20
parent: Buggy editor
has_children: false
---


# How students get their copy of the source code

The project requires each student to have their own copy of the buggy editor
source code, which they then develop. This page is about how you ensure all your
students get that code to start with.

This follows on from [customising the editor repo](customising): it assumes you
have customised the code (possibly in your own forked repo, if you're using
Git), and made it ready for distribution.

Here are three ways to distribute the code — they are not mutually exclusive,
although it's probably simpler for both you and your students if everyone is
doing it the same way.

1. **You zip up your customised source:**  
  **...then distribute that zip file to your students**  
  Students don't need any contact with Git or GitHub (in fact, neither do you:
  see note below).  
  <br>
  or...

2. **You direct students to your customised repo:**  
  **...then students either `git clone` or download the zip**  
  Students do not need a GitHub account, and can use Git _if they want_.  
  <br>
  or...

3. **Students fork your customised repo into their own account:**  
  **...then students either `git clone` or download the zip**  
  Students _must_ have GitHub accounts, and can use Git and GitHub Issues (for
  tasks) _if they want_, including pushing changes back to their repo. Although
  this is the most complex of the three methods, we've automated it on the
  server (see below), so it's straightforward for the students.  
  <br>

You need to decide on this before the project starts, because it may affect
some of the config settings you should choose. The third option is the most 
complex, but the server automates the process.

Check that the documentation reflects what you want your students to do — that
might be in the editor's (customised) README, as well as the phase 0 tasks
and the tech notes.

{: .rhul}
We used the third method: initially, we automatically forked the buggy editor
into each student's GitHub account, which they then either cloned or downloaded
by zip. Later (for the third time we ran the project and onwards), we
semi-automated that last stage by cloning onto our [remote server through
VSCode](running-remote).  
In effect, we used GitHub as a convenient way to distribute the code — this
makes it a little easier for us (you), and also exposes students to Git and
GitHub in the process.  
Once students had the code, we explicitly made it clear that using Git or
GitHub was entirely optional within the project, and most never used it (which
was fine). But those who did — because we'd injected the issues too — were free
to play with it _properly_.

## Working entirely without Git

{: .note}
If you want to just use a zip file, students don't need to use Git or GitHub.
In fact, neither do you: you can download the code, and customise it in place.

To get the zip file containing the source code for the editor, go to the
[editor repo on GitHub](https://github.com/buggyrace/buggy-race-editor),
click on the green **Code** button, and choose **Download zip**. 

Remember to [customise the source code](customising) before zipping it up
again. Then you can distribute that zip file to your students directly — for
example by emailing it, or it putting somewhere they can download from (if
you're using a system like Moodle, Canvas or Blackboard, you can put it on the
course pages as a resource to download).

{: .navigation}
**Admin** → **Config** → Config:**GitHub**

Set `IS_STUDENT_USING_GITHUB_REPO` to `No`.

{: .note}
Make sure your students know how to extract files from a zip. It will matter
_where_ in their file system they extract the application, and whether or not
they create an enclosing folder when they unzip it. The current Windows user
interface makes this surprisingly confusing, because it encourages opening the
zip file without explicitly extracting it.

## If students will be using GitHub

{: .navigation}
**Admin** → **Config** → Config:**GitHub**

Set `IS_STUDENT_USING_GITHUB_REPO` to `Yes`.

This setting only affects how some of the information on the server is
presented. We recommend you also enable automatic forking (see next section).

## Enable automatic forking

The server can automatically fork the repo into each student's GitHub account
(and, optionally, inject GitHub issues too — one for each task). We recommend
this if you want to expose your students to Git _even though they don't need
to use it_.

To enable this, there's a little more set-up required on your part. You need a
GitHub Oath app that has permission to fork into their GitHub accounts. You
set this up on GitHub, but need to tell the race server the app ID and client
secret.

{: .navigation}
**Admin** → **Config** → Config:**GitHub**

Set `IS_STUDENT_USING_GITHUB_REPO` to `Yes`.  
Set `IS_USING_GITHUB_API_TO_FORK` to `Yes` too. 
See the notes on setting up the OAuth app, below, because you need to add
`GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET` values to enable it.

Set `IS_USING_GITHUB_API_TO_INJECT_ISSUES` to `Yes` if you want that feature
too. Depending on the level you're teaching at, use of Git (including feature
branches against each of these issues) could form part of your assessment.
That's up to you. Even if you're not using Git, we think that having the tasks
as issues is a passive way to help interested students appreciate how Git
Issues can form part of a professional workflow.


### Setting up the GitHub OAuth app

{: .note}
You only need the GitHub OAuth app if you have set the config setting
`IS_USING_GITHUB_API_TO_FORK` to `Yes`.  
If you're not automatically forking the buggy editor source code into students'
GitHub accounts, you don't need to do this!

The OAuth app requests permission from the student for write access to their
GitHub account, in order to fork the repo for them (and, if you have chosen it,
to inject the tasks too).

You need to create the OAuth app up on GitHub. There's no coding involved
(because your race server already has the "back-end" code needed for the
callback): you just have to fill in the online form. The name of the GitHub
account you use will be exposed to your students (which is already the case if
you've committed your customisations to the editor source code with it).

> **See the instructions on GitHub for
[Creating an OAuth App](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app)**

These are the key points:

* Set the app's _Homepage URL_ to your race server's URL (this is what you set
  in the config setting `BUGGY_RACE_SERVER_URL`)

* For _Application description_, add something that will confirm to your
  students that this is the right place, such as "XYZ Buggy Racing server for
  the ABC course"

* For _Authorisation callback URL_, this must be a full URL to your race server,
  starting with `https://` with the path `/oauth/github/callback`  
  For example, it should look something like:  
  `https:www.example.com/oauth/github/callback`

* Provide a logo — either make your own or reuse/edit our
  [basic stripey square](/docs/img/stripe-square.png).

When you've created your OAuth app, GitHub will show you its ID and invite you
to set a secret. You need to tell your race server both of these values: put
those into the config settings `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET`.
Be careful with that secret: treat it as sensitive password. A malicious
attacker with access to the secret could abuse students' GitHub accounts. (It
is, by necessity, held in plaintext backstage on the server, which is why you
must take security on your server seriously too).

This OAuth app is only used when setting up the students' repos — it's not used
again once all your students have got their editor source code.


---
* Previous: [Customising the editor](customising)
* Next: [Where to run the app?](running-where)
