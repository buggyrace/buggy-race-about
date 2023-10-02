---
title: Replaying races
nav_order: 70
layout: home
parent: Racing
has_children: true
---

# Replaying races

<details close markdown="block">
  <summary>
    Contents of this page:
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

{: .navigation}
Top menu bar: **Races** → Race: **Replay**  
or  
**Admin** → **Races** → Race: **Replay** 

The race player **replays the races** by animating the events which are
described by the "race file" (the JSON file produced when you run a race).

{: .demo}
See this in action by [replaying a race]({{site.content.demo_url}}/races/{{site.content.demo_race_id}}/replay#replay).

This presupposes that the race file is available online — by default, if you've
uploaded it to the race server, it will be there, although you can override
this if you've set the config setting `IS_STORING_RACE_FILES_IN_DB` to `No`.

{: .note}
If _Are results visible?_ is `No` for this race, students won't be able to
replay the race (the button won't be there) — but staff can use the admin
**Races** page to access it instead.

{: .screenshot}
![Screenshot showing a replay of a race](/docs/img/screenshots/race-replay.jpg)

{: .caption}
The race player replaying a race. Specifically, a race file has been loaded
(via an Ajax call) and the events within it are being animated over an image
of the racetrack.

## The default ("built-in") player

The player that runs on the server will automatically "track" the current
user's buggy so students see their own buggy highlighted in the replay (if they
are logged in when they visit the page). You can click on any buggy on the
track — or in the player's console-like log — to highlight that one instead.

There's a **Fast** button in case the race is running too slowly (this can
happen if there are lots of punctures).

## Standalone player

{: .navigation}
**Admin** → **Races** → **Replay race** + URL

As staff, you can test a race file in the player _before_ you've uploaded it to
the server using the "standalone" player. That is, if you have a race file you
can replay it even if it's not in the database on the server. However, you need
to have the race file on a URL the server can access, which may mean you need
to overcome [CORS limitations](#hosting-elsewhere-publishing-race-files) too.
This can be useful if you're running a local copy of the server (as a developer
maybe) and want to test on localhost.

## Hosting elsewhere: extracting the race player

{: .warning}
This requires some familiarity with front-end web development to implement,
but if you're cool with that then it's handy for quickly replaying races on the
(local) machine you're actually executing the races on.

The race player can be wholly independent of the database. It replays the race
described in the race file, and doesn't need to know anything else (such as
whether or not users or buggies actually exist on a server). As it is
implemented with JavaScript, it's effectively static content that you can host
on any web page that can access the race file URLs passed to it (it makes an
AJAX request to load the race file).

We've made it feasible to extract the race player so you can drop it somewhere
convenient — either on localhost on your own machine (if you publish race files
on localhost to test them), or on a public host like GitHub pages.
Specifically, you can access the HTML page served without any of the race
server's headers and footers. Here are the files you'll need:

* HTML: `/admin/race/replay/stripped-down`
* default script: `/races/assets/buggy-race-player.js`
* [GSAP library script](https://greensock.com): `/races/assets/gsap.min.js` (or
  get it from GSAP's CDN)

{: .note}
This allows you to [customise your race-player](custom-player) (just as you
might [customise the race-runner](custom-runner)). For example, if you add new
types of events to your races, you can also update the JavaScript code of the
race player to handle them. After all, that's what we did :-).
<br>
If you do develop the race player, please consider sharing your work back with
us so other people can benefit from it too.  

{: .suggest}
If you have students with JavaScript/front-end skills who are looking for
another challenge, adding new features to the race-player (or re-implementing
it entirely) is a great project in itself!



## Hosting elsewhere: publishing race files


If you don't use the default player, or you host the race files on another
server, be aware that there may be
[cross-origin resource sharing](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
(CORS) restrictions on whether the player can access them. Specifically, CORS
may apply to the JSON race files and SVG path files.

Files served from GitHub pages sites (including JSON files) do set the
`Access-Control-Allow-Origin` header to `*` so can be used to host race files.

See [customising Races (config settings)](../customising/races) for more
details, including `BUGGY_RACE_PLAYER_URL` and `BUGGY_RACE_PLAYER_ANCHOR`.

{: .note}
A subtle difference between the standalone race player and built-in one on the
server is that the standalone version will replay _any_ race file passed into
its `?race=` query variable. Because the built-in version (initiated by
clicking a **Replay** button) only replays race files you or your staff have
uploaded, it will not replay unauthorised races (for example, no tampering to
create offensive usernames, and no changing the events of the race to display a
different result...). If you use the standalone version, the CORS restrictions
that browsers implement are to some extent performing a similar service — but
be aware that, if presented with acceptable CORS headers, your standalone race
player is capable of replaying "unofficial" races too.

## Building your own

It's entirely feasible to create a custom race-player. This lets you add more
sophisticated features than the somewhat basic version than is currently part
of the race server.

* about [building your own race-player](custom-player/)

---

* Previous: [Uploading race results](uploading-results)
* Next: [Editing races](editing)
