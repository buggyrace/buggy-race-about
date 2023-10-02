---
title: Build a custom runner
nav_order: 50
layout: home
parent: Running races
grand_parent: Racing
has_children: false

---

# Building your own race-runner

The process of [running a race](../running) is (deliberately) separate from the
race server (although there's a race-running in the code). This page describes
how to go about creating your own. It doesn't have to be in Python!

{: .note}
_"Runner" versus "player"_:  
Remember the **race runner** is the software you use to determine the outcome
of a race ("running" it). This is different from the **race player** which is
application that [replays the events of a race](../replaying) that were produced
by the race runner.

{: .todo}
This page is incomplete, and is currently being written! (2-Oct-2023)

## Summary: inputs/process/output

### Inputs

There are effectively two sources of data for the race:

* **global race/game specifications**  
  You can see these in the form of the
  [specs on the demo site]({{ site.content.demo_url }}/specs) — note how
  they are available in JSON format so your race-runner can 

* **specific details of this race and the buggy entrants**  
  This is the _race file_ (JSON format) you download from the race server

### Process

The race runner takes the inputs and calculates the events that take place in
the race, ultimately yielding its results. These include scrutineering the
buggies that have been entered into the race and disqualifying those who do
violate any race rules.

### Outputs

The race runner produces an updated version of the race file — which now
includes the results (for example, the position of each buggy) and the events
that occurred.

## Implementation details

