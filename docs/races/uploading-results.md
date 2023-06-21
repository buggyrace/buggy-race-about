---
title: Uploading race results
nav_order: 60
layout: home
parent: Running races
has_children: false
---

# Uploading race results

When you've run a race, the output of the process is a new race file. This
file is the same as before the race, except it now contains the results, and
an event-by-event log (that the race player can animate).

## Uploading the results (and disqualifications)

{: .navigation}
**Admin** → **Races** → Race: **Upload results**  
or  
**Admin** → **Races** → Race: **Details** →  **Upload results**

When you upload the results file, the server will check the contents of that
file against the details (including students) in the database. If there are
any discrepancies, you'll see warnings. If there are any warnings, then no
changes will be made on the server unless you choose **Ignore warnings**.

{: .warning}
When you first upload the results, do _not_ check **Ignore warnings** — it's
important you see what they are before you proceed. If it was a busy race, there
may be several things reported. Read the warnings carefully before deciding
to proceed: if it's OK, upload the file again, this time explicitly ignoring
warnings.

## Results of a race

When you upload the results of a race (and agree to override any warnings, if
any), they are stored in the database of the race server. Specifically, results
are about what happened to each buggy that was entered in the race. That means:
every buggy that was on the race server when you [downloaded the race file](downloading).
There are three outcomes for each buggy:

* Buggy finished (so: has a position)
* Buggy did not finish (has no position)
* Buggy was disqualified from the race — in which case the rule violations are
  suggested

Although winning races is fun, disqualifications can be especially informative
— because they may be related to the quality of each student's buggy editor,
which may be checking for rules and calculating costs. The results page is
(deliberately) the only place when students see the definitive **cost** of
their buggy. They may have calculated this out from the specs, and indeed task
2-COST requires them to have automated this calculation. Similarly, this is
where students discover if they've missed — or failed to apply — rules too
(such as having fewer tyres than wheels).

> See [about races: What the races show](../races/about#what-the-races-show)
> for more about the underlying value of race results.

## Events in a race

The detailed events that occurred during the race may be included in the race
file you've uploaded (if you use the default Python script for running the
race, they will be). These can be used to show an animated replay of the race.
For more about this, see [replaying race](replaying).

## Visibility of results

The results you upload are only visible to students if you've set both
_Is visible?_ and  _Are results visible?_ to be `Yes` — see
[editing races](editing).

{: .warning}
Be sure to upload the race file that **contains the results** of the race —
it's possible to get this wrong, because the race file did exist before you ran
the race. Running the race creates a new copy of the race file. If you
accidentally upload the wrong one, you'll see a warning that the _file contains
no results_.


---

* Previous: [Running a race](running)
* Next: [Replaying races](replaying)



