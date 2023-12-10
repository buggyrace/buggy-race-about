---
title: Privacy considerations
layout: home
nav_order: 50
parent: Installation and Hosting
---

# Privacy considerations

You have a moral and a legal responsibility to take the privacy of your students
seriously. The following notes cover the main things you should know and may
need to decide before you run the server.

## Always use TLS (`https://`)

If you're running a race server on the public internet, you should _only_ run
it over `https`, that is, as an encrypted service.

This will depend on how you are hosting the race server, but it may be
straightforward for you. Our instructions for [hosting on
Heroku](../hosting/heroku) cover this for you.

If you're self-hosting on your own infrastructure, you or your tech team should
be able to set this up on your own domain. If you're not familiar with SSL
certificates it can be a bit daunting, but
[letsencrypt.org](https://letsencrypt.org) has been enabling free encryption
on the net for years and is a good place to start.

Another way is to ask us to CNAME your site as a subdomain of `buggyrace.net`.
We've provided the certificates you need in the repo. Get in touch and we can
look into adding your site as a subdomain while you run your project.


## Basic security practice

The passwords you set on the race server are hashed (that is, they are not
stored in plain text) — with the exception of the initial auth code if you set
it as an [environment variable](.../customising/env), which is why, if you do
that, you should delete it as soon as you've completed your set-up.

Don't use weak, obvious or short passwords. Don't use duplicate passwords.
Don't share passwords. Make a point of looking away if a student or colleague
ever types theirs in front of you (it's a teaching point :-) — it also an
old-school nerd courtesy). Don't leave passwords in places where they can be
discovered. Encourage your students to adopt good security practice too. Use a
password manager!

If you believe a password has been compromised,
[user-management#changing-passwords](change it).

The race server does not support two-factor authentication. As a future feature
it would be good if it were integrated into your institutions OAuth login
scheme — but that's not in place yet.

## Hosting location: GDPR compliance

If you host the race server on the cloud you should check that the "cloud" data
centre you choose is compliant with the legislation in your country.

For example, if you use Heroku, you can currently choose "USA" or "Europe". See
this [information about GDPR compliance and Heroku](https://devcenter.heroku.com/articles/gdpr).


## Personal information

The _default_ set-up requires only a username — that you allocate to each user
— and a password for each student. That is, it's entirely feasible to run the
project without externally identifiable usernames if that's your need.

When you set up your server, you can choose to include additional information
about each user (that is, your students — although this includes your colleagues
too). See [customising Users](../customising/users) for details: you _can_
store names, emails, and other identifiers (including external usernames/IDs)
if you want to. We encourage you _not_ to add any information you don't really
need.

In addition, if you are using the GitHub API to automatically fork the buggy
editor repo into each student's account, then the race server will be storing
their GitHub access tokens. This is sensitive data and you must not store this
unless you are hosting the site in compliance with the legal requirements in
your region, and applying good security practices.


## Sensitive information

Be aware that as soon as students start using the site — uploading buggies and,
specifically, [saving notes for their reports](../teaching/progresss), then
the content of their work may be sensitive. You don't have control over what
they write, but in general it may also be an indication of progress and
engagement. This is of itself potentially sensitive information so treat it
accordingly.


## Cookies and data collection

There are no analytic cookies or tracking used by the race server. Cookies are
used to manage sessions — these are effectively functional, or "login", cookies
and store no sensitive information about the user.

There's no analytic tracking in place on the race server beyond the usual
logging of requests and errors in the webserver logs. For example, we don't
include Google analytics in the server source code. We don't use — or indeed
approve of — browser-based tracking of in-page activity (where the mouse goes,
where the focus is applied, or when it's taken away from the page) as a way of
tracking student engagement.

However, we do record _when_ students are logged in and active on the site. A
summary of this information is presented on the admin dashboard showing which
students have logged in in the last day, the last week, or never. See 
[tracking progress](../teaching/progress) for more about how you can see
which students are keeping up, and which are falling behind.


## Hiding usernames in race results

There's a config setting in the "Race" group called
`IS_USERNAME_PUBLIC_IN_RESULTS` — set this to `No` if you don't want students'
usernames shown in the race results and replays. By default this is `Yes`, and
usernames are shown.


