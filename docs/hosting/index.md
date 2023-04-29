---
title: Installation & Hosting
layout: home
nav_order: 20
has_children: true
---


# Installation & Hosting

To run the project, you need to be running a race server that provides the web
site that is both the main source of information for both students and staff,
but also accepts the JSON data that is the output of the applications the
students are developing (their "buggy editors"). The students do **not** do
their development work on the race server.

To start with, students submit their data by copy-and-pasting it — later, they
might program their app to use the server's API.

If you run with all the project features enabled, the server will also distribute
the source code the students need to start working by automatically forking it
into their own GitHub repo and inject project tasks as issues. It also encourages
students to store notes as they go (which can later be exported as the basis of
their project development report).


{: .rhul}
We designed this project for students with a range of experience, from new
programmers (1 term+) to some with web-dev experience. The project ran over 6
weeks with weekly programming lab sessions. Nobody is expected to complete all
the tasks — but we encouraged new programmers to aim to have attempted all of
phase 3 before the submission deadline.

## Steps to run the project

### From set-up to first student login...

* **Decide how the students will get the initial editor source code  
  Cloned from their own GitHub fork (done automatically or manually?), or just
  unzipped from a shared file?

* **Decide how you want your students to work**  
  On their own machines, on hosted microservers like Pythonanywhere or repl.it,
  or on your college's own server? 

* **Get the server running**  
  On your own server, or in the cloud. It needs a database to connect to, and
  must be accessible over the web: so you'll need to know its URL. You can get
  up and running without it, but before you run with students you'll need this
  to be over HTTPS. It's a standalone Flask server that's helpfully dockerised
  so it works nicely on cloud services like Heroku, but you can confidentally
  run it on your own school server.
  
* **Customise it**  
  Run through the setup phase, making the config fit to the the way you and your
  institution want to run the project. Most settings have sensible defaults.

* **Publish the task and tech notes**  
  The config settings not only control how the server runs, but also aspects of
  the project tasks you'll be giving to the students, and the supporting
  material. Once you've done the set-up and editted the task list (if you need
  to), publish them (you can publish tech notes externally if you want to
  write or host your own).

* **Register your students**  
  You'll need to upload a CSV of your students — this might be as simple as
  first-names-as-userames, or could be detailed data downloaded from your
  college or learning management system (like Moodle, Canvas, or Blackboard).

* **Add colleagues and Teaching Assistants too**  
  You can add new users — including staff — (at any time... in fact you can
  change the config after the set-up phase too (although it's best to get
  everything as close to what you want _before_ your give your students access).

* **Give your students access**  
  Notify your students of their own passwords (which they can change once
  they're in)... your project has begun!


### ...Students do the work....

* **Students do tasks, in phases**  
  They must tackle the phases in order, but can choose how thoroughly they
  implement each task.
  * Phase 0 is just to get the software running
  * Phase 1 is making basic improvements
  * Phase 2 introduces business logic (the race specs)
  * Phase 3 introduces breadth and complexity (multiple buggies!)
  * Phase 4 adds users and the API
  * Phase 5 adds more feature-like problems
  * Phase 6 is the open road

* **Run races and post results**  
  Depending on your schedule — weekly? nightly? now-and-again? — you can
  download buggies, calculate the outcome of a race, and upload the results.
  Winning or losing is fun (and hard to control), but _qualifying for a race_
  is the success the students have control over, and the incentive to fine-tune
  their editors.

* **Keep an eye on buggy uploads and note-taking**  
  Although students are not doing their development work on the server, it can
  provide some visibility of engagement or lack of it for early intervention
  with students who need a little more support.

### ...Wrapping up the project

* **If students must submit, provide a submission link**  
  The buggy racing project doesn't handle submission for you — that's down to
  your learning management software (if any). But you can configure a submission
  deadline and clear links to your submission information or page.

* **Deactivate the student records or shut down the server**  
  You're done!








