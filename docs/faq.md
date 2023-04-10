---
title: FAQ
layout: home
nav_order: 200
---

# FAQ

Frequently asked questions for administering the race server.

---

## Can I delete a user?

You can't delete a user, but you can mark them as _inactive_, which is effectively the same. Go to **Admin** → **Users**, pick the user and **Edit**. For **Is active?**, select `No`. This hides the user and also prevents them logging in. When you download buggies CSV, only buggies belonging to active users are included.


## I've forgotten the authorisation code

You can reset this by [setting it as an environment variable](customising/env)
and resetting the race server. You should then remove the environment declaration (because the value you've just set is now saved in the database).


## I've forgotten my password and can't log in

An administrator who knows the authorisation code can set any user's password (typically you do that and then invite the user to change it to one only they know as soon as they've got back in). Note the authorisation code is needed to change another admin user's password.

If you're a Teaching Assistant, you may be able to reset students' passwords (it depends if `IS_TA_PASSWORD_CHANGE_ENABLED` is `Yes`).

If nobody can log in as an administrator,  you can register a new
admin user (see next answer).

Change passwords by going to **Admin** → **Users** → **Change passwords**.


## I've accidentally demoted/deactivated the only admin account

[Set the environment variable](customising/env) `IS_PUBLIC_REGISTRATION_ALLOWED` to `1` (true).
Reset the server and go to `/admin/users/new`. Create a new admin user with a known password. You'll need the current authentication code. If you've lost that too, then set a new one as an environment variable too: `AUTHORISATION_CODE`.

Once you've got a new admin user, log in with the new credentials, and remove the environment variable declarations  (because they're now saved in the database). Promote or register the user that was lost — and once you've done that, maybe
[deactivate the new one](#can-i-delete-a-user).

