---
title: How students enter
nav_order: 30
layout: home
parent: Running races
has_children: false
---

# How students enter a race

{: .navigation}
Top menu bar: **Upload**

Students "upload a buggy" (JSON output from their buggy editor) to the race
server.

> Initially, they simply copy-and-paste the JSON.  
> Later, they can send it using the API.

**If a student has uploaded a buggy before the race deadline, their buggy is
automatically entered into the next race** (and all subsequent races).

As staff, this is why you should fluctuate the race costs between races (and,
if you have control over them when you run the races) environmental factors —
such as number of laps). This rewards students who have the most control over
_changing their buggy_ to match different criteria... which is the superpower
that their buggy editor provides.

{: .note}
Although the tech notes and race server don't explicitly advertise it, of
course students can upload JSON that hasn't come out of their buggy editor.
This was an early design decision (it could be restricted by forcing the use of
the API, for example). For some students this is their first experience of
practical JSON so if that leads to an appreciation of the textual and
expressive nature of JSON... then so be it. What typing raw JSON doesn't do is
validate the data, or calculate the cost of the buggy — which is the function
of the buggy editor.

{: .suggest}
A useful discussion to have with students who realise that the editor is merely
facilitating the production of their buggy JSON is: is _What is the shortest
JSON string you can upload to create a buggy?_ This can lead into thinking
about text files and parsing, and similarities and differences between
programming languages and data formats. What can't be serialised trivially in
JSON? Why not? What does the core Python library `json` do? How does the
`/json` route in their buggy editor work?

## Feedback from the upload

When a student uploads JSON, the server's response includes feedback as to what
worked, and what didn't. For example, if the JSON is not well-formed, there will
be a warning (and, where possible, a line number indicating where the problem
was). More buggy-specific data problems are also reported.

Note that any values that don't make sense to the server will be replaced with
their default values, together with a warning.

The default buggy editor produces JSON that describes a buggy with an explicit
number of wheels (`qty_wheels`) — nothing more. Because everything accepts the
default, except that number, the buggy that is produced will have the default
pennant (a white flag).

> Specifically, if you're looking at the specs, this means a `flag_pattern`
> that is `plain`, with the colour set to `white`.
>
> The default buggy also has only one unit of (default) petrol as its primary
> motive power, which isn't enough to get it around a lap of any distance.

## Inspecting buggies and uploaded JSON

{: .navigation}
**Admin** → **Users** → _Username_  
or  
**Admin** → **Texts** → _User's "buggy upload" (spanner)_

If you inspect a user, you can see their current buggy and the last JSON they
uploaded (together with a timestamp). Note that the buggy might not be that
described by the last upload — the buggy is only updated if _valid JSON_ is
uploaded.

The race server does not store a history of all a student's uploads — only the
most recent one.



