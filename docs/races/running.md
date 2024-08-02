---
title: Running races
nav_order: 50
layout: home
parent: Racing
has_children: true

---

# Running races

> Races are run offline — **they do not happen on the server**. You need to
> [download the race file](downloading), determine the outcome of the race, and
> then upload the results.

To run a race, run this script (for [set-up and requirements](#set-up-and-requirements),
see below):

    python3 utils/run-buggy-race.py

That will prompt for input, including the path for the
[race file you downloaded](downloading). The result of running the race is an
updated copy of the race file — this has the same contents as your downloaded
(input) race file, except now it contains _results_ and _events_ too.

{: .note}
By default the script looks for an input file called `race.json` in the current
working directory... so either drop your downloaded race file there and/or
copy/rename it to `race.json`. The script doesn't change the input file; it
creates a new (output) one.

When the script has completed, [upload the race file](uploading-results) — it
contains the results of the race as well as details of each event within it.


## Set-up and requirements

**You do not need to be running a database, or the server**. You're just running
a utility script which uses the downloaded race file (JSON) as input. That JSON
contains all the race and buggy data for this race. 

This simplest (if not the most efficient) way to get the script is to download
the whole server repo from
[`github.com/buggyrace/buggy-race-server`](https://github.com/buggyrace/buggy-race-server)
(either download the zip file from there via the green **Code** button, or use
`git clone`). Remember you don't need to run the race server, you just need the
script and the one custom library file it imports.

The script imports more Python modules but they are all from the Python standard
library, so you shouldn't need to use `pip` to install anything.

If you haven't downloaded the whole race server repo, or you're not in its
root directory when you run the `run-buggy-race.py` script, Python won't
be able to find the `race_specs` module. Make sure you're running Python from
the root of the repo you downloaded.

### Minimal version

Alternatively, if you do not want to download the whole race server repo, you
can just download the two files you need directly. There are "download" buttons
on each of these GitHub pages:

* [run-buggy-race.py](https://github.com/buggyrace/buggy-race-server/blob/main/utils/run-buggy-race.py)
* [race_specs.py](https://github.com/buggyrace/buggy-race-server/blob/main/buggy_race_server/lib/race_specs.py)

You'll need to edit the `run-buggy-race.py` script so it looks in the right
place for the `race_specs` one. The simplest way to do this is to put both files
in the same directory — any directory — and edit `run-buggy-race.py` so the
`import` statement changes from

```python
from buggy_race_server.lib.race_specs import BuggySpecs
```

to 

```python
from race_specs import BuggySpecs
```

Then, put your input race file (JSON) in the same directory, and run the script
from there:

    python3 run-buggy-race.py



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

It's even feasible for a creative classroom activity to run each race as a
table-top simulation, that is, not digitally — provided the results file is
constructed and uploaded accordingly.

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
