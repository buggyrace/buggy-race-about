---
title: Design principles
layout: home
nav_order: 15
parent: About
---


# Design principles behind this project

We didn't take the decision to share our Foundation year Buggy Racing project
lightly. This page explains some of the thinking behind its design, and the
subsequent work that was required in making it available for other educators
to use.

## Predict–Run–Investigate–Modify–Make

**Students start with a basic, but non-trivial, working app**

We're explicitly using the [PRIMM approach](https://primmportal.com)
to teaching the (practical) skill of programming:

* Predict
* Run
* Investigate
* Modify
* Make

This is why students are presented with a working (but flawed) application.

In its initial state, the buggy editor app each student starts with works
properly. It runs even if the database is missing, but fails in different ways
— one page runs fine, another fails with a caught exception, and the other
(because the default is in debug mode) breaks with a stack trace. _Why is that?
How is that possible?_

## Tasks build on — and contravene — earlier tasks

**Structure of project is controlled by phases**

The tasks encourage building up from the basic start. We demand that the phases
are completed in order because later phases deliberately require refactoring of
work the student did in earlier phases. That's why we recommend getting to
phase 3 in the default project (especially 3-MULTI) — to be the _minimum_ level
of completion for even new students. That's when this aspect of the tasks'
design is most clearly encountered.

This is a fundamentally important way of understanding how programming works:
it's a design process, and the consequences of decisions made earlier (either
by other developers, or the programmer themself) will affect work later.

## Set non-patronising problems

**Tasks can be tackled with differing levels of complexity**

One of the risks in project work for new programmers is that the problems they
are invited to solve can be patronisingly simple, because the level of Python
they can apply may indeed be very basic. This can be most stark when working
with students who, although new to programming, may have experience in entirely
different, sophisticated fields.

Our buggy racing project tries to address this by, wherever possible, making
tasks open-ended: it's up to the student to decide how thoroughly a task should
be solved. A good example of this is how data validation of the buggy's flag
colours should be handled (if you're using the default project tasks, that
might come up in task 1-VALID or task 2-RULES, depending on the students).
What's the bottom limit on validating a CSS colour? That it won't "break" the
web page, or that it is in accord with the latest specification of the W3G CSS
Working Group? What are the technical implications of how the student decides
to solve this? How do they justify their decision?

Although buggy racing itself is, like _Mad Max: Fury Road_, fundamentally silly,
it's clear that the operation on data is universal, and the challenges are not
patronising in the way exercises like _"sort this list of sales figures"_ can
be. For example, at the start of the project, students upload the output of
their application (which is a JSON description of their racing buggy) to the
server by copy-and-pasting it. Later, in task 4-API they are invited to use the
race server's API. That features use of an API key and (if they want) one-time
secrets, which explicitly emulates how services like payment gateways operate.

The buggy racing specfication is deliberately large, and the rules embedded in
it are not all tabulated or enumerated. At some point every student needs to
find where the boundary between specification and implementation lies in the
software they write. When is data encapsulated in code? When is it explicitly
separate?


## Students work with existing code

**Developing an existing codebase is both common and informative**

Contrary to much academic project work, the reality of vocational programming
is that most developers do _not_ work on new codebases. Being a programmer
usually involves debugging and developing existing programs. (Sometimes that
code is _terrible_, and there are good pragmatic reasons why that is not going
to change). Understanding the structure of someone else's program is a very
different skill from just knowing the capabilities of a programming language,
and — crucially — it one of the best ways to begin to understand why writing
_good_ code matters, and what that even means.


## It's OK to expose students to things they don't know

**If it's working, and in context, they can and will figure it out**

There's SQL in the buggy racing project, even though we didn't teach it
explicitly when we ran this project. That's because — provided students are
not intimidated by it — it _is_ possible to make educated guesses of what it's
doing by reading it. That's one of the benefits of the PRIMM approach — the code
that students do not understand is _working_ so they can reason about what it
does before they need knowledge of the internals of _how_ it's doing it.

There are some idiosyncracies of SQL that can make it tough for new learners,
so when we ran this project ourselves we made it clear that we'd answer and
help with any questions on SQL — even fixing code — because _that_ isn't what
the project was about. In the vast majority of cases, student's didn't block
on SQL (sometimes to their own surprise!) because _pattern matching_ turns out
to be a very useful and universal skill that can get you a long way in a
language you haven't learned. (For a course on databases, this is not the
right way to teach SQL; for a Python project, we proved to our satisfaction it
can be).

## Encourage adoption by other educators

**It's not enough to just open source the project: make it helpful**

We've put a lot of effort into making the buggy racing server very
customisable, and — as you can tell, because you're reading this site —
thoroughly documented. This includes tryinmg to maintain good UI principles
and doing user-testing.

The decision to teach using someone else's project rather than roll your own is
not an easy one, especially for a busy educator who hasn't got endless spare
time to investigate it. We've taken the responsibility to make your experience
of the race server — the admin interface — and its supporting documentation as
easy and reassuring as possible. That is, merely putting content out ("it's
Open Source! Here's the GitHub repo!") is never enough. This policy is far from
universal in a lot of free education software — and for good reason, it takes
time and resources to do this properly.


## Apply some visual design

**We anticipate that students may be working on other modules too**

If you're familiar with Bootstrap you'll probably recognise the buggy racing
server is using that unexciting but ultimately safe basis for its design. But
it's helpful to students — especially those for whom this might be one of
several different modules they are doing as part of their course — for material
to be distinct, even if it's on a subconscious level.

Online learning environments favoured by academic institutions have a tendency
to make all the modules look _identical_. (Our own experience is of Moodle
running with a proscribed theme.) Of course, there is value in consistency —
including visual consistency — but it can be unhelpful and, at worst, confusing
when all material presented looks the same.

We wanted to be sure our students knew when they were engaging with the racing
buggy material. We've used the danger-stripe motif throughout, and made each of
the task/project/tech-notes sections within the server visually different.


## Be fun

**Wait... "buggy" has a double meaning? :-O**

We've tried to do all this and make the application basically fun too.
Who doesn't love a hamster?
