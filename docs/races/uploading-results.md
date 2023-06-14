---
title: Uploading race results
nav_order: 60
layout: home
parent: Running races
has_children: false
---

# Uploading race results

{: .todo}
This isn't ready yet: the documentation is still being written.

When you've run a race, the output of the process is a new race file. This
now contains the results, and an event-by-event log (that the race replaying
can animate).

## Uploading the results (and diqualifications)

{: .navigation}
**Admin** → **Races** → Race: **Upload results**  
or  
**Admin** → **Races** → Race: **Details** →  **Upload results**

When you upload the results file, the server will check the contents of that
file against the details (including students) in the database. If there are
any discrepancies, you'll see warnings.


---

{: .todo}
Currently you can't publish _race files_ on the race server — you need to
publish them elsewhere on the web.

{: .warning}
The _race file_ (which you publish elsewhere) is not protected.  
Once you publish the race file, which is contains _all_ the details that the
race player needs to replay the race, **anyone who knows the URL** can view the
race and its results even if you haven't formally published them.