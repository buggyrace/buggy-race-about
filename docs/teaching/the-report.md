---
title: Students' reports
layout: home
parent: Teaching
has_children: false
nav_order: 50
---

# Students' reports

{: .demo}
See the [report page]({{site.content.demo_url}}/project/report). This is
customised by the server's config settings.
The instructions describe to students how to add the report to their editor
app.

The config settings that control the report are in the "Project" group of
config settings: [configuring the project](../customising/project).

## The report is optional

If you don't require your students to submit a report at the end of the project,
set `PROJECT_REPORT_TYPE` to `none`.

## The report is a page on the buggy editor

Students already have to [submit their buggy editor app](submission) at the end
of the project — so the report needs to be presented as a page within the app.

Specifically, it's a route to `/report` in each student's own buggy editor app.

{: .note}
In fact — for historic reasons — originally this was `/poster` (which is still
a configurable alternative... but we think `/report` makes more sense). There
is still a promotional part of the report ("tell us why we should use your
editor") that has the feel of a poster to it. We might make that optional in
the future, but in the meantime it's an invitation for the students to think
about what they've done to make the features of their app attractive to users.


## Using task texts

If you enable task texts — and we recommend that you do, if you require a
report — then students can save notes on how they tackled each task _as they
do them_.

{: .screenshot}
![Screenshot of student task texts](/docs/img/screenshots/student-task-texts.png)

{: .caption}
The task text "matrix" shows students' notes, which is handy for keeping an eye
on progress: see [more about task texts](progress#task-texts-for-the-report).


The server provides buttons so a logged-in student can download their
accumulated task texts as a single file suitable for dropping into the
`report.html` template that they are presumably adding to their buggy editor.
This can also do markdown to HTML conversion.





