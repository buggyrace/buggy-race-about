---
title: Viewing buggies
layout: home
nav_order: 50
parent: Day-to-day running
---

# Viewing buggies

{: .navigation}
**Admin** → **Buggies**

You can see a list of the buggies that are currently on race server. Typically
you only care about the students' buggies (since those are the ones that
will be in the races), but you _can_ include non-student (presumably staff)
users' buggies on this page too.

When you [download a race file](../races/downloading), that (JSON) race file
automatically includes a snapshot of all the buggies that are candidates for
the race. This means that you don't usually need to download the buggies
separately. Nonetheless, there is a CSV download option available if you want
it. If you write your own custom race scripts, this might be useful to you.

You can inspect the last-uploaded JSON and the buggy of an individual user —
if they have one — by going to their [user page](../running/user-management)
or via the [task texts summary](../teaching/progress).

## A buggy might not match the latest JSON

A student who has never uploaded any JSON, or who has only uploaded malformed
JSON which did not parse, will not have a buggy on the race server.

Remember that the buggy that you see on the server is the result of the last
_valid_ JSON that the student uploaded. If a student submits bad JSON — that is,
JSON that does not parse — then that latest JSON is recorded, but the student's
buggy won't be updated. This is why you may see JSON that does not describe
the buggy for the same student.

If you have enabled the config setting `IS_BUGGY_DELETE_ALLOWED` (in the
"Server" group), then a student can delete their buggy. The last JSON they
uploaded will still be available to inspect.

## Default buggies (can be very common!)

If a student uploads valid JSON, their buggy will be updated and any missing
values will accept their default values. This is common at the beginning of
the project because **initially** the buggy editor produces JSON with only two
items in it: the number of wheels (`qty_wheels`), and the local ID (see below).

You can see the default values for a buggy in the specifications. You can
usually spot default buggies in the list of buggies (or in the races) because
they have a plain white pennant, four wheels, and a single unit of petrol.

{: .demo}
See the [buggy specifications]({{site.content.demo_url}}/specs/).

In general, up on the server you'd expect to see more settings in more buggies
deviate from the default settings as students develop their editors.


## What is the `id2` field?

The field marked id<sup>2</sup> is the buggy's ID on the students own buggy
editor database.

When students' buggies are saved on the race server, they are allocated an
(auto-incrementing) ID in the database. However, those buggies also have an ID
in their native database — that is, the SQLite database on each student's own
machine. To start with, that ID is _always_ `1`. You can see this as the
`DEFAULT_BUGGY_ID` constant in the [buggy editor
code](https://github.com/buggyrace/buggy-race-editor/blob/main/app.py). It's
common for students not to think about this at all (which is fine) until they
get to the task 3-MULTI. That's when their editor starts to handle multiple
buggies. This datum might usually be ignored, but it is made available (in the
race files, for example) because the later task 5-RACELOG might require the
student to be able to identify which of their buggies was the one they uploaded
for a given race.
