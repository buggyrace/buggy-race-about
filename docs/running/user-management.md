---
title: User management
layout: home
nav_order: 28
parent: Day-to-day running
---


# User management

{: .navigation}
**Admin** → **Users**

The Users admin page lists all the users registered on the race server, 
showing data for each and providing links to investigate and edit each one.

Students are listed before staff.

You can choose which columns are displayed by clicking the white buttons at
the top of the table: they toggle the display of the respective column. The
show/hide choices are stored in your browser, so will be used whenever you
revisit this page.

{: .note}
In general, only administrators who know the authorisation code can change 
other users' data.  
An exception is that Teaching Assistants can be granted the ability to change
students' passwords.

### Active vs. inactive users

If you mark a user as _inactive_, they are effectively suspended: they won't
be able to log in, their existing login session will be terminated, and they
won't be included in any downloads.

### Types of user

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
  setting `IS_TA_PASSWORD_CHANGE_ENABLED` is `Yes`.

The username you nominated as the admin user during the setup-up phase is
automatically an administrator.

## Inspect a user

When you're looking at the list on the _Users_ page, you can click on **✱** to
view the for-staff-only _comment_. The JSON button (with a spanner icon)
displays the last-uploaded JSON.

You can click on the username to inspect the user's settings and task texts
in detail.

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


## Downloading user data

{: .navigation}
**Admin** → **Users** → **Download students CSV**

You can download a comma-separated values (CSV) file containing the current
user data.

