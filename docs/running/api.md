---
title: Race server API
layout: home
nav_order: 50
parent: Day-to-day running
---

# The race server API

The server supports a mechanism for uploading buggy JSON programmatically. It's
"the race server API" and students encounter it in task 4-API.

The API does not use the same login/session mechanism as the website. Instead
it requires a valid combination of username, key, and secret.


{: .demo}
See the full [public API specification]({{site.content.demo_url}}/api).

{: .demo}
See [task 4-API]({{site.content.demo_url}}/project/tasks/4-API),
which invites your students to _use_ the API.

{: .note}
If you edit the tasks so that the API task isn't in phase 4 any more, you
should [change the config setting](../customising/tasks) `TASK_NAME_FOR_API` in
the "Tasks" group.

| Key            | Value                                                      |
|----------------|------------------------------------------------------------|
| `username`     | Username of a valid, active user                           |
| `key`          | String for this user (set by staff, lasts until staff changes it) |
| `secret`       | String for this user (set by user, times out, and potentially only used once) |

These [config settings](../customising/server) in the "Server" group control
how the API criteria behave:

| Config setting               | Effect                                                         |
|------------------------------|----------------------------------------------------------------|
| `API_SECRET_TIME_TO_LIVE`    | Lifespan of API secret from the moment it is set.              |
| `IS_API_SECRET_ONE_TIME_PW`  | Can the secret be used repeatedly (within its lifespan), or is it one-time-use only? |
| `IS_STUDENT_API_OTP_ALLOWED` | If the secret is not a one-time password, can a student override their own so that it is? |

The API is an introduction to the usefulness of APIs: it's replacing a manual
process that the students have been using (copying and pasting the buggy JSON
into the upload form) with a programmatic one. The mechanism of using a key and
a secret (and potentially that secret being a one-time token) is an example of
how transactions like payments work on the web.


## Setting API keys

{: .navigation}
**Admin** → **API Keys**

As a staff member, you can set the API key for any individual user. Select the
user or users to which you want to allocate a key, and click **Generate API
keys**. The server will randomise a separate key for each user you selected.

Similarly, you can revoke a key by clicking **Clear API keys**.

We suggest that you do not grant API keys until individual students ask for
one. It's a simple way to check with their progress and an opportunity to see
how much they've understood about how the API works.

## Setting the API secret

{: .navigation}
Top menu bar: **Settings** → **API Secret**

Users set their own API secret.


## API test page

{: .navigation}
**Admin** → **API Keys** → **API Test**

If you're logged in as a member of staff, you can play with the API to see how
it works and what its (JSON) responses look like. The test generates a JSON
buggy description that contains only one value — `qty_wheels` — set to a random
integer. You'll need to set both a key and a secret if you want the API `POST`
call to succeed. This is a genuine API call so if the criteria are correct, it
will change your buggy.

{: .screenshot}
![Screenshot of staff API test](/docs/img/screenshots/api-test.png)

{: .caption}
The API test generates an HTTP `POST` request to the `/api` endpoint with the
parameters from the form.


