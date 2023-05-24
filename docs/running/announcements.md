---
title: Announcements
layout: home
nav_order: 20
parent: Day-to-day running
---


# Announcements

{: .navigation}
**Admin** → **Announce**

You can publish (and hide) announcements that appear on the race server pages.

{: .screenshot}
![Screenshot showing two example top-of-page announcements](/docs/img/screenshots/example-announcements.png)

{: .caption}
Example of two top-of-page announcements: the first is `special` style (and
uses HTML to allow both bold and regular text), the second is `danger` style.

There are two types of announcement:

* **On every page**  
  Standard announcments are displayed at the top of every page (except the tech
  notes). You can choose from a set of preset styles that change the colour of
  the announcement:  
  <span class="announce-danger">danger</span>
  <span class="announce-info">info</span>
  <span class="announce-special">special</span>
  <span class="announce-warning">warning</span>

* **On specific pages**  
  These announcements allow you to place messages in specific locations:
    * `get-editor`  
      The get-editor announcment is shown on the settings page when the student
      has forked their editor repo. This lets you add instruction/encouragement
      if you have a complex process to follow after automatic forking (if this
      is enabled).
    * `login`  
      The login announcement is displayed above the login form. Use this if
      you need to clarify to your students how/where you have supplied them
      with their login criteria
    * `tagline`  
      The tagline is displayed on the race server's home page, underneath
      the main title.

## Creating an announcement

{: .navigation}
**Admin** → **Announce** → **New announcement**

Creating a new announcement does not publish it. You must do that separately
(the **Publish** button is available once you've created the announcement).

There's also an **Add example announcement** button if the race server notices
you don't already have a "Buggy racing is currently suspended" announcement
(shown in the example at the top of this page).

Creating the example won't publish it — like any announcement editing, you can
only publish it by explicitly clicking on the **Publish** button. You can
inspect, edit or even delete it.


## Editing announcements

You can choose to enable HTML in any announcement (set **Allow HTML** to `Yes`).
This allows you to use markup like `<strong>bold</strong>`.

{: .warning}
Be careful if you enable HTML in an announcement!  
It _is_ possible to break layout on pages if you do not close every tag that you
open.

{: .note}
When you change an announcement it will _always_ revert to being hidden. This
is effectively an "are you sure?" failsafe. You must always explicitly
**publish** an announcement after you've changed it.


## Publishing announcements

An announcement is only published when you _explicitly_ click the **Publish**
button.

{: .screenshot}
![Screenshot showing announcement list](/docs/img/screenshots/announcement-list.png)

{: .caption}
A list of three announcements — note the **Publish** buttons.


## Recovering from an announcement with critically broken HTML

If you mess up the HTML in an HTML-enabled announcement badly enough, the list
display _might_ be so broken that it won't display the **Edit** button you need
to click to put it right. This can happen if your HTML does not properly
balance (that is, you opened an HTML tag such as `<div>` that you didn't close).

Don't panic! Use the **Suppress HTML in list** button (or go to
`/admin/announcements/nohtml` on your race server) to stop the HTML rendering
in the list view (and at the top of the screen). Then you can click **Edit** on
the offending announcement, and fix the offending HTML in the announcement's
text.

