---
title: About the students
layout: home
parent: Teaching
has_children: false
nav_order: 10
---


# About the students

_Buggy Racing_ is a practical Python project for students who are familiar with
the basics of Python — but might not know (yet) how a webserver works, what
Flask is, or how a database fits in. We initially ran it with students who had
been taught Python for *one term* — see [Students](students) for more detail.

### What the students do

Your students start with a basic standalone Flask web application (the **buggy editor**) that lets them define a racing buggy. It outputs the description of the buggy in JSON format, which they upload to the race server to enter their buggy in the communal nightly races.

{: .warning }
Buggies that violate race rules (for example: must have an even number of wheels) are disqualified from that race.

That buggy editor is very limited: all it can do is _change the number of wheels_. As students work through the **phases** and **tasks** of the project,
their editors get more capable, and more complex.

{: .note }
Winning races is fun, but the race results are not a material part of
the project. The challenge is to produce increasingly complex behaviour
in the editor that builds the buggies — _entering races_ is the incentive.

### What they produce

This project is based on the PRIMM principle of starting with working code,
investigating how it works, and then developing it. By the end of the project —
we ran it over six weeks, with weekly lab sessions — students have developed a
Flask web application that (optionally — if you wanted it) include a "report"
describing how they tackled each task.

{: .note}
**Optionally** you can require students to use their own GitHub accounts
(the server will fork the buggy editor repo into their account and even
inject the tasks as issues).
