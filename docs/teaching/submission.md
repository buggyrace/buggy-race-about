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
really is. There might or might not be a [report](the-report) involved too —
perhaps as the `/report` route inside each student's buggy editor. If you're
using GitHub, you might not require explicit submissions from the students. Or
you might be snapshot-cloning them at the cutoff date. Or you might require
students to make a _release_.

In general, we anticipate the students' work — if it is submitted at all — to
take the form of the directory (or Git repo) they have been working in.


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




