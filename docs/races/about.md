---
title: About races
nav_order: 10
layout: home
parent: Racing
has_children: false
---

# About races

{: .navigation}
Top menu bar: **Races**

Although this is the _Buggy Racing_ project, really the students' focus is on
their buggy editors — the web app each student develops in order to create
and customise the specification for a racing buggy.

It _is_ feasible to run this project without running any races, although that's
not ideal.

{: .rhul}
In fact, for the first few years we ran this project without running _any_
races. This wasn't entirely planned — it was a consequence of Covid and other
work priorities — but it accidentally confirmed that the project can be run,
and be the context for students' work, even without the races. However,
obviously everything makes more sense if there are also races being run.

{: .screenshot}
![Screenshot showing a replay of a race](/docs/img/screenshots/race-replay.jpg)

{: .caption}
The race player replaying a race.

## What the races show

It's important to remember that the objective of the project is not to _win_
races. Although that's a laudible goal, the focus from a software development
point of view is to provide a context, and an incentive, for the improving the
buggy editor. After all, the students _start_ with a working editor: the
incentive for the project should be to make it better.

For this reason we discourage you running races _too_ close to the start of
the project. Be careful not to accidentally discourage students who don't get
up to speed quickly enough.

It's a deliberate feature of the design of the project that the software that
determines the outcome of races can (and does) run separately from the race
server. That is, we encourage you to customise or write your own. We think there
is case for making the outcomes of the races clearly random enough that winning
is more a cause of delight than an testiment of engineering brilliance. In
that respect, we ran our races more like a card game than a physics simulation.

### Total cost and race rule violations

The results of the race are the first time a student sees confirmation of the
race server's calculation of their buggy's cost, and — if their buggy did not
qualify for the race — the rule violations that disqualified them.

We don't publish this information before the race has been run, because it
encourages the students to trust their own programs. In fact, the race server
calculates the total cost of every buggy whenever it is stored in the database.
But we don't show this information except when it is listing in race results.

The race rules (and, specifically, the violations that are used to justify why
a buggy has been disqualified from a race) are not listed explicitly — that is,
they are not tabulated. Instead they are embedded in the specs page which
students can and should interpret for themselves.


---

* Next: [Creating a race](creating)
