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

You can add up to to four links to external sites, which are displayed on the
home page and on the footer of the tech notes. These are useful for linking to
social media sites or other pages that are related to your course.

{: .rhul}
For the RHUL Foundation module, we used these to link the module's Moodle page,
and the MS Teams channel where staff were available for help.


{: .screenshot}
![Screenshot showing two social links](/docs/img/screenshots/social-example.png)

{: .caption}
Example showing two social links displayed on the race server's home page — one
to Moodle, another to Discord. The text is shown above the button, and the name
on the button.

## Config settings ("Social")

The settings are numbered from zero to three, inclusive. It doesn't matter if
you leave gaps/skip numbers, but the links will be displayed in
numeric order — so `SOCIAL_0` will always be displayed before `SOCIAL_4`.



{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `SOCIAL_0_NAME` | Name of the linked site (it's shown on button).<br>If this is empty, the link **will not be displayed**.  <br><br> _Default value:_ _none/empty_ |
| `SOCIAL_0_TEXT` | A short description of the site or link  <br><br> _Default value:_ _none/empty_ |
| `SOCIAL_0_URL` | Full URL to external site/resource  <br><br> _Default value:_ _none/empty_ |

Repeat for:

* `SOCIAL_1_NAME`, `SOCIAL_1_TEXT`, `SOCIAL_1_URL`
* `SOCIAL_2_NAME`, `SOCIAL_2_TEXT`, `SOCIAL_2_URL`
* `SOCIAL_3_NAME`, `SOCIAL_3_TEXT`, `SOCIAL_3_URL`


---
 * Previous: [Organisation config](org)
 * Next: [Users config](users)