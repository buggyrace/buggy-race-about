---
title: Static placeholder
layout: home
nav_order: 20
parent: Shutting down
has_children: false
---


# Running a static placeholder

Once you've [shut down the race server](../shutdown), any attempts to connect to
it in a browser will, of course, fail. This may well be OK — it's what happens
when any server is offline. But if the URL to the server is one that you might
be re-using, and links to it may persist — on your institution's online learning
platform or module website, for example — consider running a static placeholder
in its place.

The static site is intended solely to return meaningful content to a human who
follows the link. This may be helpful to students and also to staff who are
unfamiliar with the project.

This presupposes that you can either remap the DNS settings for your race server
to point at the placeholder, or you can put the placeholder content on the host
that was running that race server.

A static placeholder _could_ be as simple as a single page that displays a
"not running at the moment" message. The limitation of this is that ideally you
want to send a meaningful response to _any_ path that might have persistent
links. The solution shown below is to run a GitHub Pages site with a custom 404
page. (There is a case for returning
[302 Found](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/302)
 → the holding page instead, but... this really is just a placeholder!).

## An example of a placeholder site

{: .rhul}
We've been running the buggy racing project every year, but it's only active in
the final term. In the other terms, we don't run the full server (not least
because there's a small cost to doing so). We now use a simple (one-page)
GitHub Pages site as a placeholder in the interim, and we change the `CNAME`
record in the DNS settings for the race server's subdomain to point at that.

We use [GitHub Pages](https://pages.github.com) because it provides a reliable,
free static hosting platform that can run on a custom domain. The repo we used
is public at:

* [`github.com/davewhiteland/buggy-race-stub-www`](https://github.com/davewhiteland/buggy-race-stub-www)

It's a [Jekyll](https://jekyllrb.com) site because that's the mechanism
supported by GitHub Pages. The 404 custom page catches URLs to all paths, but
is fundamentally a copy of the index page, shown below. In effect we're stubbing
all the page requests, except the index, to a 404. Note that this feature —
a custom 404 page — only works on GitHub Pages sites when using a custom URL
(which is explicitly what we're doing).

{: .screenshot}
![Screenshot of Royal Holloway's buggy-racing project showing "currently suspended"](/docs/img/screenshots/shut-down-placeholder.jpg)

{: .caption}
Screenshot of the [RHUL](../glossary#rhul) "placeholder" buggy racing site, with
message "Buggy racing is currently suspended".

When we're ready to run the dynamic race server again, we spin it up (and test
it on its [local](../hosting/heroku), or [heroku-specific](../hosting/heroku),
URL), and when it's ready we change the DNS record to point `CNAME` back to
that.

