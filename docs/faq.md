---
title: FAQ / troubleshooting
layout: home
nav_order: 200
---

# FAQ / troubleshooting

Frequently asked questions for administering the race server.

---

## My server is running but pages are unstyled

This can happen if [Webpack](https://webpack.js.org) has failed. Webpack
depends on node.js, and is a pre-processor that bundles all the static assets
(JavaScript, images, and — the first thing you notice if it's not working — CSS
(stylesheets)). If you have access to the command line where your server is
running, try running `npm run build` and look for diagnostic/error messages.


## Server responds to every request with unknown key error (and code 500)

If you _always_ see a 500 error and in the logs that's an unknown key error
looking for a config setting — your server isn't connecting to the database.
All the config (except environmental overrides) is in the database, so if
the server can't connect to that the first thing the app fails at will be
getting its own configuration. Check that your database server is running and
that the `DATABASE_URL` you've specified for it works for you if you try
connecting directly.


## Can I delete a user?

You can't delete a user, but you can mark them as _inactive_, which is
effectively the same. Go to **Admin** → **Users**, pick the user and **Edit**.
For **Is active?**, select `No`. This hides the user and also prevents them
logging in. When you download buggies CSV, only buggies belonging to active
users are included.


## I've forgotten the authorisation code

You can reset this by [setting it as an environment variable](customising/env)
and restarting the race server. You should then remove the environment
declaration (because the value you've just set is now saved in the database).


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
done that, maybe [deactivate the new one](#can-i-delete-a-user).


## Oops! An announcement with bad HTML is breaking every page

Announcements are uniquely dangerous because if you accidentally fail to
"balance your tags" they can have a destructive effect on page layout
(including the pages for fixing it). You can resolve this this by editing the
announcement to remove the offending HTML. Specifically, you can
[disable the HTML to get to the edit-announcements pages](running/announcements.html#recovering-from-an-announcement-with-critically-broken-html).
