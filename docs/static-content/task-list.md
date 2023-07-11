---
title: The task list
layout: home
nav_order: 10
parent: Static content
---


# The task list

{: .note}
This page is about the task list (the single HTML page on the race server)
— for information about how to specify the tasks themselves, including
editing them, see [creating the tasks](../customising/creating-tasks).

{: .demo}
See the [default task list]({{site.content.demo_url}}/project/tasks).

The task list is the page on the race server that defines the **tasks** which
your students need to attempt. Tasks are grouped into **phases** which must
be tackled in order: don't allow your students to start a phase until they've
completed all the task in the previous phases. However, with the pragmatic
exception of phase 0, students can do the tasks _within_ each phase in any
order they want.

{: .screenshot}
![Screenshot of example task list page](/docs/img/screenshots/example-task.png)

{: .caption}
An example task on the task list. This is 1-ADD: on your server at
`/projects/tasks/1-add` (or `/projects/tasks/#task-1-add`). The **Add text**
button lets the user (if logged in) add a text for this task that will
contribute to their report.

For some thoughts on using the tasks to teach, see
[teaching with the tasks and phases](../teaching/tasks-and-phases).



{: .screenshot}
![Screenshot of example task list page](/docs/img/screenshots/task-list.png)

{: .caption}
The top of the task list page (on your race server at `/projects/tasks`).

## Individual tasks on the list

The task list contains all the tasks for the students to attempt.

Every task has:

* a name/id (the phase it's in, and a mnemonic)
* a title
* statement of the problem it is addressing
* description of the solution (informally, this is similar to acceptance
  criteria for determining if it has been done)
* hints which give additional suggestions or things to think about when solving
  it

### URLs of individual tasks

The "true" URL of an individual task uses the anchor tag to locate it within
the (single) task-list page. For example:

    /projects/tasks/#task-1-add

By default, the server will generate URLs in the form:

    /projects/tasks/1-add

and automatically redirect to the form with the anchor tag. Task redirection is
also case insensitive. If you don't want this behaviour, you can disable it by
switching the config setting `IS_TASK_URL_WITH_ANCHOR` to `Yes`, which always
uses the URL without requiring redirection.

{: .navigation}
**Admin** → **Config** → Config:**Tasks**

See more about the [task config settings](../customising/tasks).

