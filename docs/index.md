---
title: Overview
layout: home
nav_order: 10
---

# Buggy Racing: Python programming project


The _Buggy Racing_ project consists of the software (the **race server**) and
supporting material (the **tech notes**) for running a practical Python
project... for students who are learning Python.

You need to host the race server — either on your institution's own
infrastructure, or in the cloud. See [Hosting & installation](hosting) for
details and guidance.


{: .highlight }
This project was designed to run in the final term of the CompSci Foundation
course at Royal Holloway, University of London.



## Features

* Customisable for your institution including links to
  supporting sites e.g., Moodle
* Fully customisable tasks (although the defaults are tried and
  tested!)
* Configurable for your teaching environment, including student
  data
* Can run with or without student GitHub accounts:
    * without: students unzip the source code and get to work
    * with: server can fork the repo into students' accounts and optionally inject tasks as issues
* Development can happen on students' own machines, college
  machines, or online services like
  [pythonanywhere](https://www.pythonanywhere.com) or
  [repl.lit](https://repl.it)
* Students can store notes (task texts) as they go
* "Tech notes" supporting material (can be replaced with your own)

## Not included

* Submission and assessment of projects (because how you do that
  depends enormously on your institution and the course of study
  it's part of, if any)... although [we have guidance](teaching)
  on how to handle that too.


## Requirements

* The racing server must be accessbile over HTTPS
    * host it yourself (e.g., on your college's server)
    * or in the cloud (e.g., on Heroku)

* Tech stack:
    - race server is itself a Python Flask application (but also
      uses webpack, i.e., node)
    - ...that needs to connect to a database (e.g.,
      Postgres or MySQL (but Microsoft SQL Server should also work)
    - it's wrapped up in a Docker container to ease deployment
    - for full GitHub integration (automatically forking the
      editor code into students' own repos) you need an Oauth
      app running on GitHub

Students need access to the race server, but because the buggy editor
they are developing is a standalone web app, they can work offline
on their own machines (or college machines).

Once you've sorted out hosting, we might be able to help with the
DNS: if you're a college or school, ask us to add you as a
[subdomain on `buggyrace-net`](hosting/buggyrace-net)
(this might make SSL easier too)


## Components:

* "Race server" for students to upload their buggies
  for the races
* Structured activity of tasks arranged in phases (getting
  progressively more complex)
* Support of
* Explanatory pages ("tech notes") on topics and tasks in the project




* Who is it for?

We taught this with a cohort of students, some of whom had only done one
term Python programming before diving into buggy racing, and others who were
confident programmers with A-level (high school) experience.

The Buggy Racing project was designed specifically with university
Foundation students in mind: there's potentially a wide range of experience
with such a group. Building the buggy editor is a realistic and rewarding
mission for new students, but a challenging undertaking for more experienced
programmers who push through to the later tasks.

The phase/task philosophy: each student

  * must complete the phases in order (they are designed to build on each
    other)
  * but chooses how _thoroughly_ to implement each task

