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

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `SUPERBASICS_URL` | There are a few places (for example in the workflow page and the tech notes) that link to a &#34;superbasics&#34; site which explains basic concepts for students. You can use the default, but you can also fork it and customise it, in which case put its URL here. Note that the links are to specific paths within the superbasics, which are added to this base URL, so if you host your own version be cautious about changing existing paths within it.  <br/><br/> _Default value:_ `https://superbasics.beholder.uk` |
| `SITE_1_NAME` | Name (shown on button)  <br/><br/> _Default value:_ _none/empty_ |
| `SITE_1_TEXT` | Short description  <br/><br/> _Default value:_ _none/empty_ |
| `SITE_1_URL` | Full URL to external site/resource  <br/><br/> _Default value:_ _none/empty_ |










  
---
 * Previous: [Organisation config](org)
 * Next: [Project config](project)