---
title: Running remotely
layout: home
nav_order: 60
parent: Buggy editor
has_children: false
---


# Running on a remote server



This is the most specific way for the students to run their editor app.
First the editor repo is forked to each student's GitHub repo. Then a VSCode
workspace file is prepared (once the fork has been done) which can clone _that_
repo into the student's account on the remote server. The remote server must
be set up such that each student has an individual port number assigned. The
remote server uses these port numbers so that the each web app can be accessed
uniquely.

{: .rhul}
This is the set-up we used after the first two years of running the project
with students developing on their own machines (or in the cloud on Replit).
The advantage of this mechanism, which forces the students to work on the 
college server is that we could be certain that all students' environments were
the same. It also allowed us to exploit the VNC-based session sharing that was
in place — so we could remotely support students without needing to lock into
their own, private machines. Finally having access to the students' dev
environment does mean it's possible to check on the actual progress.  

## Steps for using the VS Code workspace file




---
* Previous: [Running on Replit](running-replit)
