---
title: Tracking progress
layout: home
parent: Teaching
has_children: false
nav_order: 15
---

# Tracking progress

{: .todo}
This isn't ready yet: the documentation is still being written.

## What activity we do keep an eye on

The admin dashboard summaries who's logged in (to the race server) today,
who's logged in during the last seven days, and who has never logged in.
This allows you to quickly see any students who are not joining in.

We don't keep an audit trail of the buggy uploads: the database contains the
last JSON that was uploaded (for each student), and the last buggy that was 
created as a result of such an upload. These don't always coincide: if a
student uploads bad JSON — that is, JSON that doesn't parse — it will be
saved as the upload, but the buggy won't be updated. 

The sophistication of the buggy can be an indicator of what their editor is
capable of doing. The _default_ buggy is fairly easy to spot. Early on in the
project you expect to see buggies whose only changing characteristic is the
number of wheels, because that's the only input that is provided in the initial
buggy editor app. Of course, the editor doesn't _need_ to be used to generate
the JSON — but that's part of the learning curve for the students.

Once you start running races and varying the cost threshold, a great indicator
to look out for is which students change their buggies' cost to be a point or
two below the maximum cost _for every race_. This generally is the result of
functioning 3-COST task: the student is using the editor they build to edit
their buggy to a numerical criteria.

If you've specified that students should be submitting a report, the
<strong>task texts</strong> give a helpful indication of progress. Students are
encouraged — mainly by the timely convenience of the tool — to take notes on
how they tackled each task _as they are doing them_. Towards the end of the
project, they can download these task texts in the specific format needed to
drop straight into their report.


{: .screenshot}
![Screenshot of student task texts](/docs/img/screenshots/student-task-texts.png)

{: .caption}
The task text "matrix" shows which tasks students have saved notes against —
these can be downloaded to form their reports towards the end of the project.
You can click on a cell to view the student's text for the given task.


Some students may prefer to take their notes offline, using other tools. That
of course is fine, provided that is what they are doing.

{: .note}
Because we are _not_ doing any assessment on the server, the task texts are
not a mechanism for _knowing_ the progress students are making... but they are
a useful indicator.


## What activity is _not_ visisble on the server

Remember that the students are _not_ doing their development on the server.
So there's no analysis or access here to the work they are doing: that is, 
the programming and problem-solving and debugging.

