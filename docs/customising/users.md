---
title: Users config
layout: home
nav_order: 80
parent: Customising
has_children: false
---


# Configuring users

{: .navigation}
**Admin** → **Config** → Config:**Users**

You can choose what data is stored with your users. The simplest form is for
your users to _only_ have a username — this might be all you need. Usernames
are always lower case.

{: .note}
The server will display usernames with title case (intial caps) if config
setting `IS_PRETTY_USERNAME_TITLECASE` is `Yes`.  
For example, do this if the usernames you are giving students are based on
their names.

You can also add other fields to users _but these are not necessary_. It might
be helpful for you to add them so you can more easily identify the students
when on the race server. By default, users have none of these extra fields. If
you want them you need to explicitly add them — ideally during the
[set-up phase](setup-phase) before you register any users.

These are the **optional** fields you can add:

* email address
* first name
* last name
* VCS username — for example GitHub or GitLab
* external username — for example, if students have a college username
* external ID — perhaps the ID from an online learning system like Moodle,
  Canvas, or Blackboard

If you use external username and external ID, you should configure the _names_
of those columns too. For example, the external username might be "College
username", or the external ID "Moodle ID". See notes on each, below.

{: .warning}
You _can_ change these settings **after** you've registered users, but be
careful because if you add a new field after you've registered any user, the
field will be blank (you must [edit each user](../running/user-management)
manually to fix it). Similarly, removing a field won't purge its value from the
database.

If your students are using GitHub, the GitHub account information is stored _in
addition to_ these fields. You don't enter that, as the race server stores it
when each student authenticates their GitHub account.

## Email address

Currently, the race server never sends emails, so you only need add this if you
think it will be helpful to disambiguate students.

## First name and last name

Again, these are only used for identification. If you've allocated usernames
based on names, then _also_ storing one or both of these might be useful
(for example, if you've allocated usernames like "olivia1" and "olivia2").

## VCS (e.g., GitHub) username

The _name_ of the VCS that is displayed on the race server interface (for
example, "GitHub username" or "GitLab username") is set in the `VCS_NAME`
setting in the [VCS config group](vcs). Unlike the other optional fields for
users, the VCS username might be used by the race server: it depends on how
you're [distributing the Buggy Editor code](../buggy-editor/distributing-the-code)
(the `autofork` or `vsremote` methods add a GitHub access token to each user too).

Even if you're distributing the source code by GitHub, you might not need to
store the students' GitHub usernames on the race server. If the method you're
using requires it, the Config settings interface will tell you, so if you're not
sure — like the other optional fields — leave it out.

## External ID

External IDs are currently only for your convenience — the race server does
not use them.

The external ID might be useful if you use an online learning system like
Moodle, Canvas, or Blackboard. The buggy race server does not directly help
with marking or assessment, but if you are going to need to automatically
match buggy race usernames with students' IDs on such a system, it might be
useful to store this with the user.


## External username

If students have another username or ID that you use, store it here. If you require your students to log into a remote server, using
a different username to the one on the buggy race server, then set this here.

You can also set the _name_ of this username (for example, "College username")
using the config setting `EXT_USERNAME_NAME`. This can help prevent confusion
with students between different usernames. You should also set
`EXT_USERNAME_EXAMPLE` to be an example username: it's very helpful to students
(and maybe staff) if the format of the username helps dismabiguate it from
other usernames they might need in other contexts.


### Placeholders and login message

If you're running the buggy racing as part of an institution (such as a college), it can be confusing to students which username should be used on
which website. You can set example placeholders for both the username and
external usermname (if you're using it) with the config settings
`USERNAME_EXAMPLE` and `EXT_USERNAME_EXAMPLE` respectively.

You can also set a custom message that appears on the login page:
see [how to set announcements](../running/announcements).

## Config settings ("Users")

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `IS_PRETTY_USERNAME_TITLECASE` | Should usernames (which are always lower case) be displayed using title case? For example, choose `Yes` if the usernames you're using are effectively students' names. Login is always case insensitive, so this only affects how usernames are displayed, not what users need to type.  <br><br> _Default value:_ `Yes` |
| `USERS_HAVE_EMAIL` | Do users need email addresses? The server doesn't send emails so you don't need this field unless it's a useful way of identifying a student.  <br><br> _Default value:_ `No` |
| `USERS_HAVE_FIRST_NAME` | Do users need to have a first name? You might be using each student's first name as the username, in which case you don't need this.  <br><br> _Default value:_ `No` |
| `USERS_HAVE_LAST_NAME` | Do users need to have a last name? If you can already identify your students from the other fields, you might not need this.  <br><br> _Default value:_ `No` |
| `USERS_HAVE_VCS_USERNAME` | Do users have an external username for a version control system (VCS) such as GitHub or GitLab? You might want or need to store each student's VCS username depending on whether or not your students need to use a platform like GitHub or GitLab (which you specify by your choice of `EDITOR_DISTRIBUTION_METHOD` setting in the Project group). If you set this to `Yes`, make sure you set the `VCS_NAME` setting in the VCS group so everyone knows what platform this username is for. If you're not using a VCS, leave this as `No`.  <br><br> _Default value:_ `No` |
| `USERS_HAVE_EXT_USERNAME` | Do users have an external username or account that's specific to your organisation or institution? You might not need this, or you might already be using it as the username — in which case choose `No`. Note: the race server does **not** use this for authentication (i.e., there is no OAuth implementation). However, if your users need to log into a remote server for development _and_ you are using VS Code workspace files, you will need this to be `Yes` — unless you're simply using those external usernames as the students' race server usernames when you register them.  <br><br> _Default value:_ `No` |
| `USERS_HAVE_EXT_ID` | Do users have an ID from an external system? This might be useful if you want to match students with their existing ID on another system like Moodle, Blackboard or Canvas. You don't need this unless it's a useful way of identifying a student. If you do set this to `Yes`, you should also set `EXT_ID_NAME` to describe what it is.  <br><br> _Default value:_ `No` |
| `USERNAME_EXAMPLE` | A placeholder string used in the login form. This can be especially helpful if students use a different username for accessing other college systems. You can set this to be blank.  <br><br> _Default value:_ `hamster` |
| `EXT_USERNAME_NAME` | If users have an external username, what is it called? For example: "College username". This is to clearly differentiate the race server username (which students use to log into this race server) from this external one (which they presumably use to access other course systems). Keep it short, because it's used on buttons in the admin. This setting is ignored if `USERS_HAVE_EXT_USERENAME` is `No`.  <br><br> _Default value:_ `Ext. username` |
| `EXT_USERNAME_EXAMPLE` | If users have an external username, provide an example format (e.g., `abcd123` or `ada@example.org`). Note that this only serves as a placeholder suggestion when inputting — it's not used to validate or force the format of inputs. This setting is ignored if `USERS_HAVE_EXT_USERENAME` is `No`.  <br><br> _Default value:_ `abcd123` |
| `EXT_ID_NAME` | If user have an external ID, what is it called? For example: "Student number", "Moodle ID", "Blackboard ID", "Canvas ID". This setting is ignored if `USERS_HAVE_EXT_ID` is `No`.  <br><br> _Default value:_ `External ID` |
| `EXT_ID_EXAMPLE` | If users have an external ID, provide an example of what it might look like. This setting is ignored if `USERS_HAVE_EXT_ID` is `No`.  <br><br> _Default value:_ `12345` |
| `IS_TA_EDIT_COMMENT_ENABLED` | Teaching Assistants cannot edit user data. But do you want TAs to be able to add or edit comments left by staff?  <br><br> _Default value:_ `Yes` |
| `IS_TA_PASSWORD_CHANGE_ENABLED` | Administrators can change all other users' passwords. Choose `Yes` if you also want Teaching Assistants to be able to change (non-staff) users' passwords. Note that students who forget their passwords cannot reset them, and will need to ask a staff member to do it — so enabling TAs might be helpful. Changing a student's password does not require the auth code.  <br><br> _Default value:_ `Yes` |
| `IS_TA_SET_API_KEY_ENABLED` | Do you want your Teaching Assistants to be able to set (or clear) student's API keys? If you're using the default tasks, students don't need these until they are in phase 4.   <br><br> _Default value:_ `Yes` |
| `USER_ACTVITY_PERIOD_S` | The period (in seconds) over which each logged-in user's activity is logged. Pragmatically, this avoids updating the database on every request, because usually you're only concerned about whether or not a student has logged in recently, not the accuracy of the timestamp. This updates the "last activity" timestamp if the user sends a request this-number-of-seconds since the last recorded activity.  <br><br> _Default value:_ `300` |


 ---
 * Previous: [Tasks config](tasks)
 * Next: [Races config](races)

