---
title: Running locally
layout: home
nav_order: 30
parent: Buggy editor
has_children: false
---


# Running the editor locally

The simplest way for students to run their individual buggy editor apps is to
execute the Python script on their own machine. Flask runs as a webserver on
port 5000 so each student can access their app on `http://localhost:5000`.

{: .note}
In the buggy editor's `app.py`, we _explicitly_ set the port number to 5000
even though this is Flask's default. This is to make it explicit to the
students where that number is coming from.

The catch with this is it assumes that students have access to such an environment (typically, on their own machine), and it requires the development environment to be set up correctly.

How straightforward it is to set up a working Python environment depends on a
number of factors, some of which can be out of your control. **Do not
underestimate how bewildering — and demoralising — new students may find this
process**.

It's probably best to stick to recommending a process that you (and your
teaching assistants) are most familiar with. For many people that may be
installing
[Anaconda](https://www.anaconda.com).

Once the students have Python, and the editor source code, they should be able to install the libraries (most significantly: Flask) with:

```
pip install -r requirements.txt
```

Students need to initialise the database by running `init_db.py` (the app will
run without it, but fails when it encounters the absence of the `buggies`
table). This is deliberate.

Finally, running the app is probably done with:

```
python app.py
```

All of this is covered in more detail in the [editor's README](https://github.com/buggyrace/buggy-race-editor/blob/main/README.md)
(which, at this stage, will also be on the student's own machine).

{: .rhul}
We first ran this project during the UK's full Covid lockdown — so, 100% online.
The complications arising from students attempting different Python installations on different operating systems was far from straightforward. (Variations _within_ Windows caused us the most trouble). Much will depend on
what exposure your students already have to navigating file systems, using the
command line, or simply being able to articulate their set-up problems or
interpret error messages.
<br>
The first phase (especially tasks `0-GET` and `0-RUN`) is about getting past
this milestone. It's significant that getting the code running is itself part
of the task list. Don't dismiss this — there's a lot to understand for new students in this process, and for many of them it can be the most abstract part of the whole project.


{: .note}
If your students need support with some of the computer basics, it might help
to point them at the [CompSci superbasics](https://superbasics.beholder.uk).



---
* Previous: [Customising the editor](customising)
* Next: [fixme](fixme)
