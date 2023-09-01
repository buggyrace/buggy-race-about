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
This page is incomplete, and is currently being written! (1-Sep-2023)

## Summary: inputs/process/output

### Inputs

There are effectively two sources of data for the race:

* **global race/game specifications**  
  You can see these in the form of the
  [specs on the demo site]({{ site.content.demo_url }}/specs" — note how
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

### The race file format

This is the JSON file the race runner should produce. It's the same as the race
file format that the race server produces when you download a race file,
except the race file your runner creates should add `race_position` and
`violations_str` to each buggy in the `buggies` collection, and `events` array
consisting of an array of events for each 1-second turn.

**Example race file format:**

```json
{
  "race_file_url": "",
  "title": "First race",
  "description": "Introductory one-lap race",
  "cost_limit": 200,
  "max_laps": 1,
  "track_image_url": "https://demo.buggyrace.net//races/assets/tracks/racetrack-01.jpg",
  "track_svg_url": "https://demo.buggyrace.net//races/assets/tracks/racetrack-01-path-460.svg",
  "league": "",
  "version": "1.0",
  "start_at": "2023-07-20 23:58",
  "raced_at": "2023-07-21 09:00",
  "buggies_entered": 15,
  "buggies_started": 12,
  "buggies_finished": 8,
  "buggies": [
    {
      "username": "foxglove",
      "user_id": 11,
      "flag_color": "yellow",
      "flag_color_secondary": "red",
      "flag_pattern": "dstripe",
      "cost": 96,
      "race_position": 11,
      "violations_str": ""
    },
    {
      "username": "johanna",
      "user_id": 16,
      "flag_color": "#640044",
      "flag_color_secondary": "black",
      "flag_pattern": "plain",
      "cost": 194,
      "race_position": -1,
      "violations_str": "RACE_COST_THRESHOLD,ENOUGH_TYRES"
    }
    ...
  ],
  "events": [
    [
      {"b": "auberon",  "d": 10.0},
      {"b": "ethel", "d": 5.0},
      {"b": "foxglove", "d": 27.0},
      ...
    ],
    [
      {"b": "gault", "d": 8.0}, 
      {"b": "matthew", "e": "p", "s": "puncture! now running on 3 of 4 wheels"},
      {"b": "mervyn", "d": 11.0},
      {"b": "foxglove", "s": "is out of power (and has no auxillary power)"},
      {"b": "gault", "d": 1.0},
      ...
    ],
    [
     {"b": "gault", "s": "crosses the finish line in 8th place (1 lap race)"}
    ]
  ]
}
```
