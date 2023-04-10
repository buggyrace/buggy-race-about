---
title: Users config
layout: home
nav_order: 50
parent: Customising
has_children: false
---


# Configuring users

{: .highlight}
Go to **Admin** → **Config** → Config:**Users**

You can choose what data is stored with your users. The simplest is for your
users to _only_ have a username — this might be all you need. Usernames are
always lower case[^1].

You can also add other fields to users _but these are not necessary_. It
might be helpful for you to add them so you can more easily identify the
students when on the race server. By default, users have none of these extra
fields. If you want them you need to explicitly add them — ideally during the
[set-up phase](setup-phase) before you register any users.

These are the optional fields you can add:

* email address
* first name
* last name
* external username

{: .warning}
You _can_ change these settings after you've registered users, but be careful
because if you add a new field after you've registered any user, the field will
be blank (you must [edit each user](../running/user-management) manually to fix
it). Similarly, removing a field won't purge it from the database.

Note that if your students are using GitHub, the GitHub account information is
stored _in addition to_ these fields. You don't enter that, as the race server
stores it when each student authenticates their GitHub account.

## Email address

The race server never sends emails, so this is only used for identification. Like the other fields, you might not need this if the usernames you're giving
to your students are already clear.

## First name and last name

Again, these are only used for identification. If you've allocated usernames
based on names, then _also_ storing one or both of these might be useful
(for example, if you've allocated usernames like "olivia1" and "olivia2").

## External username

If students have another username or ID that you use, store it here. If you require your students to log into a remote server, and you're allocating 
different usernames (such as the students' names), then set this here.

You can also set the _name_ of this username (for example, "College username")
using the config setting `EXT_USERNAME_NAME`. This can help prevent confusion with students between different usernames.

### Placeholders and login message

If you're running the buggy racing as part of an institution (such as a college), it can be confusing to students which username should be used on
which website. You can set example placeholders for both the username and
external usermname (if you're using it) with the config settings
`USERNAME_EXAMPLE` and `EXT_USERNAME_EXAMPLE` respectively.

You can also set a custom message that appears on the login page:
see [how to set announcements](../running/announcements).



---

[^1]: The server will display usernames with titlecase if config setting `IS_PRETTY_USERNAME_TITLECASE` is `Yes` (for example, if the usernames are their names).