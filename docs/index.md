---
title: Introduction
layout: home
nav_order: 1
---

# Buggy Racing: a Python programming project for teachers and tutors


**Got students learning Python?**  
_Buggy Racing_ is the software, documentation and supporting material for
running a practical Python programming project:
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
      <a href="teaching/the-report.html">&rarr;&nbsp;the&nbsp;report</a>
    </p>
  </div>
  <div class="item-card">
    <img class="decal" src="/docs/img/feature-tech-note.png" />
    <p>
      “<strong>Tech notes</strong>” supporting material on key technical
      concepts encountered in the project (can be replaced with your own)
    </p>
    <p class="item-footer">
      <a href="static-content/tech-notes">&rarr;&nbsp;the&nbsp;tech&nbsp;notes</a>
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
    <p class="item-footer">
      <a href="buggy-editor/distributing-the-code">&rarr;&nbsp;distributing&nbsp;the&nbsp;code</a>
    </p>
  </div>
  <div class="item-card">
    <img class="decal" src="/docs/img/feature-work.png" />
    <p>
      Students do their development work <strong>where you want</strong>:
      own machines, college machines, or online
services like <a href="buggy-editor/running-pythonanywhere">PythonAnywhere</a> or
<a href="buggy-editor/running-replit">Replit</a>.
    </p>
    <p class="item-footer">
      <a href="buggy-editor/running-where">&rarr;&nbsp;where&nbsp;to&nbsp;work</a>
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
        <a href="{{site.content.demo_url}}/races/{{site.content.demo_race_id}}/replay#replay">&rarr;&nbsp;see&nbsp;on&nbsp;demo&nbsp;site</a>
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
    <p class="item-img">
      <img src="/docs/img/screenshots/thumb-about.png">
    </p>
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
CompSci Foundation programme at Royal Holloway, University of London (RHUL). It
ran as a 6-week course of weekly lab sessions with students who'd done at least
one full term of introductory Python.  
<br>
Since then we've made it very configurable so you can run it in a way that works
for your institution or course — university department, FE College, or local
code club. Available **for free** under the GNU GPL license.

## License: free and open source software

The race server and buggy editor is made available under the **GNU Affero
General Public License**: a free, copyleft license (see [gnu.org for
details](http://www.gnu.org/licenses/)).

In practice this means: you and your institution don't have to pay to use it
— there's nothing to buy, because the whole thing is made freely, explicitly
available for you — and you can modify it and even improve it (but if you
do, you should make those improvements available to other people too).

See the [race server's LICENSE.txt](https://github.com/buggyrace/buggy-race-server/LICENSE.txt)

> "Free as in speech, free as in beer"

Remember to teach your students about Open Source software :-)

![Buggy racing mascot: Mesocricetus roadentus](/docs/img/rene-hamster-1.png)

