---
title: Step-by-step process
layout: home
nav_order: 50
parent: Overview
---

# Step-by-step process

In a nutshell: you need to decide _how_ you're going to customise the project,
get the server up and running, and then run the project with your students.

The steps below break this right down so you can see what's involved
and the sort of things you need to think about before you start.

* **Setting up**: [from set-up to first student login...](#from-set-up-to-first-student-login)
* **Running**: [...students do the work....](#students-do-the-work)
* **Ending**: […wrapping up the project](#wrapping-up-the-project)

---

## From set-up to first student login...

* **Decide how the students will get the initial editor source code**  
  Cloned from their own GitHub fork (done automatically or manually?), or just
  unzipped from a shared file?

* **Decide how you want your students to work**  
  On their own machines, on hosted microservers like Pythonanywhere or repl.it,
  or on your college or institutions's own server? 

* **Get the server running**  
  On your own server, or in the cloud. It needs a database to connect to, and
  must be accessible over the web: so you'll need to know its URL, which should
  be running over HTTPS. It's a standalone Flask server that's helpfully
  dockerised so it is well-behaved on cloud services like Heroku, or (if you or
  your IT team are confident) on your own school server.
  
* **Customise it**  
  Run through the set-up phase, making the config fit to the the way you or
  your institution want to run the project. Most settings have sensible
  defaults, so this isn't too arduous.

* **Publish the task and tech notes**  
  The config settings not only control how the server runs, but also aspects of
  the project tasks you'll be giving to the students, and the supporting
  material. Once you've done the set-up and editted the task list (if you need
  to), publish them (you can publish tech notes externally if you want to
  write or host your own).

* **Register your students**  
  You'll need to upload a CSV file of your students — this might be as simple as
  first-names-as-usernames, or could be a detailed data downloaded from your
  college or learning management system (like Moodle, Canvas, or Blackboard).
  The server has a utility to help you prepare this from existing spreadsheets.

* **Add colleagues and Teaching Assistants too**  
  You can add new users — including staff — at any time. In fact you can
  change the config after the set-up phase too (although it's best to get
  everything as close to what you want _before_ your give your students access).

* **Give your students access**  
  Notify your students of their own passwords (which they can change once
  they're in)... your project has begun!


## ...Students do the work....

* **Students do tasks, in phases**  
  They must tackle the phases in order, but can choose how thoroughly they
  implement each task. The default project looks broadly like this (you can
  change this by editing/adding/removing tasks):
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
  Although students are not doing their development work on the race server, it
  can provide some visibility of engagement or lack of it for early intervention
  with students who need a little more support.

## ...Wrapping up the project

* **If students must submit, provide a submission link**  
  The buggy racing project doesn't handle submission for you — that's down to
  you and your learning management software (if any). But you can configure a
  submission deadline and clear links to your submission information or page.

* **Deactivate the student records and shut down the server**  
  You're done!

