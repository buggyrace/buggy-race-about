---
title: What is it?
layout: home
nav_order: 5
parent: Buggy editor
has_children: false
---

# What is the buggy editor?

The buggy editor is small Python application that the students develop and run.
It's a Flask webserver that lets the user produces a JSON description of a
racing buggy which can then be uploaded to the race server. If a student's
buggy has been uploaded to the server, it's automatically included in the next
race.

{: .screenshot}
![Buggy editor front page](/docs/img/screenshots/buggy-editor.png)

{: .caption}
Front page of the Buggy Editor.

The editor is very limited — all you can do is specify the number of wheels —
but it is _working_. The project tasks guide the students through developing the
editor app from this basic program to, potentially, a much more sophisticated
one.

{: .screenshot}
![Buggy editor basic form](/docs/img/screenshots/buggy-editor-form.png)

{: .caption}
The "make buggy" form of the editor. Until the student adds more capability,
the editor only accepts the number of wheels.


## Staff and the editor

From the staff point of view, you need to decide the best way for your students
to start with with editor code (either as a directory of files, or a Git repo
depending on how you want to do it), and the environment in which you want them
to do the work. The rest of this section goes into these things in detail.



---
* Next: [Customising the Buggy Editor](customising)
