---
title: How students submit
layout: home
parent: Teaching
has_children: false
nav_order: 30
---



# How students submit

{: .note}
The race server doesn't manage or handle submission of the projects or
reports. See also: [assessment](assessment).

Although we anticipate that students will work through the tasks developing
their buggy editors, submitting the work is not handled by the race server.
Nonetheless the server will display both a deadline and a link if you provide
them.

The server can't really handle this for you because there is so much variation
— depending on the level of your students — as to how and what the submission
really is. There might or might not be a [report and/or poster](report-and-poster)
involved too — perhaps as the `/report` route inside each student's buggy editor,
or separate documents. If the students are using version control, you might not
require explicit submissions from the students. Or you might be
snapshot-cloning them at the cutoff date. Or you might require students to make
a _release_.

In general, we anticipate the students' work — if it is submitted at all — to
take the form of the directory (or Git repo) they have been working in, and
possibly additional documents.


## Set the submission deadline and link

{: .navigation}
**Admin** → **Config** → Config:**Project**

If you enter a submission deadline in the config setting
`PROJECT_SUBMISSION_DEADLINE`, it will be displayed on the race server
on the project page (`/project`).

You can also provide a URL to the submissions page in `PROJECT_SUBMISSION_LINK`.
If it exists, the race server will link to it.

If you want your students to create and submit a zip archive of their work,
the server has some settings for showing instructions regarding that too. See
the [config settings](../customising/project) in the "Project" group.

{: .rhul}
When we ran this project we required students to zip up their work and submit
it on the Moodle. This had the benefit of being the way most work in their
course in the department would be submitted, but also meant the staff could
benefit from the mechanism — including, crucially, the audit trails — for
acknowledging submission receipt.
<br>
So the submission deadline was displayed on the race server, and the submission
link was the URL of the Moodle page where the zip files could be uploaded.

## Customising deadlines and links for individual students

You can override the project submission deadline or submission link for
individual students. You might want to do this if any of your students have
different deadlines (for example, if you are handling extensions or resits).
This behaviour is not enabled by default: you need to set one or any of `IS_PROJECT_SUBMISSION_DEADLINE_PER_STUDENT`,
`IS_PROJECT_SUBMISSION_LINK_PER_STUDENT`, or `IS_PROJECT_NOTICE_PER_STUDENT`
to enable it.

Once you've done so, the appropriate fields are available when you edit the
user:

{: .navigation}
**Admin** → **Users** → (individual user) **Edit**

Values you enter here override the project-wide settings (if any). Conversely,
any you leave empty will inherit the values (if any) of the Project config 
settings `PROJECT_SUBMISSION_DEADLINE` and `PROJECT_SUBMISSION_LINK`.

You can also set a `PROJECT_NOTICE`, which is a text displayed on the `/project`
page that you can use to give additional information about the project. We
anticipate this being used mostly to display a custom (per-user) message to
students with an overridden deadline or link.

If you've enabled any of these `IS_PROJECT_*_PER_USER` settings, _none_ of them
will be displayed on the `/projects` page except when a user is logged in.
The dashboard shows a summary (count) of the numbers of such overridden values
(on active students) is provided on the dashboard. You can see which users have
overrides by looking at the Users page in the admin.


