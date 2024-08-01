---
title: Editing races
nav_order: 90
layout: home
parent: Racing
has_children: false
---

# Editing races

{: .navigation}
**Admin** → **Races** → Race: **Details** → **Edit**

You can edit the details of a race after you've created it.

The setting _Is visible?_ can be used to hide a race entirely from the students.
This can be useful if you've prepared a race (the first race, for example) but
haven't decided when to run it. We recommend _not_ running races right from the
start of the project, so that students can make some progress on their editors
before the first race.

{: .note }
The public `/races` page only ever shows **one** future race — the next one.
So if you have ten races, all visible, only the _next_ one will appear on that
page (together with all past ones that are not hidden). When you view the list
of races in the admin (**Admin** → **Races**), you see _all_ the races on the
server: all the past and future races are listed.

The setting _Are results visible?_ can be used to hide race results while you
are working on them. You can check that the results (and replaying) work as
expected before publishing them to the students.


## Abandoning races

{: .navigation }
**Admin** → **Races** → Race: **Details** → **Edit** → **Abandon race**

If you decide not to run a race, you can abandon it. This specifically means
the race was not run, and will have no results. It's a good idea to also edit
the _Description_ of the race explaining why it was abandoned.

One practical reason for abandoning a race is if there were no buggies entered,
because you cannot upload results that contain no buggies. This might happen if
there were no buggies on the server at the time of the race: perhaps no students
have uploaded buggies yet (or, if you've enabled deletion with
`IS_BUGGY_DELETE_ALLOWED` set to `Yes`, those that were there have been deleted).


## Changing races after results have been uploaded

You can usefully change the visibility of races (or fix typos). Otherwise,
changing some details about the race after you've uploaded the results may not
be helpful — especially if the race's "Is visible?" or "Are results visible?"
settings are both set to Yes.

However, you _can_ change the results of a race by uploading a new race file.
The existing results **will be deleted** before being replaced with the new
ones.

Similarly, if you decide to abandon a race after you've uploaded results, those
results will be deleted (because, by definition, an abandoned race has no
results). You'll see warnings if you try to do this. You can proceed, but be
aware that you can't undo it (although, if you still have the race file
containing the results that you had previously uploaded, you _could_ upload
them again).


## Deleting a race

{: .navigation}
**Admin** → **Races** → Race: **Details** → **Delete**

You can delete a race. If you do so, its results will also be removed.

---

* Previous: [Replaying races](replaying)
* Next: [Custom racetracks](racetracks)
