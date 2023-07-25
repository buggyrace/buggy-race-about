---
title: Introduction
layout: home
nav_order: 1
---

# Buggy Racing: a Python programming project for teachers and tutors


**Got students learning Python?**  
_Buggy Racing_ is a project (fully documented software + material) for running
a practical Python programming project:
[see the overview](overview).


{: .demo}
See the demo race server at [demo.buggyrace.net]({{site.content.demo_url}}).

<div class="callout">
  <h2 id="features">Features</h2>
<div class="two-cols">
  <div class="item-card">
    <img class="decal" src="/docs/img/feature-institution.png" />
    <p>
      Configurable for your <strong>institution</strong>
      and <strong>teaching environment</strong>
      including links to supporting sites and control over
      which student data is included
    </p>
    <p class="item-footer">
      <a href="customising">&rarr;&nbsp;customising</a>
    </p>
  </div>
  <div class="item-card">
    <img class="decal" src="/docs/img/feature-tasks.png" />
    <p>
      Project broken into <strong>tasks</strong> and
      <strong>phases</strong>, all fully customisable
      (although the defaults are tried and tested!)
    </p>
    <p class="item-footer">
      <a href="teaching/tasks-and-phases.html">&rarr;&nbsp;tasks&nbsp;&amp;&nbsp;phases</a>
    </p>
  </div>
  <div class="item-card">
    <img class="decal" src="/docs/img/feature-notes.png" />
    <p>
      Support for student <strong>reports/lab notes</strong>: collecting
      task-based texts as-they-go (or not: you configure how the project is run)
    </p>
    <p class="item-footer">
      <a href="teaching/tasks-and-phases.html">&rarr;&nbsp;tasks&nbsp;&amp;&nbsp;phases</a>
    </p>
  </div>
  <div class="item-card">
    <img class="decal" src="/docs/img/feature-tech-note.png" />
    <p>
      “<strong>Tech notes</strong>” supporting material on key technical
      concepts encountered in the project (can be replaced with your own)
    </p>
  </div>
  <div class="item-card">
    <img class="decal" src="/docs/img/feature-github.png" />
    <p>
      Can run with <strong>GitHub</strong>:
      server forks repo into students' accounts and injects tasks as
      issues (or use GitHub without automation, or just Git... or no
      Git at all — download zip and go!)
    </p>
  </div>
  <div class="item-card">
    <img class="decal" src="/docs/img/feature-work.png" />
    <p>
      Students do their development work <strong>where you want</strong>:
      own machines, college machines, or online
services like <a href="https://www.pythonanywhere.com">PythonAnywhere</a> or
<a href="https://repl.it">Replit</a>
    </p>
  </div>
</div>
</div>

## Requirements

See the [full requirements](overview/requirements). You need to
[host your own race server](hosting).

## Components

<div class="two-cols" style="align-items:flex-start">
  <div class="item-card component-server">
    <h3>Race server</h3>
    <p class="item-img">
      <img src="/docs/img/screenshots/thumb-server.png">
    </p>
    <p>
      Main project website:<br>
      students' buggy uploads
      / race results
      / staff admin features
    </p>
    <p class="item-footer">
      <code>[Python Flask, webpack, Docker]</code>
    </p>
    <div class="item-card">
      <h3>Task list</h3>
      <p>
        Detailed project tasks
        (with instructions and hints)
      </p>
      <p class="item-footer">
        <a href="{{site.content.demo_url}}/project/tasks">&rarr;&nbsp;see&nbsp;on&nbsp;demo&nbsp;site</a>
      </p>
    </div>
    <div class="item-card">
      <h3>Specs</h3>
      <p>
        Full buggy-racing specifications and
        race rules (text and JSON format)
      </p>
      <p class="item-footer">
        <a href="{{site.content.demo_url}}/specs">&rarr;&nbsp;see&nbsp;on&nbsp;demo&nbsp;site</a>
      </p>
    </div>
    <div class="item-card">
      <h3>Tech notes</h3>
      <p>
        Web pages of supporting tech material
      </p>
      <p class="item-footer">
        <a href="{{site.content.demo_url}}/tech-notes">&rarr;&nbsp;see&nbsp;on&nbsp;demo&nbsp;site</a>
      </p>
    </div>
    <div class="item-card">
      <h3>Admin pages</h3>
      <p>
        Full staff access to config, project
        and student data
      </p>
      <p class="item-footer">
        <a href="{{site.content.demo_url}}/admin">&rarr;&nbsp;see&nbsp;on&nbsp;demo&nbsp;site</a>
      </p>
    </div>
    <div class="item-card">
      <h3>Race player</h3>
      <p>
        Animated view of race result
      </p>
      <p class="item-footer">
        <a href="{{site.content.demo_url}}/races/1/replay#replay">&rarr;&nbsp;see&nbsp;on&nbsp;demo&nbsp;site</a>
      </p>
    </div>
    <div class="item-card">
      <h3>Editor zip</h3>
      <p>
        Source code for student apps
        <em>(optional, if not using GitHub)</em>
      </p>
    </div>
  </div>
<div class="flex-holder">
  <div class="item-card component-editor">
    <h3>Buggy editor</h3>
    <p class="item-img">
      <img src="/docs/img/screenshots/thumb-editor.png">
    </p>
    <p>
      Basic app that each student starts with:
      already working, but to be developed
      according to the tasks
    </p>
    <p class="item-footer">
      <code>[Python Flask, sqLite]</code>
    </p>
  </div>
  <div class="item-card component-docs">
    <h3>Documentation</h3>
    <p>
      This site :-)
    </p>
    <p class="item-footer">
      <code>[Jekyll, markdown]</code>
    </p>
  </div>
</div>
</div>

## Not included

{: .warning}
Submission and assessment of projects is **not included** (because how you do
that depends enormously on your institution and the course of study it's part
of, if any)... although [we have guidance](teaching) on how to handle that too.


{: .rhul  }
_Buggy Racing_ was originally created in 2020 as the final term project of the
CompSci Foundation programme at Royal Holloway, University of London (RHUL). We
ran it as a 6-week course of weekly lab sessions with students after at least
one full term of introductory Python.  
<br>
Since then we've made it very configurable so you can run it in a way that works
for your institution or course — university department, FE College, or local
code club. Available **for free** under the GNU GPL license.

