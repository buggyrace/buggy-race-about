---
title: What is it?
layout: home
nav_order: 5
parent: Buggy editor
has_children: false
---

# What is the buggy editor?

The buggy editor is a small Python application that the students develop and
run. It's a Flask webserver that lets the user produce a JSON description of a
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

{: .demo}
"Number of wheels" is just one aspect of a racing buggy that students can
define. See the [full race specs]({{ site.content.demo_url }}/specs) for all
the others!

{: .note}
The GitHub repo containing the buggy editor source code is at  
[github.com/buggyrace/buggy-race-editor](https://github.com/buggyrace/buggy-race-editor)  
...but — because you should customise it before sharing with your students —
we recommend that you do not share that directly (see following section).

## Staff and the editor

From the staff point of view, you need to decide the best way for your students
to start with the editor code (either as a directory of files, or a Git repo
depending on how you want to do it), and the environment in which you want them
to do the work. The rest of this _Buggy editor_ section goes into these things
in detail.


---
* Next: [Distributing the code](distributing-the-code)
