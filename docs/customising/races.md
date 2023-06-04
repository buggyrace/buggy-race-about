---
title: Races config
layout: home
nav_order: 80
parent: Customising
has_children: false
---


# Configuring races

{: .navigation}
**Admin** → **Config** → Config:**Races**

The races are the incentive for students to develop good editors. You don't
_need_ to run races, but we recommend that you do!
 
See more about [running races](../running/running-races).


## Config settings ("Races")

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `IS_USERNAME_PUBLIC_IN_RESULTS` | When you publish race results, are usernames (as well as the buggies' pennants) shown?  <br><br> _Default value:_ `Yes` |
| `DEFAULT_RACETRACK_IMAGE` | URL of the default background image (2:1 aspect ratio JPG or PNG for racetracks used in the race replayer).   <br><br> _Default value:_ _none/empty_ |
| `DEFAULT_RACETRACK_PATH_SVG` | The default path — described as a <path> element within the SVG file found at this URL — for racetracks used in the race replayer).   <br><br> _Default value:_ _none/empty_ |
| `DEFAULT_RACE_COST_LIMIT` | The default point cost threshold for buggies: you can always override this when you create each race.  <br><br> _Default value:_ `200` |
| `IS_RACE_VISIBLE_BY_DEFAULT` | Should a race be public as soon as you create it? If you choose `No`, you'll have to remember to publish a race in order for students to see it.  <br><br> _Default value:_ `No` |
| `BUGGY_RACE_PLAYER_URL` | If you want to override the default race player and host your own, specify it here and races will link to that instead (passing the 'results file' URL as a query variable called `race`). Do this if you want or need to run this as a standalone service (e.g., hosted on GitHubPages and potentially totally customised). If you don't specify a URL, races will use the race player on this server.  <br><br> _Default value:_ _none/empty_ |
| `BUGGY_RACE_PLAYER_ANCHOR` | Anchor which is appended to any race player URLs. If the race player page has a header (which the default player on this server does), this scrolls that out of the way. If you don't prefix this with `#`, it will automatically be added.  <br><br> _Default value:_ `#replay` |


 ---
 * Previous: [Tech notes config](tech-notes)
 * Next: [GitHub config](github)