---
title: Tech notes config
layout: home
nav_order: 70
parent: Customising
has_children: false
---


# Configuring tech notes

{: .navigation}
**Admin** → **Config** → Config:**Tech notes**

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
 
 
 
See more about [managing the tech notes](../static-content/tech-notes).

## Config settings ("Tech Notes")

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `IS_TECH_NOTE_PUBLISHING_ENABLED` | The admin interface normally lets you publish the tech notes, but if you're hosting them externally this might be confusing (because it certainly won't be changing your external site). However, there are circumstances where you want to be able to publish them here too, depending on how you're managing their creation. This setting doesn't affect the display of tech notes (see `TECH_NOTES_EXTERNAL_URL`), only whether the interface for publishing them is shown.  <br><br> _Default value:_ `Yes` |
| `TECH_NOTES_EXTERNAL_URL` | Full URL to the tech notes pages if they are *not* being hosted on this server. If you've customised them and have published them somewhere else (for example, hosted on GitHub pages), then put the URL here. By default, tech notes are hosted on the race server, so you can leave this blank.  <br><br> _Default value:_ _none/empty_ |
| `IS_ALL_CONFIG_IN_TECH_NOTES` | Choose `Yes` if all the config settings' values should be available when publishing tech notes. This setting is only relevant if you're customising the tech notes and/or publishing them externally. If `No`, only (sensible) selected config settings will be available as subtitutions in the tech notes' markdown. See the Pelican config file(s) for details.  <br><br> _Default value:_ `Yes` |



 ---
 * Previous: [Tasks config](tasks)
 * Next: [Races config](races)