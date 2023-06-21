---
title: Replaying races
nav_order: 70
layout: home
parent: Running races
has_children: false
---

# Replaying races

{: .navigation}
Top menu bar: **Races** → Race: **Replay**  
or  
**Admin** → **Races** → Race: **Replay** 


{: .note}
If _Are results visible?_ is `No` for this race, students won't be able to
replay the race (the button won't be there) — but staff can use the admin
**Races** page to access it instead.

The race player animates the events of the race.

Then race player is entirely standalone (it's implemented in JavaScript and
you can host your local version of it independently of the race server). It
works by reading a race file, and playing the race described within it.

This presupposes that the race file is available online — by default, if you've
uploaded it to the race server, it will be there, although you can override
this if you've set the config setting `IS_STORING_RACE_FILES_IN_DB` to `No`.

The race player reads the JSON file (from the URL you've nominated, which will
be on the race server by default, because it is saved when you upload it), and
animates the events and buggies described within it.

{: .suggest}
The race player, like the mechanism that [runs the races](running), is
potentially separate from the race server — so in future more sophisticated
versions may be used.


## The default player

The player that runs on the server will automatically "track" the current
user's buggy so students see their own buggy highlighted in the replay.
You can click on any buggy on the track — or in the log — to track that one
instead.

There's a **Fast** button in case the race is running too slowly (this can
happen if there are lots of punctures).

## Standalone player

As staff, you can test a race file _before_ you've uploaded it using the
"standalone" player — you need to have the race file on a URL it can access
though, and there may be CORS considerations (see below) too.


## Hosting elsewhere

If you don't use the default player, or you host the race files on another
server, be aware that there may be
[cross-origin resource sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
(CORS) restrictions on whether the player can access them. Specifically, CORS
may apply to the JSON race files and SVG path files.

JSON served from GitHub pages sites do set the `Access-Control-Allow-Origin`
header to `*` so can be used to host race files.

See [customising Races (config settings)](../customising/races) for more details,
including `BUGGY_RACE_PLAYER_URL` and `BUGGY_RACE_PLAYER_ANCHOR`.



---

* Previous: [Uploading race results](uploading-results)
* Next: [Editing races](editing)
