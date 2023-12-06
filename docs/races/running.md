---
title: Running races
nav_order: 50
layout: home
parent: Racing
has_children: true

---

# Running races

To run a race, run

    python3 utils/run-buggy-race.py

That will prompt for input, including the path for the
[race file you downloaded](downloading). The result of running the race is an
updated copy of the race file — this one is the same as your download, except
it now contains _results_ and _events_.

Once you've got the results in a race file, [upload the file](uploading-results).

---

## Why races are run offline

The Buggy Racing project is _really_ about the students developing their
[buggy editors](../buggy-editor). As such, the race server is really to help
you manage and run that project. The races themselves are the context but it's
not where the focus is.

With this is mind, the details of how races are implemented has always been
separate from how the students' project is run. So although currently the races
are run by a Python script, we anticipated races could be implemented in a
variety of ways. You can customise or rewrite the Python script, or develop
an entirely different race, using the buggy specs and race file as the input.

* about [building your own race-runner](custom-runner/)

{: .suggest}
The buggy race, with its detailed input and output specifications, coupled with
a customised player, could be an excellent games-dev project for final year
students.

So the download → process → upload mechanism of race files is a very general
way of leaving this open. For this reason, the race player (that animates the
events from the race) is also entirely standalone, although the default one is
included on the race server.

It's even feasible for a creative class to run each race as table-top
simulation, that is, not digitally — provided the results file is constructed
and uploaded.

For more about the context of races as an incentive for students — specifically
_qualification for races_ — see
[about races: What the races show](../races/about#what-the-races-show).


## Made a race-runner? Let us know!

If you implement a buggy-racing mechanism please consider sharing it with us
so other people can choose how to run the races when they run a Buggy Racing
project.



---

* Previous: [Downloading](downloading)
* Next: [Uploading race results](uploading-results)
