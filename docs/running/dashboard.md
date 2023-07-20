---
title: Admin dashboard
layout: home
nav_order: 8
parent: Day-to-day running
---


# The admin dashboard

{: .navigation}
**Admin**

The admin dashboard shows a summary of activity including user activity. If you
haven't published [static content](../static-content) yet, you'll see warnings
here too.

{: .screenshot}
![Screenshot of the admin dashboard](/docs/img/screenshots/admin-dashboard.png)

{: .caption}
The admin dashboard summaries recent login and task-text activity.


### Purging unexpected settings

If you see this message:

    Unexpected config settings found in database

...together with one or more blue buttons marked **Purge**, it means that there
are config settings in your database which are no longer being used. This might
happen after a software update. It's safe to click each such blue button and
delete the deprecated config setting.
