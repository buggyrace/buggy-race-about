---
title: Introduction
layout: home
nav_order: 1
---

# Buggy Racing: Python programming project


**Got students learning Python?**  
_Buggy Racing_ consists of the software (the "race server") and supporting
material (the "tech notes") for running a practical Python programming
project.

You need to host the race server — either on your institution's own
infrastructure, or in the cloud. See [Hosting & installation](hosting) for
details and guidance.


{: .rhul  }
_Buggy Racing_ was originally designed in 2020 as the final term project of the
CompSci Foundation programme at Royal Holloway, University of London. We ran it
as a 6-week course of weekly lab sessions with students after at least one full
term of introductory Python.  
<br>
We've subsequently made the resources you need to run this project yourself
available not just by releasing it under the MIT GPL Open Source license, but
also making it configurable so it can fit in with how you and the institution
you're running it for — university department, FE College, or local code club.


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
* Students can store notes (task texts) as they go, working towards producing a project report (or not: you configure how the project is run)
* "Tech notes" supporting material (can be replaced with your own)


## Not included

{: .warning}
Submission and assessment of projects is **not included** (because how you do
that depends enormously on your institution and the course of study it's part
of, if any)... although [we have guidance](teaching) on how to handle that too.


## Requirements

* The racing server must be accessbile over HTTPS:
    * host it yourself (e.g., on your college's server)
    * or in the cloud (e.g., on Heroku)

* Tech stack:
    - race server is itself a Python Flask application (but also
      uses webpack, i.e., node)
    - ...that needs to connect to a database such as
      Postgres or MySQL (but Microsoft SQL Server should also work)
    - it's wrapped up in a Docker container to ease deployment
    - for full GitHub integration (automatically forking the
      editor code into students' own repos) you need an Oauth
      app running on GitHub

Students need access to the race server, but because the buggy editor they are
developing is a standalone web app, they can do their development work offline
on their own machines (or college machines).

Once you've sorted out hosting, we might be able to help with the
DNS: if you're a college or school, ask us to add you as a
[subdomain on `buggyrace-net`](hosting/buggyrace-net)
(this might make SSL easier too).


## Components:

* "Race server" for students to upload their buggies
  for the races
* Structured activity of tasks arranged in phases (getting
  progressively more complex)
* Explanatory pages ("tech notes") on topics and tasks in the project




## Who is it for?

{: .rhul  }
We first ran this project with a cohort of around 100 Foundation students, some
of whom had only done one term Python programming before diving into buggy
racing, and others who were confident programmers with A-level (high school)
experience.

The Buggy Racing project was designed specifically with university
Foundation students in mind: there can be a very wide range of experience
within such a group. Building the buggy editor is a realistic and rewarding
mission for new students, but can also be a challenging undertaking for
experienced programmers who push through to the later tasks.

The phase/task philosophy is that each student:

  * must complete the phases in order (they are designed to build on each
    other)
  * but chooses how _thoroughly_ to implement each task — which should be
    appropriate for their ability


    

