---
title: Recovering texts
layout: home
nav_order: 70
parent: Day-to-day running
---

# Recovering task texts

This page describes a mechanism for loading an individual student's task texts
from a [database backup](database-backup). This is not a regular activity — in
fact, we hope you never need to do it! — but it's provided just in case you
need to recover texts that a student has accidentally deleted. This presupposes
that you _do_ have a backup, and that the backup contains the texts that the
student wants to recover.

{: .warning}
Extracting texts from a database backup is a non-trivial operation: you'll need
to spin up a standalone race server (presumably locally) and populate it with
your database backup. If this is challenging for you, ask us for help!

{: .note}
Remember that task texts can be disabled _entirely_ by setting
`IS_STORING_STUDENT_TASK_TEXTS` to `No`: see the
['Tasks' config settings](customising/tasks).

## The special case of student texts

If you require your students to produce a [report](../teaching/the-report), you
may have encouraged them to save their [task texts](../glossary#task-text).
Because they are free to edit their texts at any time during the course of the
project, students can also (presumably accidentally) destructively edit them
(or even delete them). This can seem catastrophic to a distressed student,
but... if you have been retaining [database backups](database-backup) it is
technically feasible to recover them.

For this reason the race server has a mechanism for extracting an individual
student's task texts as a JSON file which can subsequently be used to replace
existing texts.

This is a somewhat cumbersome process (described below), but it's probably
easier (and less prone to error) than manipulating your SQL backups manually,
which is the other way to do it.

Remember that the nature of rolling back to a previous backup is that you are
inevitably going to lose any edits that were made since the "snapshot" of that
backup. This isn't a selective form of version control: it's a way of replacing
_all_ of a student's existing task texts with the texts that they had saved
when the backup was taken. Presumably the subsequent edits were destructive
which is why rolling back to the earlier backup is helpful.

## You need a local copy of a race server

The bad news is that you need to install a local copy of the race server and
populate it with your backup. It only needs to be local — this is just so you
can navigate to the student through the interface in your browser and extract
the JSON file — so it might even be possible to use a quick-and-dirty SQLite
database (which is the default if you don't specify a `DATABASE_URL`).

{: .note}
You need to be able to log in as an administrator. As this is a local server,
if you can't log in with your normal staff credentials you can
[use the emergency procedure](../faq#ive-accidentally-demoteddeactivated-the-only-admin-account)
instead.

## Download the student's texts as JSON

On your local race server, populated from the database backup, go to the user
(the **Load texts as JSON** button is at the bottom of the page).

{: .navigation}
**Admin** → **Texts** (or **Users**) → User (by username) → **Load texts as JSON**

This takes you to the "Task texts... JSON" page where you can download the task
texts for this user in JSON format. Notice that this screen shows the _most
recent timestamp on a task text_. Check that this matches the date you expected:
if you've populated this local server with a backup, you should not see a
timestamp here that is more recent than that backup. (Task texts are timestamped
with both created-at and modified-at times, and this is showing you the most
recent of all of those for the user whose texts you are recovering).

Click on the **Download User's texts as JSON** button.

You'll get a JSON file which contains the student's texts at the time you took
that backup. You have just extracted the texts (for this single user) in a
format which your live race server is able to consume.

## Choose student and upload texts

Now go to the live race server, and navigate via the same route:

{: .navigation}
**Admin** → **Texts** (or **Users**) → User (by username) → **Load texts as JSON**

You need to upload the JSON file you've just saved.

{: .screenshot}
![Screenshot of text recovery](/docs/img/screenshots/student-text-recovery.png)

{: .caption}
The same page is used to download the JSON file (on a local copy of a race
server loaded with _old_ data), or to upload texts extracted in such a way.

{: .warning}
This will **delete any and all existing texts** for the student you've selected!  
Be very careful, and check everything! You are destroying the student's existing
texts, and replacing them with the texts in the JSON file.

The first time you upload the JSON set **Ignore warnings** to `No` (this is
the default). This ensures that if there is anything non-straightforward, the
operation will be aborted.

If you upload the JSON texts and either there are no warnings or you have chosen
to ignore them, the _existing texts_ for the user you selected will be deleted,
and replaced with the texts from the JSON file.

### What kind of thing can go wrong?

Some predictable — but unlikely! — problems arise if any of the _tasks_ have
changed name (or phase) since the backup was taken, or if the username has been
changed. Unless you've opted to ignore warnings, any such anomalies will
prevent any changes being made.

This mechanism deliberately does _not_ use the underlying `id` values for the
records it's recovering: it matches each text to user and task using their
_names_.

* **username doesn't match**  
  If there is a mismatch with the username, and you choose to ignore the
  warning, then the upload will replace the texts for the user you've selected
  on the race server: the username inside the JSON file is ignored.

* **task name (or phase) doesn't match**  
  If there is a mismatch with any of the task names, the texts will *not* be
  included. You can fix this by manually editing the JSON (to have the correct
  task phases and names) and trying again.

Normally, usernames and tasks don't change during the lifetime of a project,
so you will probably never encounter these problems.

