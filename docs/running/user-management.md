---
title: User management
layout: home
nav_order: 28
parent: Day-to-day running
---
# User management

<details close markdown="block">
  <summary>
    Contents of this page:
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

{: .navigation}
**Admin** → **Users**

The Users admin page lists all the users registered on the race server, 
showing data for each and providing links to investigate and edit each one.

Students are listed before staff.

You can choose which columns are displayed by clicking the white buttons at
the top of the table: they toggle the display of the respective column. The
show/hide choices are stored in your browser, so will be used whenever you
revisit this page. For example, once the project is running you probably don't
need to see the date each user was created, or their first login timestamp.
The user table can be a bit crowded, so you can also choose to truncate all
timestamps by only showing dates without HH:MM times.

{: .note}
In general, only administrators who know the authorisation code can change
other users' data. Depending on config settings (in the
["Users" group](../customising/users)), Teaching Assistants may be able to add
staff comments and reset students' passwords.

## Active vs. inactive users

If you mark a user as _inactive_, they are effectively suspended: they won't
be able to log in, their existing login session will be terminated, and they
won't be included in any downloads.

{: .rhul }  
Our definitive list of enrolled students came from the Moodle (we
exported that list, as a CSV, to
[register the students](../registering-users/spreadsheet) on the race server).
Inevitably one or two of those students might no longer be on the course, but
that doesn't always become apparent until term has started. Marking those as
_inactive_ on the race server kept everything in synch with the Moodle list —
no missing students — but kept them out of the way from our day-to-day running
of the project: Inactive students are not included in totals when [tracking
progress](../teaching/progress) or [running races](../races).

## Types of user

### Students

A user can be an _enrolled student_. This is used to distinguish students
who are actively engaged in the project from other users (such as staff —
although these are not mutually exclusive). In general, the race server decides
if a user should be included in the following collections based on their
_student_ status:

* display of task texts
* download of student data
* download of buggy data

It is possible for a staff user to _also_ be a student. This may be useful
before the project starts so staff can familiarise themselves with the server.
In general, you probably won't want staff to be marked as students once your
enrolled students have been registered. If you do, staff activity will be
included in the "students" statistics and downloads.

### Staff users: administrators and Teaching Assistants

There are two types of staff user:

* **Administrator**  
  Administrators are staff users with access to all the admin features of the
  race server.  
  Some admin changes require the admin user to also know the site's
  _authorisation code_.

* **Teaching Assistants**  
  Teaching Assistants (TAs) are staff users with mostly read-only access.  
  TAs may be able to set (i.e., change) students' passwords if the config
  setting `IS_TA_PASSWORD_CHANGE_ENABLED` is `Yes`, and edit staff comments on
  a user's record if `IS_TA_EDIT_COMMENT_ENABLED` is `Yes`.

The username you nominated as the admin user during the setup-up phase is
automatically an administrator.

### Other users: guest observers

It is possible for a user to be neither student not staff. These are
effectively guest accounts — you probably don't need them unless you want to
give access to colleagues who are not actively working on the course. Remember
to consider [privacy implications](../hosting/privacy) of granting access to
the race server.

## Inspect a user

When you're looking at the list on the _Users_ page, you can click on the
speech bubble icon to view the for-staff-only _comment_. The JSON button (with
a spanner icon) displays the last-uploaded JSON.

You can click on the username to inspect the user's settings and task texts
in detail.

## Commenting on a user

Staff users can leave comments on a user that are only displayed to other staff
users on the server (that is, students do not see these comments). By default
Teaching Assistants can edit comments as well as read them (although you can
disable this by setting `IS_TA_EDIT_COMMENT_ENABLED` to `No`). You'll see
comments (if any) when you inspect a user, but there's also a button (marked
with a speech bubble) for quick inspection when you're listing all users
(**Admin** → **Users**).

## Changing passwords

{: .navigation}
Top menu bar: **Settings** → **Change password**

Any user can change their own password while logged in.

If you're an admin user — or a Teaching Assistant and the server has enabled
this — you can change _any other user's password_ (but if _they_ are an admin,
you'll need the auth code too).

If you forget your password and you're not logged in, you _cannot_ reset your
password from outside (the server doesn't send emails, so can't send you a
reminder). You need a staff member to reset it for you. 

Here's the
[emergency procedure](faq#ive-accidentally-demoteddeactivated-the-only-admin-account)
for when no staff members can log in (try not to let this happen ;-) ).


## Edit a user

{: .navigation}
**Admin** → **Users** → _**Username**_ → **Edit**  
or  
**Admin** → **Users** → (individual user) **Edit**

If you click on the username in the _Users_ list, you can inspect all the
settings for that user, including their task texts and buggy data. From there
you can choose to **Edit** or **Change password**.

You can change the staff status of any user when you edit them.

Be careful not to revoke administrator status from _all_ the staff users. If
you do, you'll need to create a new administrator by overriding config settings
using environment variables.


## Enabling or disabling logins

{: .note}
**Administrators**' logins are never disabled: this setting is ignored for
admin accounts. Similarly, an _inactive_ user can never log in, regardless of
whether their login is enabled or not.

{: .navigation}
**Admin** → **Users** → **Enable/disable logins**

You can disable (or enable) logins in bulk: choose students, Teaching
Assistants, or all users. Disabling a login simply prevents access to the
logged-in pages of the server, until you enable it again. This might be useful
if you want to disable logins for all students before or after the end of term,
for example.

If you want to disable logins for all but a handful of students (perhaps they
have extensions on their deadlines), first disable _all_ student logins using
this bulk setting, and then edit the exceptions individually to enable them.

{: .navigation}
**Admin** → **Users** → _**Username**_ → **Edit**

Enabling or disabling a user's login is one of the settings available when you
[edit a user](#edit-a-user).


## Deleting a user's GitHub details

If a user has a GitHub username (or an access token, which is issued to the
server if it's granted access via the app), you can use the **Delete GitHub
details** button on their edit page.

This might be useful if they've accidentally linked to the "wrong" GitHub
account (this sometimes happens if students have more than one GitHub account).
The server doesn't let you edit these, because they are only set as a consequence
of the OAuth app allocating them. Similarly, users cannot delete (or change)
their own GitHub details.

Deleting GitHub details simply removes the data from the database. It will not
make any changes on GitHub, so if the user has cloned the editor repo, that
will still be there. The race server will no longer offer the user a link to it,
of course, because that requires the GitHub username, which you've just deleted.


## Deleting a user

You can delete a user record. Go to edit them, and click on **Show delete
form**. The delete form requires confirmation and the authorisation code.

When you delete a user, their buggy and task texts (if any) will also be
deleted. You can't get them back; there is no undo. For this reason, consider
marking them as _inactive_ (set **Is active?** to `No`), which effectively
suspends them without destroying any data. A user who has been marked as not
active cannot log in.

## Bulk deleting users

{: .navigation}
**Admin** → **Users** → **Bulk delete users**

It is possible to delete user records in bulk: you can choose to delete all
students, all Teaching Assistants, or all non-administrator staff. We
anticipate this mostly being useful at start-up if you've made a mistake when
[uploading students](../registering-users/spreadsheet), so (if you have the
default settings) it is hidden from the interface once the students records are
no longer "fresh". Specifically, if the most recently created student user was
added to the database more than `USER_BULK_DELETE_TIMEOUT_DAYS` days ago (or if
there are no student records), the bulk delete option is disabled and hidden
from the interface. If you need to get it back, edit the config setting in the
**Users** group (or set it to `0` to keep bulk delete always available).

Deleting users in this way also deletes their buggies and task texts. The
bulk delete feature will not delete users who are administrators.

## Downloading user data

{: .navigation}
**Admin** → **Users** → **Download students CSV**

You can download a comma-separated values (CSV) file containing the current
user data.

