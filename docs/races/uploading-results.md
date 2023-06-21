---
title: Uploading race results
nav_order: 60
layout: home
parent: Running races
has_children: false
---

# Uploading race results

When you've run a race, the output of the process is a new race file. This
file is the same as before the race, except it now contains the results, and
an event-by-event log (that the race replayer can animate).

## Uploading the results (and disqualifications)

{: .navigation}
**Admin** → **Races** → Race: **Upload results**  
or  
**Admin** → **Races** → Race: **Details** →  **Upload results**

When you upload the results file, the server will check the contents of that
file against the details (including students) in the database. If there are
any discrepancies, you'll see warnings. If there are any warnings, then no
changes will be made on the server unless you choose **Ignore warnings**.

{:. warning}
When you first upload the results, do _not_ check **Ignore warnings** — it's
important you see what they are before you proceed. If it was a busy race, there
may be several things reported. Read the warnings carefully before deciding
to proceed: if it's OK, upload the file again, this time explicitly ignoring
warnings.

## Results of a race

When you upload the results of a race, they are stored in the database of the
race server. Specifically, you'll 



{: .warning}
The _race file_ (which you publish elsewhere) is not protected.  
Once you publish the race file, which is contains _all_ the details that the
race player needs to replay the race, **anyone who knows the URL** can view the
race and its results even if you haven't formally published them.