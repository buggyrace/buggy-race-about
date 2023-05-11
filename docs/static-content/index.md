---
title: Static content
layout: home
nav_order: 45
has_children: true
---


# Static content

The task list and the tech notes are both explicitly published: that is, you
need to generate them on the server. Once you've done that, they don't change
until you generate them again.

This is for efficiency, but it can catch you out if you make any changes
_after_ you've published them. Remember to re-publish static content if you
change any config.

In practice, the material isn't expected to change once your project is running
anyway.

{: .note}
You'll see a warning message if the task list or the tech notes have not been
published. Look in the
[admin dashboard](../running/dashboard)
or the [set-up summary](../running/setup-sumary).
