---
title: Tasks and phases
layout: home
parent: Teaching
has_children: false
nav_order: 12
---

<details close markdown="block">
  <summary>
    Contents of this page:
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

# Tasks and phases

{: .demo}
See the [default task list]({{site.content.demo_url}}/project/tasks).

The Buggy Racing project work that the students must undertake is broken up
into tasks, and the tasks are grouped into phases.

Tasks are grouped into phases which **must be tackled in order**: don’t allow
your students to start a phase until they’ve completed all the task in the
previous phases.

However, with the pragmatic exception of phase 0, students can do the tasks
_within each phase_ in any order they want.

Furthermore, students can **decide how thoroughly** to implement any tasks.

Finally, it's inevitable (and deliberate) that the open-ended nature of the
tasks, and their increasing complexity, means that **students are not expected
to complete all the tasks**.

{: .note}
You can set the config setting `PROJECT_PHASE_MIN_TARGET` to indicate which
**phase** you expect most of your students to reach. By default, this is set
to `3` but will vary depending on the nature of your students (are they
mostly beginners, or do they already have experience in web development?). If
you set it to `0` then no recommendation will be shown.


{: .rhul}
This fluid approach — letting students decide how thoroughly to address each
task — worked well with the range of students. Inevitably, some students do
the minimum. But most engaged students did a lot more. It's also common — and
a good indicator of a growing appreciation of what's involved in software
development — to see students revisit tasks to add more coverage to them once
they've worked out a way to implement a solution.

## The contents of a task

You can edit all or part of any task. Each task has the following components:

### Task name

Every task has a clear, short, mnemonic name so students can unambiguously
identity what they are working on and what they need to achieve. The number of
the phase to which it belongs is part of this name — for example,
[task 2-COST]({{site.content.demo_url}}/project/tasks/2-COST) is the task
that adds calculation of the total cost of the buggy, and there's a link (via
your race server) to its definitive description.

### Task problem statement

Each task is presented in terms of the problem that needs to be overcome.

### Task solution suggestion

The solution text describes what the student needs to do to address the problem.

### Task hints

There's always a section with related information and suggestions. It's very
common both in the project and web development in general that there's more than
one way to do something, so the hints can direct or suggest.


## The "Task" group of config settings

{: .navigation}
**Admin** → **Config** → Config:**Tasks**

There are a small number of config settings that relate to tasks. These include
the names for some specific tasks — for example the setting `TASK_NAME_FOR_API`
is the name for the task where students are first exposed to the
[race server API](../running/api). By default this is 4-API, but if you
rename the task (changing either its name or the phase in which it is found)
you'll need to update this setting. These settings are used in one or two places
in the race server interface or the tech notes.

## Customising tasks

The race server has a default set of 27 tasks arranged into six phases. You
can accept these, and — before the project starts — you can edit any of them
individually. This includes removing tasks completely, changing the wording
of any of their text, or even changing the name or phase to which they belong.

{: .warning}
As the tasks' names and phases are used as links, you should make any changes
you want _before_ you start the project — that is, before you share the
task list and its links with your students.

## Downloading and uploading all tasks in one go

Because the tasks are inherently verbose, if you want to edit them, you can
download a single markdown file that contains them all. You can then edit
this file — keeping the basic structure you'll see in the example you've
downloaded — and upload when you're happy with it. This _replaces all the
tasks on the server_ in one go, so may be a more convenient way for you to
customise your tasks if there's a lot you want to change.

{: .note}
Your server's config settings are available as string values that you can
drop into your task texts. If you add `%BUGGY_RACE_SERVER_URL%` to the markdown,
when you publish the task list, such tokens will be substituted with the value.
See the [config settings](../customising) (or the
[system info](../customising/env#other-system-settings-system-info)) for the
exact names you should use.  
<br>
These are _not_ Jinja templates, so you can't use conditionals or anything
especially fancy: just string replacement for named settings.

You can also download the tasks on your server as a single markdown file _at
any time_ — for example at the end of the project. This might be useful if you
want to preserve the tasks and load them into a new race server (for example,
if you tear this one down and subsequently want to run the project in the next
academic year).


## Tasks and the growing complexity of the buggy

We designed the tasks with consideration on _how_ they build on each other.

The [buggy editor](../buggy-editor) that the students start with is deliberately
basic: it lets the student change the _number of wheels_. And that's it.

But the database it includes _also_ has three columns for the racing pennant:
`flag_color`, `flag_pattern`, and `flag_color_secondary`. So if the student
wants to add another field beyond the number of wheels, then those three are
probably a good place to start. It quickly transpires that the `flag_pattern`
input is different from the other two because there are only a handful of
patterns (valid string values) that are meaningful for those, whereas the
colours are... potentially more complex.

A similar range of complexity within the project, with some nudges, is a 
pattern we've tried to apply throughout the tasks.
