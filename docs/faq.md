---
title: FAQ / troubleshooting
layout: home
nav_order: 200
---

# FAQ / troubleshooting

Frequently asked questions for administering the race server.


<details open markdown="block">
  <summary>
    Questions:
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

---

## My server is running but pages are unstyled

This can happen if [Webpack](https://webpack.js.org) has failed. Webpack
depends on node.js, and is a pre-processor that bundles all the static assets
(JavaScript, images, and — the first thing you notice if it's not working — CSS
(stylesheets)). If you have access to the command line where your server is
running, try running `npm run build` and look for diagnostic/error messages.

---

## I see "There was a problem at start-up" (and code 500)

Check the message that accompanies the warning. There are two distinct
kinds of problem — notice which of these two you're seeing:

* "probably a failure to connect: check DATABASE_URL and error logs"
* "app had unpopulated database (missing table): need to run migrations first,
   or schema.sql?"

In the first case, check that your `DATABASE_URL` is correct. If you're using
something like Postgres or mySQL, check that you really can (manually) connect
to the database using the authorisation criteria you've included in the URL.
Remember that the username and password here are for the _database_, and
nothing to do with (for example) any passwords or auth codes on the race server.

There are a couple of special config settings which affect the way that
`DATABASE_URL` is used, so if you're sure the username and password you've
provided in that string are correct, these might help: see more about
[database-related environment variables](customising/env#important-variables-you-must-or-should-set).

You can see examples of what the `DATABASE_URL` should look like for different
kinds of database (including the SQLite one: see note below) by looking inside
[`env.example`](https://github.com/buggyrace/buggy-race-server/blob/main/env.example).

In the second case — where you see the "unpopulated database" message — the
connection (and hence `DATABASE_URL`) is OK but you've managed to run the race
server before you've populated the database. Specifically, the tables the app
expected to find in there don't exist yet. These are usually set up by running
Flask's _database migration_. You won't be able to run your set-up phase until
you've fixed this.

If you're using Docker or Heroku, the start-up process automatically runs 
Flask's database migrations before it launches the webserver, which takes care
of this (the migrations make the tables). If that's not working for you — which
is unexpected, so get in touch — there will be failure messages in the build
or release logs that should help with diagnosis.

You can explicitly run the database migrations using:

     flask db upgrade

If you can't run the Flask database schema migrations, but you know your way
around SQL, then there's a 
[`schema.sql`](https://github.com/buggyrace/buggy-race-server/blob/main/db/schema.sql)
in the server repo that you can use to populate the database manually instead.

An extra tip: if you're having database problems, one thing to try is switching
your `DATABASE_URL` to use SQLite — just as a test — and see if you get the
same problem. This can be handy because SQLite doesn't use any authorisation
credentials, which is why that's a good smoke test: you can't get a password or
username wrong.


---

## Server responds to every request with unknown key error (and code 500)

This used to be the behaviour of the server if the database connection was
missing at start-up — we've since changed this, so now you get the more informative
warning [described above](#i-see-there-was-a-problem-at-start-up-and-code-500).
If you're still seeing this message then maybe the database connection has gone
down while the app has been running. Try restarting the database, check it's
running, and that the connection criteria in your
[`DATABASE_URL` setting](../customising/env.html#database_url) still work. Once
you know the database is good again, restart the race server.


---

## Error: Could not locate a Flask application

If you see this error and you're trying to launch the app — or the database
migrations — from the command line, then perhaps your `FLASK_APP` environment
variable is wrong (maybe from another project entirely?), you haven't set
one at all, or you're trying to launch from the "wrong" directory.

First, `cd` to the directory that contains the application files and try again.

If that doesn't work, then the error message probably goes on to suggest
setting `FLASK_APP` or using the `--app` option. How you do that depends a
little which platform you're on: see
[set or export env variables](customising/env#set-or-export-environment-variables-explicitly).
Provided you are in the right directory (because the values here are
relative), either one of these values should work: `autoapp.py` or
`buggy_race_server/app.py`.

---

## Can I delete a user?

Yes, and if you delete a user their buggy and task texts will be deleted
too. If you delete a user, you can't get them back, so only do it if you're
sure you don't want their data (for example, if they were added by mistake).
See [Deleting a user](running/user-management.html#deleting-a-user).

If you want to _suspend_ a user, you can mark them as _inactive_, which is
like deletion without destroying the data. Go to **Admin** → **Users**, pick
the user and **Edit**. For **Is active?**, select `No`. This hides the user
and also prevents them logging in. Inactive users' buggies are excluded from
race files: when you download a race file for a race, only buggies belonging to
active users are included.

You can also [disable a user's login](running/user-management.html#enabling-or-disabling-logins)
if you just want to prevent them logging in or changing anything on the server.

It is possible to bulk delete users, although we anticipate this only being
useful at start-up, so (if you have the default settings) it is hidden from the
interface once the students records are no longer "fresh". See
[bulk deleting users](running/user-management.html#bulk-deleting-users).

---

## I've forgotten the authorisation code

You can reset this by [setting it as an environment variable](customising/env)
and restarting the race server. You should then remove the environment
declaration (because the value you've just set is now saved in the database).

---

## I've forgotten my password and can't log in

An administrator who knows the authorisation code can set any user's password
(typically you do that and then invite the user to change it to one only they
know as soon as they've got back in). Note the authorisation code is needed to
change another admin user's password.

If you're a Teaching Assistant, you may be able to reset students' passwords
(if the config setting `IS_TA_PASSWORD_CHANGE_ENABLED` is `Yes`).

If nobody can log in as an administrator, see
_[I’ve accidentally demoted/deactivated the only admin account](#ive-accidentally-demoteddeactivated-the-only-admin-account)_.

Change passwords by going to **Admin** → **Users** → **Change passwords**.

---

## I've accidentally demoted/deactivated the only admin account

[Set the environment variable](customising/env) `IS_PUBLIC_REGISTRATION_ALLOWED`
to `1` (true). Restart the server and go to `/admin/users/new`. Create a new
admin user with a known password. You'll need the current authentication code.
If you've lost that too, then set a new one as an environment variable too:
`AUTHORISATION_CODE`.

Once you've got a new admin user, log in with the new credentials. Go to
**Admin** → **Config** → **Server** and set `IS_PUBLIC_REGISTRATION_ALLOWED`
back to `No`. Remove the environment variable setting you used to bypass that
(do not forget this step: otherwise, you'll have public registration again next
time you restart). Promote or register the user that was lost — and once you've
done that, maybe [deactivate or delete the new one](#can-i-delete-a-user).

---

## Oops! An announcement with bad HTML is breaking every page

Announcements are uniquely dangerous because if you accidentally fail to
"balance your tags" they can have a destructive effect on page layout
(including the pages for fixing it). You can resolve this by editing the
announcement to remove the offending HTML. Specifically, you can
[disable the HTML to get to the edit-announcements pages](running/announcements.html#recovering-from-an-announcement-with-critically-broken-html).

---

## Why can't I replay this race?

If you are looking at a race on the server and you can't see a **Replay**
button, it may be because the race hasn't been run yet (no results have been
uploaded) _or_ the race still has the results hidden from students
(go to **Admin** → **Races** → Race:**Details** **Edit**, and fix _Are results
visible?_). If it's neither of those, check that there is a URL for
`race_file_url` (described as "URL of race file (JSON)"). If there's no race
file URL to replay, the server won't show the **Replay** button.

If the **Replay** button is there but the problem is that the race won't run
— if it says there are no events, for example — then maybe you've uploaded the
wrong race file. It must be a race file with _events_ in it for the player
to show them. See [running races](races/running) for more information.

The route of a race is defined by the path inside an [SVG file](glossary#svg):
if that won't load, the race can't be replayed. If that's the problem, see
[Racetrack not working: "Problem getting SVG"](#racetrack-not-working-problem-getting-svg).

---

## I made a task text but it's not showing up! Where is it?

You can access you own task texts by clicking on **Settings** →
**List your task texts**.
This is where you can find all the texts you've made, as well as editing (or
even deleting) them.

If you're not an enrolled student (for example, you're a Teaching Assistant
or admin) then your texts _will not appear_ on 
[the main text matrix](teaching/report-and-poster.html#using-task-texts).
That only shows the texts for active (that is, not suspended) students.

This is why, while you're setting up the course, it's OK to set staff users to
_also_ be "enrolled students", so you can experiment with things like this and
see how it looks. Just remember to [edit the user](running/user-management.html#edit-a-user)
to remove enrolled student status from any staff accounts before the course
starts.

Note that task texts can be disabled _entirely_ by setting
`IS_STORING_STUDENT_TASK_TEXTS` to `No`: see the
['Tasks' config settings](customising/tasks).


---

## What's the difference between an external ID and an external username?

Very little — both are _optional_ settings (with string values) that you can
save with each of your users if that's helpful. We used both at Royal
Holloway because students had both a college username (which we were using for
the more [complex VSCode distribution
method](buggy-editor/distributing-the-code#method-vsremote)) and an underlying
Moodle ID which helped us when doing our assessments/marking.

You can enable either or both of these, together with giving them descriptive
names and example values, via the ["Users" group of config settings](customising/users).

---

## Racetrack not working: "Problem getting SVG"

If you look at a race or a racetrack as an admin and you see "Problem getting
SVG", there are a couple of things to check. If you have this problem, it
probably means the race won't replay on the [race player](races/replaying)
either.

First, try hitting the racetrack SVG's URL in the browser (view either the race
or the racetrack in the admin): you should not get a 404. If you do, then
either the URL is wrong, or the SVG file has been deleted since the URL was
added.

If it's not that, the other reason might be a [CORS
problem](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors). This
can happen if the SVG is coming from a different domain than your race server.
If that's the case, look in your browser's console for messages such as
`Cross-Origin Request Blocked`. If that's what you see, you need to either
modify the server that's sending the SVG file to send the correct CORS headers
or, if you can't do that, host it on a server that does. SVG files served from
[GitHub Pages]() sites have wildcarded CORS headers, so those should work. The
most certain way to avoid CORS problems is to serve the SVG file from the same
domain as the requester — in this context, that's almost certainly the race
server whose race player you are running. If you're hosting your own race
server consider adding static files such as the racetrack SVG to the repo you've
forked. Look in `buggy_race_server/race/assets/tracks` to see the race server's
default racetracks, and add your own alongside those. You can access them on
your server at `/races/assets/tracks/filename.svg`. Note that racetrack assets
like this are treated differently from general static content (such as images
or CSS) because they are not handled by [Webpack](glossary#webpack).

---

## Why can't I see all the (yellow) admin links at the top of my admin pages?

There are a couple of admin pages that are contextual, and if your project is
not using them, they are not displayed. For example, if your choice of 
[distributing the code](buggy-editor/distributing-the-code) does not use the
Buggy Editor source code _on the race server_, the link to that admin page is
not displayed (it's `/admin/buggy-editor`). Similarly if you have disabled the
display of [tech notes](static-content/tech-notes), then that link is not
displayed on the admin (it's at `/admin/tech-notes`).

The [admin dashboard](running/dashboard) always shows all the available admin
"nav" links on the top. But on other admin pages, the second line is collapsed
to save space. Use the **···** button to expand it, or **·×·** to collapse it.
You can make these decisions "sticky" (so they _always_ expand or collapse when
the page is loaded) by clicking on your username on the top right menu bar, and
selecting your _Admin button preference_.

Finally, some of the admin pages are only available to administrators, so if
you're logged in as a Teaching Assistant, some of those admin links will be not be enabled.

---

## Why does it say "hamster" in the login form? Can I change that?

It's the default example username being used as a placeholder. You can change
it (or set it to be blank) by editing the `USERNAME_EXAMPLE` config setting (in
the **Users** group). It may be helpful to set an example here to distinguish
the race server's usernames from those your students may be using on other
systems. For more about this — and external usernames — see
[customising users](customising/users). You can also
[set a login message](running/announcements) to display above that form.

The [hamster](glossary#hamster) is one of the forms of motive power available
to racing buggies.

---

## How can I find out what version I'm running?

Go to **Admin** → **Dashboard** → **System info** where it's at the top of the
page.  
Or look under the hamster on the <code>/about</code> page.

This documentation is up-to-date for Buggy Race Server version
**{{ site.content.server_version }}**.

---


