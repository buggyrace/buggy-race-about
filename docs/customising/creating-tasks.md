---
title: Creating the tasks
layout: home
nav_order: 100
parent: Customising
has_children: false
---

<details close markdown="block">
  <summary>
    Contents of this page:
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

# Creating the tasks

{: .navigation}
**Admin** → **Config** → **Tasks** → **Load or bulk-edit tasks**

When the set-up phase is complete — all the config settings have been defined
— you can create the tasks your students are going to attempt.

Each task includes hints and descriptions, so is quite verbose. The default
tasks are the ones that come built-in with the server, and you might not need
to change them. But if you want to, there are two ways to customise them. You
_can_ edit each one individually, up on the race server. Alternatively, you can
download the whole lot as a single markdown file, which you can then edit
conveniently offline and upload when you're done: see the instructions below.


{: .note}
If you use the _default tasks_ that come pre-built on the race server, the first
two tasks of phase 0 (getting and running the code) **will be customised** to
match your config settings (especially in the "GitHub" group, i.e,, 
[how the buggy editor code is distributed](../buggy-editor/distributing-the-code)).  
<br>
Specifically, tasks `0-GET` and `0-RUN` may differ based on which distribution
method you are using.

Creating the tasks is potentially destructive (it will delete any existing
tasks), so you need the [authorisation code](auth) to do it.

{: .warning}
Be careful! Although you can create the task list _at any time_, doing so will
delete any existing tasks and replace them with the new ones. You shouldn't do
this once the project has started!

## Accept the defaults

{: .screenshot}
![Screenshot of upload tasks dialogue](/docs/img/screenshots/upload-tasks-default.png)

{: .caption}
Loading the default tasks. The first two tasks of phase 0 (`0-GET` getting the
source code, and `0-RUN` running it) will be customised depending on how you've
decided to distribute the buggy editor source code to your students).

The simplest way to create the tasks is to accept the default tasks delivered
with the project. To do this, don't upload anything. Choose `Yes` to the
_Are you sure?_ prompt, select the distribution method that matches how your
students get the buggy editor source code, and press the red **Load tasks into
database** button.

This will populate the database with the default 27 tasks in 7 phases.

{: .warning}
Make sure the distribution method you choose matches the decisions you made
in your configuration settings! See more about
[how the buggy editor code is distributed](../buggy-editor/distributing-the-code),
which includes the _specific_ settings needed for each method.

If you want to edit the tasks offline (see the next section), but you're not
using the default distribution method, it's probably easiest to load the
defaults like this first, being careful to choose the appropriate distribution
method. This changes the first two tasks' texts to match your setup (this is a
default-within-a-default!). Now you can download the _current_ tasks as
markdown and that change will already be in there... and you can dive in and
edit them further.

## Or upload a customised markdown file

{: .screenshot}
![Screenshot of upload tasks dialogue](/docs/img/screenshots/upload-tasks-bulk-markdown.png)

{: .caption}
Instead of using the default tasks, or editing them in place, you can download
them all in one markdown file, edit it, and upload it back here — the race
server parses that file and inserts the individual tasks into the database.
Because tasks can be verbose, this may be much more convenient.

Before you can upload your own markdown file, you need to download one from
the race server as a basis to work from. There are two **Download** buttons on
the load task admin page (below the form).

* **Download the _default_ tasks as Markdown**  
  The downloaded file will contain the complete details of the default tasks
  — regardless of what's in the database. These will always be the unedited,
  default tasks.

* **Download the _current_ tasks as Markdown**  
  The downloaded file will contain the complete details of existing tasks in a
  markdown file that you can edit (and subsequently upload). This file contains
  edits (if any) that have been made since the tasks were added to the database.

Be careful to respect the organisation of the markdown file you downloaded,
because the server uses that structure when it parses what you send back up.
If you break it badly (or upload a file that isn't markdown) you'll probably
see a **Error parsing/adding tasks: No tasks found** error. The level of the
headings is significant: `#` for the name, `##` for the title, and `###` for
the `Problem`, `Solution` and `Hints` sections. If you deviate from this
structure, the file probably won't parse the way you expect.

## Then edit on the race server

Once you've loaded or uploaded them, you can edit the tasks on the race
server. In practice this allows you to make refinements and corrections to the
tasks that are now held in the database.

Remember that any changes you make here **will not be seen** by the students
until you publish (or re-publish) the task list.

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

Note that the load task admin page also allows you to download the _current_
tasks in this form, which might not be the same as the published issues (if you
have edited the tasks since you last published them).


---

 * Previous: [GitHub config](github)
