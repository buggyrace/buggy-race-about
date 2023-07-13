---
title: Introduction
layout: home
nav_order: 1
---

# Buggy Racing: a Python programming project for teachers and tutors


**Got students learning Python?**  
_Buggy Racing_ consists of the software (the "race server") and supporting
material (the "tech notes") for running a practical Python programming
project.


{: .demo}
See the demo race server at [demo.buggyrace.net]({{site.content.demo_url}}).

{: .rhul  }
_Buggy Racing_ was originally created in 2020 as the final term project of the
CompSci Foundation programme at Royal Holloway, University of London. We ran it
as a 6-week course of weekly lab sessions with students after at least one full
term of introductory Python.  
<br>
Since then we've made it very configurable so you can run it in a way that works
for your institution or course — university department, FE College, or local
code club. Available **for free** under the GNU GPL license.

{: .todo}
Some pages are not quite ready: the documentation is still being written! (July 2023).

## Features

* Customisable for your institution including links to
  supporting sites e.g., Moodle
* Fully customisable tasks (although the defaults are tried and
  tested!)
* Configurable for your teaching environment, including student
  data
* Can run with or without student GitHub accounts:
    * without: students unzip the source code and get to work
    * with: server can fork the repo into students' accounts and optionally
      inject tasks as issues
* Development can happen on students' own machines, college machines, or online
  services like [PythonAnywhere](https://www.pythonanywhere.com) or
  [Replit](https://repl.it)
* Students can store notes (task texts) as they go, working towards producing a
  project report (or not: you configure how the project is run)
* "Tech notes" supporting material (can be replaced with your own)


## Requirements

See the [full requirements](overview/requirements). You need to
[host your own race server](hosting).

## Components

* "Race server" for students to upload their buggies
  for the races
* "Buggy editor" basic app that each student starts with
* Structured activity of tasks arranged in phases (getting progressively more
  complex) — you can edit them or write your own
* Explanatory pages ("tech notes") on topics and tasks within the project
* Admin backend for managing the project


## Not included

{: .warning}
Submission and assessment of projects is **not included** (because how you do
that depends enormously on your institution and the course of study it's part
of, if any)... although [we have guidance](teaching) on how to handle that too.


