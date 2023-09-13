---
title: Build a custom player
nav_order: 50
layout: home
parent: Replaying races
grand_parent: Racing
has_children: false

---

# Building your own race-player

The process of [(re-)playing a race](../replaying) is (deliberately) separate
from the race server (although there's a built-in race player, you can use your
own if your prefer). This page describes how to go about creating your own. It
probably should run in a browser (e.g., a JavaScript or WASM application).

{: .note}
_"Player" versus "runner"_:  
Remember the **race player** is the software you use to replay a race-file that
has events and results that were generated by a [race runner](../running),
which is a standalone application that calculates the outcome (events and
results) of a race.

{: .todo}
This page is incomplete, and is currently being written! (1-Sep-2023)

## Summary: inputs/process/output

### Inputs

There are effectively three inputs for the race player:

* **race file**  
  The race file should contain the _results_ (per buggy) and the _events_ of
  the race (you can assume that the events describe a race that yields the
  results that are described within it). The race player is primarily concerned
  with displaying those events (presumably as an animation of the race
  as it progresses).
  
* **racetrack background image URL**  
  This is a cosmetic depiction of the racetrack as a 2:1 (landscape) aspect
  ratio image (typically JPEG).
  
* **racetrack path SVG path URL**  
  This describes the racetrack as an SVG path. If overlayed on the background
  image, the path describes the route followed by buggies driving along the
  racetrack. _Racetrack paths must always be loops._

  
### Process

The race player should display the progress of a race — the built-in one uses
animation applied to SVG elements to do this, and supports pausing, tracking
(highlighting) individual buggies, speeding up (in case the race gets slow due
to everyone running on punctured tyres, and so on).


### Output

The race player doesn't provide any output — only the display. The results don't
need to be displayed either, because those are already tabulated on the race
server.


