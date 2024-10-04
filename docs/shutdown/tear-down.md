---
title: Tear-down checklist
layout: home
nav_order: 10
parent: Shutting down
has_children: false
---

# Tear-down checklist

Here are some things to consider before you shutdown your race server.


<details open markdown="block">
  <summary>
    Contents of this page:
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## Take a backup

If you [save a backup of the database](../running/database-backup), you can run
up a new instance of the race server in the future. Almost all the config
settings are preserved in that database backup, although for completeness you
might find it helpful to save a
[snapshot of the config settings](../customising/env#saving-a-config-snapshot-for-env)
as a text file too.

{: .warning}
If you've customised the [tech notes](../static-content/tech-notes) then
those changes will not be in the database. You've probably done that in your own
repo though, in which case _that_ is your backup. If you added new files (such
as images), check that you have included them.

If you have not been storing [race files](../glossary#race-file) on the server
(because config setting `IS_STORING_RACE_FILES_IN_DB` is not `Yes` — by default
it is) then you should probably save copies of those as well (from wherever they
are).

## Disable student logins

Disabling student logins prevents students making any changes on the server.
If you've been using the [task texts matrix](../teaching/progress) for example,
it's probably best to disable student logins to "freeze" this matrix once the
last submission deadline has passed.

{: .navigation}
**Admin** → **Users** → **Enable/Disable logins**

For "Which users?", choose "All students" and click **Disable logins**.

You can enable individual students' logins (for example, if they are submitting
late or are part of a resit group).
See [Enabling logins](../running/user-management#enabling-or-disabling-logins).


## Leaving the races online

After the project has ended, students may still want to see the races. So
although there will be no more uploading (that is, dynamic activity) on the
server, the race results and the race player are still there. This might be a
good enough reason to not shutdown the race server right away (but consider
disabling student logins, above).

If you want to preserve the races for posterity, it is possible to run a
standalone race-player on a different site. To do this you'll need the (JSON)
race file for each race, and the standalone race-player. See
[Publishing race files](../races/replaying) for more. You'll need to
[download the race files](../races/downloading#downloading-the-race-file)
before you shut down your race server.

The results tables that are shown on the race server are _not_ explicitly
presented in the race player, although they are implicitly shown when the
race is replayed.

## Consider running a static placeholder

If you've shared links to your race server elsewhere — for example, on your
institution's online learning system — simply switching the race server off can
be unhelpful. This really only matters if you intend to preserve the domain or
subdomain over time, and you want to indicate that the URL is correct (which is
good practice!). See [running a static placeholder](placeholder).

