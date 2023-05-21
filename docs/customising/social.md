---
title: Social sites config
layout: home
nav_order: 40
parent: Customising
has_children: false
---


# Configuring social or related sites

{: .navigation}
**Admin** → **Config** → Config:**Social**

You can add upo to four links to external sites, which are displayed on the home
page and on the footer of the tech notes. These are useful for linking to
social media sites or other pages that are related to your course.

{: .rhul}
For the RHUL Foundation module, we used these to link the module's Moodle page,
and the MS Teams channel where staff were available for help.


## Config settings ("Social")

The settings are numbered from zero. It doesn't matter which numbers you use
(it doesn't matter if you jump from 0 to 3), but they will be displayed in
numeric order — so `SOCIAL_0` will always be displayed before `SOCIAL_4`.



{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `SOCIAL_0_NAME` | Name (shown on button)  <br><br> _Default value:_ _none/empty_ |
| `SOCIAL_0_TEXT` | Short description of the site or link  <br><br> _Default value:_ _none/empty_ |
| `SOCIAL_0_URL` | Full URL to external site/resource  <br><br> _Default value:_ _none/empty_ |

Repeat for:

* `SOCIAL_1_NAME`, `SOCIAL_1_TEXT`, `SOCIAL_1_URL`
* `SOCIAL_2_NAME`, `SOCIAL_2_TEXT`, `SOCIAL_2_URL`
* `SOCIAL_3_NAME`, `SOCIAL_3_TEXT`, `SOCIAL_3_URL`


---
 * Previous: [Organisation config](org)
 * Next: [Users config](users)