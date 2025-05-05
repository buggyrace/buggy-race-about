---
title: Races config
layout: home
nav_order: 100
parent: Customising
has_children: false
---


# Configuring races

{: .navigation}
**Admin** → **Config** → Config:**Races**

The races are the incentive for students to develop good editors. You don't
_need_ to run races, but we recommend that you do!
 
See more about [running races](../races/).



















## Config settings ("Races")

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `IS_USERNAME_PUBLIC_IN_RESULTS` | When you publish race results, are usernames (as well as the buggies&#39; pennants) shown?  <br/><br/> _Default value:_ `Yes` |
| `IS_SHOWING_EXAMPLE_RACETRACKS` | Do you want the admin interface to include the example racetracks? If you are certain you only want to use your own custom racetracks, you can choose `No` to hide the button that adds the pre-built examples. Unless you&#39;ve already built your racetracks, you should almost certainly choose `Yes`.  <br/><br/> _Default value:_ `Yes` |
| `DEFAULT_FLAG_COLOR` | The default `flag_color` for buggies (this should be a CSS color). If you haven&#39;t raced before, the default (a middle-grey) is a good choice, because it encourages students to change it to something more interesting.  <br/><br/> _Default value:_ `#888888` |
| `DEFAULT_RACE_COST_LIMIT` | The default point cost threshold for buggies: you can always override this when you create each race.  <br/><br/> _Default value:_ `200` |
| `IS_DNF_POSITION_DEFAULT` | Is a **Did not Finish** race result still given an ordinal position (based on how far the buggy _did_ travel before it stopped)? It&#39;s common in motorsport to not grant a position to a racer who did not complete the necessary number of laps... but in buggy racing, buggies can more easily run out of fuel, especially early in the project when nobody knows how much petrol or how many hamsters you need to get round a track. So choose `Yes` if you want to avoid demoralising students for mishaps during races. This is the default for your project and you can override it on a race-by-race basis.  <br/><br/> _Default value:_ `Yes` |
| `IS_RACE_VISIBLE_BY_DEFAULT` | Should a race be public as soon as you create it? If you choose `No`, you&#39;ll have to remember to publish a race in order for students to see it.  <br/><br/> _Default value:_ `No` |
| `BUGGY_RACE_PLAYER_URL` | If you want to override the default race player and host your own, specify it here and races will link to that instead (passing the &#39;results file&#39; URL as a query variable called `race`). Do this if you want or need to run this as a standalone service (e.g., hosted on GitHubPages and potentially totally customised). If you don&#39;t specify a URL, races will use the race player on this server.  <br/><br/> _Default value:_ _none/empty_ |
| `BUGGY_RACE_PLAYER_ANCHOR` | Anchor which is appended to any race player URLs. If the race player page has a header (which the default player on this server does), this scrolls that out of the way. If you don&#39;t prefix this with `#`, it will automatically be added.  <br/><br/> _Default value:_ `#replay` |
| `IS_STORING_RACE_FILES_IN_DB` | When you upload race files (primarily for replaying races), do you want to store them here on the race server, in the database? If you don&#39;t, you&#39;ll need to publish them online somewhere which has a friendly CORS policy (GitHub pages works fine), and make sure you store the URL correctly when you update the race. If you&#39;re running an especially large project or little server, there may be efficiency benefits in _not_ using the database, but otherwise it&#39;s simplest to choose `Yes`.   <br/><br/> _Default value:_ `Yes` |
| `IS_RACE_FILE_START_STAMPED` | Do you want the race start (date+time) to appear in the filename when you download a race file? You might not need this if your races always have recognisably unique titles.  <br/><br/> _Default value:_ `Yes` |
| `IS_RACE_FILE_DATE_STAMPED` | Do you want a datestamp (when you downloaded it) to appear in the filename when you download a race file?  <br/><br/> _Default value:_ `No` |

  
 ---
 * Previous: [Users config](users)
 * Next: [VCS config](vcs)