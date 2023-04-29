---
title: Getting the code
layout: home
nav_order: 30
parent: Buggy editor
has_children: false
---


# How students get their copy of the source code

The students need their own copy of the buggy editor source code, in order to
get to work developing it.

There are a number of ways to do this. You need to decide before the project
starts which method suits you and your students best, because it affects some
of the preparation you need to do with your config settings.

{: .rhul}
We required our students to fork the buggy editor repo on GitHub, and then
either clone (or download by zip) the files from there. As well as being a
convenient way to distribute the code (we automated the forking from within the
race server) this was to expose them to Git and GitHub... but once they had the
code, we deliberately did _not_ make using Git or GitHub mandatory within the
project.

## Distribute a zip file

* **pros:**
  * students don't need a GitHub account
* **cons:**
  * unzipping is surprisingly confusing to some students  
  * no exposure to version control
  * no control over the environment in which they are then developing (this might be con, depending on how confident your students are)

Once you've made your own fork of the buggy editor, and [customised it](customising), you can download its files as a zip. To get the zip file, go to your forked repo on GitHub, click on the green **Code** button, and choose **Download zip**. You can either distribute that zip file to your students directly, or (since your forked repo up on GitHub is public) you can share
the URL of your forked repo and give students instructions how to download it from there.

Make sure your students know how to extract files from a zip. It will matter
_where_ in their file system they extract it to, and whether or not they
create an enclosing folder when they unzip it.


## Students manually fork your repo

## Server automatically forks into students' repos



---
* Previous: [Customising the editor](customising)
* Next: [Running locally](running-locally)
