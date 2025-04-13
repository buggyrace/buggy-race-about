---
title: The Python project
layout: home
nav_order: 20
parent: Overview
---

# The Python project (what students do)

Each student develops a small Python Flask webserver that stores the
specification of a racing buggy in a local database. They can edit the buggy
(for example, changing the number of wheels) and output the buggy specification
as JSON data. This app is the students'
**[buggy editor](../buggy-editor/the-editor)**.

> The students' buggies take part in races that you run on the **race server**:
> See more about [installing and hosting](../hosting) the server and the
> [day-to-day running](../running) of it.

{: .screenshot}
![Screenshot of buggy-race-editor](/docs/img/screenshots/buggy-editor.png)

Uploading that JSON data to the race server enters the buggy for the next
race.

The project consists of around 26 tasks arranged in 7 phases. Phases must
be completed in order, but students are free to implement tasks as thoroughly
as their level allows.

The complexity of the tasks generally increases as the student works through
the phases.

See more about the [tasks and phases](../teaching/tasks-and-phases). You can
customise any and all of them.

## Flask serving on localhost

The project uses Flask, a lightweight webserver, which students hit in their
browser using `localhost`.

The project can support students working on their own machines, college
machines, or in the cloud using services like PythonAnywhere or Replit.
See more about [where students can work](../buggy-editor/running-where).

---

* Previous: [Who is it for?](who-is-it-for)
* Next: [Requirements](requirements)
