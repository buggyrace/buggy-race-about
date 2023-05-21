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

These config settings affect some of the behaviour around how
the tech notes (explanatory pages relating to the tech and some specifics of
the tasks) are handled.

{: .note}
You cannot edit the tech notes that are presented by the server, but you can
host them externally (so you can then change and customise them): see
`TECH_NOTES_EXTERNAL_URL`, which redirects requests away from the race server.
 
See more about [managing the tech notes](../static-content/tech-notes).



## Config settings ("Tech Notes")

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `IS_TECH_NOTE_PUBLISHING_ENABLED` | The admin interface normally lets you publish the tech notes, but if you're hosting them externally this might be confusing (because it certainly won't be changing your external site). However, there are circumstances where you want to be able to publish them here too, depending on how you're managing their creation. This setting doesn't affect the display of tech notes (see `TECH_NOTES_EXTERNAL_URL`), only whether the interface for publishing them is shown.  <br><br> _Default value:_ `Yes` |
| `TECH_NOTES_EXTERNAL_URL` | Full URL to the tech notes pages if they are *not* being hosted on this server. If you've customised them and have published them somewhere else (for example, hosted on GitHub pages), then put the URL here. By default, tech notes are hosted on the race server, so you can leave this blank.  <br><br> _Default value:_ _none/empty_ |
| `IS_ALL_CONFIG_IN_TECH_NOTES` | Choose `Yes` if all the config settings' values should be available when publishing tech notes. This setting is only relevant if you're customising the tech notes and/or publishing them externally. If `No`, only (sensible) selected config settings will be available as subtitutions in the tech notes' markdown. See the Pelican config file(s) for details.  <br><br> _Default value:_ `Yes` |
| `IS_FAKE_LATEX_CHOICE_ENABLED` | The tech notes are static pages, rendered on a dark background (to clearly distinguish from the race server's pages). If you choose `Yes`, this option adds a small button to the bottom right-hand corner of each page that toggles the style between the dark style, and a simulation of a classic page created with LaTeX, the excellent typesetting system beloved of academics. Because the tech notes are static content, this CSS toggle is implemented in JavaScript. This feature is an in-joke that only need be engaged if you are feeling playful, or if there are academics in your institution who might be horrified by the prospect of reading text in a sans-serif font on anything other than white paper.  <br><br> _Default value:_ `No` |


 ---
 * Previous: [Tasks config](tasks)
 * Next: [Races config](races)