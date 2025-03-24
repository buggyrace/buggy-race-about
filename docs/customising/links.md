---
title: Links config
layout: home
nav_order: 40
parent: Customising
has_children: false
---


# Configuring links to external sites

{: .navigation}
**Admin** → **Config** → Config:**Links**

You can add up to four links to external sites, which are displayed on the
home page and on the footer of the tech notes. These are useful for linking to
social media sites or other pages that are related to your course.

{: .rhul}
For the RHUL Foundation module, we used these to link the module's Moodle page,
and the MS Teams channel where staff were available for help.


{: .screenshot}
![Screenshot showing two external links](/docs/img/screenshots/links-example.png)

{: .caption}
Example showing two links displayed on the race server's home page — one to
Moodle, another to Discord. The text is shown above the button, and the name on
the button.

## Config settings ("Links")

The settings are numbered from zero to three, inclusive. It doesn't matter if
you leave gaps/skip numbers, but the links will be displayed in numeric order —
so `SITE_1` will always be displayed before `LINK_4`.



{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `LINK_1_NAME` | Name of the linked site (it's shown on button).<br>If this is empty, the link **will not be displayed**.  <br><br> _Default value:_ _none/empty_ |
| `LINK_1_TEXT` | A short description of the site or link  <br><br> _Default value:_ _none/empty_ |
| `LINK_1_URL` | Full URL to external site/resource  <br><br> _Default value:_ _none/empty_ |

Repeat for:

* `LINK_1_NAME`, `LINK_1_TEXT`, `LINK_1_URL`
* `LINK_2_NAME`, `LINK_2_TEXT`, `LINK_2_URL`
* `LINK_3_NAME`, `LINK_3_TEXT`, `LINK_3_URL`


---
 * Previous: [Organisation config](org)
 * Next: [Project config](project)