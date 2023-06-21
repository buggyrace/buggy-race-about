---
title: Downloading
nav_order: 40
layout: home
parent: Running races
has_children: false
---

# Downloading the race file

{: .navigation}
**Admin** → **Races** → Race: **Details** → **Download...**

> The races are run _offline_ (see [running the race](running) for details on
> why and how this is). You need to download the **race file** for the
> race, because this is used as input when you run the run.

When you download the race file, the race server bundles up all the information
needed *including the buggies*. The time you download the file matters: it's
a snapshot of the buggies that will be considered for the race. For this reason
you should download the race file as soon after the start time you published.

Usually, you just need to click the blue button **Download race file with
(current) buggies**.

The race file is actually a JSON file, and when you run the race, that process
produces a new race file for you to upload containing the results.

## Download options

{: .note}
You don't need these if you're simply running a race.

There may be circumstances when you want a little more control over the contents
of the race file you download. Specifically, if the race has not been run but
you do not want to use the server's _current_ buggies, you can download the race
file without them. This presupposes you have the buggies available in some other
form.

If you are looking at a race that has already been run, downloading the race
file is a little more complicated. Ideally, you'll have _uploaded_ the results
file after running the race — by default, storing it on the race server. If
so, that's the definitive race file because that one will contain the events
as well as the results. But the server also lets you download race file(s) that
are constructed from the data. These won't include the events, and may include
buggies that have changed since the last time you downloaded the race file.

## About buggies in the race files

Each race file is a snapshot of the time when the race was run, together with
the results and events that occurred (offline). For this reason you need to be
clear about when you download them. Ideally, download the race file, run the
race, and upload the (new) race file — and that's all you need.

The results shown on the race server — which are extracted from the race file
when you upload it — show buggies _as they were_ when the race was run. This
is important because students' buggies **can and will change between races**.

---

{: .todo}
We're planning on adding a scheduler so downloading the file (or at least,
capturing a snapshot of it when the race is due to start) happens automatically
in future releases.  
See [issue #176](https://github.com/buggyrace/buggy-race-server/issues/176)

