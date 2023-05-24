---
title: Creating the tasks
layout: home
nav_order: 100
parent: Customising
has_children: false
---


# Creating the tasks

{: .navigation}
**Admin** → **Config** → **Tasks** → **Load new tasks into database**

When the set-up phase is complete — all the config settings have been defined
— you can create the tasks your students are going to attempt.

Each task includes hints and descriptions, so is quite verbose. That's why the
tasks are defined in a single "task list" markdown document, which you upload.
The race server parses this file and creates the individual tasks in the
database. The format of that document is straightforward — if you want to
create you own, you can edit the example that is already on the race server
(see below).

{: .screenshot}
![Screenshot of upload tasks dialogue](/docs/img/screenshots/upload-tasks.png)

{: .caption}
The upload tasks dialogue — if you don't provide a file to upload, the race
server will use the default tasks.

Creating the tasks is potentially destructive (it will delete any existing
tasks), so you need the [authorisation code](auth) to do it.

{: .warning}
Be careful! Although you can create the task list _at any time_, doing so will
delete any existing tasks and replace them with the new ones. You shouldn't do
this once the project has started!

## Accept the defaults

The simplest way to create the tasks is to accept the default tasks delivered
with the project. To do this, don't upload anything. Choose `Yes` to the
_Are you sure?_ prompt, and press the red upload button.

This will populate the database with the default 27 tasks in 7 phases.


## Or upload a customised markdown file

Before you can upload your own markdown file, you need to download one from
the race server as a basis to work from. There are two **Download** buttons on
the task admin page.

* **Download the _current_ tasks as Markdown**  
  The downloaded file will contain the complete details of existing tasks in a
  markdown file that you can edit (and subsequently upload). This file contains
  edits (if any) that have been made since the tasks were added to the database.

* **Download the _default_ tasks as Markdown**  
  The downloaded file will contain the complete details of the default tasks
  — regardless of what's in the database. These will always be the unedited,
  default tasks.

## Then edit on the race server

Once you've created them, you can edit the tasks on the race server. In practice
this allows you to make refinements and corrections to the tasks that are now
held in the database.

Remember that any changes you make here **will not be seen** until you publish
(or re-publish) the task list.

{: .warning}
Be careful about materially changing any tasks once the project has started:
**it is not recommended**.  
Changing the name or phase of a task, changes its URL too — so don't do this if
any students already have links (this may include in GitHub issues if you're
automatically injecting those into students' repos).

## Substituting config settings in the text

Inside the tasks' markdown texts, words like this: `%CONFIG_NAME%` (all-caps
between `%`, no spaces) will be replaced with the value of the config setting
with that (exact: type it carefully!) name. For example,
`%BUGGY_RACE_SERVER_URL%` will be replaced with the URL you have set in that
config setting.

You can check the config settings' names by looking on the race server where
you set them: **Admin**&nbsp;→&nbsp;**Config** lists them all.

This substitution of placeholders with values happens when the task list is
published (not when they are uploaded into the database). This means that if
you change config settings, you should re-publish the task list to reflect the
latest values.


## Issues CSV

{: .note}
The issues CSV described here is optional. The race server might use it, but
normally you won't need to — so skip this if you're not interested.

The most important effect of publishing the task list is that the current tasks,
_and_ the current values of any config settings they reference, are rendered
into HTML as the task list. Students work directly from this task list.

However, the publishing process _also_ generates an "issues CSV" which the
server will use if you've set the config setting
`IS_USING_GITHUB_API_TO_INJECT_ISSUES` to `Yes`. The issues CSV is effectively
a static file "frozen" to be in synch with the published task list. It is a
headerless CSV file with two columns:

* name and title
* problem description and link to the task on the race server (markdown)

The file is made publicly available on your race server at
`/project/tasks/issues.csv`, and there's a button on the admin tasks page so
you can download it in case this is useful to you.

Note that the task admin page also allows you to download the _current_ tasks
in this form, which might not be the same as the published issues (if you have
edited the tasks since you last published them).


---

 * Previous: [GitHub config](github)
