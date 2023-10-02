---
title: The JSON race-file
nav_order: 110
layout: home
parent: Racing
has_children: false

---

# Inside the JSON race-file

The race server produces a race-file when you [download a race](../downloading),
which you must do in order to [run the race](../running). It contains a
description of the race and each of the buggies that was entered into it.

{: .note}
You **do not need to know this** for normal operation of buggy-racing project!  
This information is for you (or your students) if you (or they) are
[customising the race-player](../custom-player) or
[customising the race-runner](../custom-runner).

When you [run the race](../running), the race-runner produces a new version of
that race-file that contains the detailed _events_ of the race. It also updates
the buggies so each now contains a `race-position` and (where appropriate) the
`violations-str`.

When you [replay a race](../replaying), the race-player reads the race-file
and animates the events described within it.

## Fields in the race file

| Field             | Value                                                    |
|-------------------+----------------------------------------------------------|
| `race_file_url`   | The URL (if known) of the source of this race file       |
| `title`           | Title of the race (shown wherever race is displayed)     |
| `description`     | Description of race (displayed to students)              |
| `cost_limit`      | Buggy cost threshold for entry in the race               |
| `max_laps`        | Number of laps for the complete race                     |
| `track_image_url` | URL of the background image (2:1 "landscape") for the racetrack |
| `track_svg_url`   | URL of the SVG containing `path` that is overlaid on the image |
| `league`          | Races can be grouped into leagues (not currently used)   |
| `version`         | String identifying the race-runner used to create this file |
| `start_at`        | Timestamp of the public start time of the race           |
| `raced_at`        | Timestamp when the race was actually run                 |
| `buggies_entered` | Quantity of buggies entered in the race (length of `buggies` array) |
| `buggies_started` | Quantity of buggies that were not disqualified from the race, i.e., starters (if the race has been run) |
| `buggies_finished`| Quantity of buggies that finished the race (if the race has been run) |
| `buggies`         | Array of buggy entries: [see below](#fields-in-the-buggies-entries) |
| `events`          | Array of "event second" entries: [see below](#fields-in-each-events-turn) |


### Fields in the `buggies` entries

The `buggies` field consists of an array with an object for each buggy. The
order of the buggies is not significant.

| Field           | Value                                                      |
|-----------------+------------------------------------------------------------|
| `username`      | Identifying string for the buggy: normally this is the user's username, but may be an anonymised unique string if [`IS_USERNAME_PUBLIC_IN_RESULTS`](../customising/races) was set to `No`|
| `user_id`       | Corresponding user ID on race server                       |
| `flag_color`    | Primary flag colour for this buggy (CSS colour)            |
| `flag_color_secondary` | Secondary flag colour (CSS colour)                  |
| `flag_pattern`  | Flag pattern (one of valid patterns — default `plain` see `flag_pattern` from the [specs on the demo site]({{ site.content.demo_url }}/specs))  |
| `cost`          | Total cost of the buggy (calculated when it was submitted) |
| `race_position` | If race has been run, the finishing position of this buggy: `-1` did not start, `0` did not finish, `+n` position |
| `violations_str`| If race has been run, comma-separated list of names of rule violations that disqualified this buggy from the race (so: `race_position` will be `-1`) |


The `user_id` is used by the race server to correctly record the results of
the race when it is uploaded after having been run. It's generally not used
by the race-player (in anticipation of replaying the race independently of
the race server).

The two result items are `race_position` and `violations_str` which can only be
populated once the race has been run — so they might be absent, or `null`. 

### Fields in each `events` turn

The `events` field is an array of arrays, each one comprised of the events that
happened in that second of the race (the first array, index `0`, being the first
second after the start. Effectively each second is a "turn" in the race.

| Field | Value                                                                |
|-------+----------------------------------------------------------------------|
| `b`   | Buggy name — this is a string match on the corresponding buggy name in the `buggies` array |
| `d`   | Delta: distance along track that this buggy moves this "turn"        |
| `e`   | Event type (if any): used by the race player to trigger custom behaviour (e.g., a fire attack might trigger an animation of a fireball) |
| `s`   | String describing the event                                          |

#### `b`: Buggy name

The buggy name is used to identify the buggy throughout the race — they are
guaranteed to be unique within the race. They are lower case (because that's
a requirement of the buggy owner's username on the race server where the
buggy originates).

#### `d`: Delta (distance moved along track)

The "delta" is added to the buggy's linear position along the track. Therefore a
missing delta, or a delta of `0`, result in no movement. In theory, a negative
detla would move a buggy in reverse.

#### `e`: Event type

An event does not need to have an event type. But if it doesn, the race player
can triggert appropriate behaviour. The default race runner currently generates
two possible events by way of an example:

| Event type       | Code | Detail                                               |
|----------------+------+------------------------------------------------------|
| `PUNCTURE`     | `p`  | A puncture causes a loss of tyre (automatically replaced with a spare tyre, if available) |
| `CHASSIS_FAIL` | `xc` | End of race: chais breaks (typically because it wasn't strong enough for the mass of the buggy) |

The race player can use these events to trigger animations or special messages
in thew race player. The race player should ignore event types it doesn't


## Example race file


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
