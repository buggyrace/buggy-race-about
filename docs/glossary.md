---
title: Glossary
layout: home
nav_order: 300
---

# Glossary

Clarification of terms used in the project and its documentation.

<dl>

<dt>ASBP</dt>
<dd>
  The <em>Acme School of Buggy Programming</em>, a fictitious institution and
  the default value for the "Org" (Organisation) config settings, which you use
  to customise the buggy server to match your own institution.
  <br>→ <a href="customising/org">"Org" config settings</a>
</dd>

<dt>admin pages</dt>
<dd>
  Pages on the race server that can only be accessed by staff users, and allow
  access to configuration and student data. Paths in URLs generally start with
  <code>/admin</code>. Admin-only links tend to be pale yellow buttons, to
  distinguish from public links.
  <br>→ <a href="running/dashboard">the admin dashboard</a>
</dd>

<dt>administrator</dt>
<dd>
  An administrator is a <strong>staff user</strong> with full access to all the
  admin capabilities of the race server. Some admin functions also require
  knowing the <strong>auth code</strong>. There should always be at least one
  administrator (the username/account is created during the
  <strong>set-up phase</strong>).
  <br>→ <a href="running/user-management">user management</a>
</dd>

<dt>announcement</dt>
<dd>
  Announcements are messages that are displayed either at the top of every
  page on the race server (except the tech notes), or in specific places
  (such as the login screen). 
  <br>→ <a href="running/announcements">managing announcements</a>
</dd>

<dt>authorisation code,<br>auth code</dt>
<dd>
  A code that an administrator needs to present in order to perform some
  admin functions, including changing config settings, user data, and some
  other "risky" behaviour. Depending on how big your team is, it's feasible
  for not all admin users to know the auth code.
  <br>→ <a href="customising/auth">configuring authorisation</a>
</dd>

<dt>buggy</dt>
<dd>
  A racing buggy. In the project, the student develops an app for editing
  the specification of a buggy, which is expressed as JSON data.
</dd>


<dt>buggy editor</dt>
<dd>
  The basic Python Flask application that each student is given at the start
  of the project, and which they need to develop to add more features and
  functionality.
  <br>→ <a href="buggy-editor">about the buggy editor</a>
</dd>

<dt>config setting</dt>
<dd>
  The config settings control the behaviour and customisation of the race
  server. You can edit them in the config <strong>admin pages</strong> (that
  is, through the web interface), but they can also be set use environment
  variables if you have access to the server itself. For convenience, config
  settings are grouped thematically (for example, all the config settings
  affecting races are in the group "Races").
  <br>→ <a href="customising">customising (with config settings)</a>
</dd>

<dt>comments</dt>
<dd>
  Comments on a user are only visible to staff users (depending on config
  settings, all staff may be able to edit them, or just administrators).
  <br>→ <a href="running/user-management#commenting-on-a-user">commenting on users</a>
</dd>

<dt>cost</dt>
<dd>
  Most components of a racing buggy have a cost. The total cost of a buggy is
  the sum of the costs of all its components. Cost matters because one of the
  <strong>race rules</strong> is that a buggy's total cost must be equal or less
  than the cost threshold of the race: if it's not, the buggy has a
  <strong>race violation</strong> and can't participate in that race.
</dd>

<dt>Docker</dt>
<dd>
    Docker is a software tool that wraps applications in "containers" that
    work in different environments in isolation. The race server is "dockerised"
    so it can be installed using Docker.
    <br>→ <a href="https://www.docker.com">Docker website</a>
</dd>

<dt>ext_username</dt>
<dd>
  An "external username", which is a field you can choose to add to all users.
  This may be useful if you identify students by their college username, for
  example (or if your students are running the buggy editor on a remote server
  via VSCode and they need this to login to that, external, server).
  <br>→ <a href="customising/users">"Users" config settings</a>
</dd>

<dt>ext_id</dt>
<dd>
  An "external identifier", which is a field you can choose to add to all users.
  This may be helpful if you need to link students in another system, for example
  if you're using an online framework like Moodle. The race server doesn't use
  this — it's just for your information (but might be handy if you need to
  automate submission of marks or feedback, for example).
  <br>→ <a href="customising/users">"Users" config settings</a>
</dd>

<dt>Flask</dt>
<dd>The lightweight Python webserver the project uses.
  <br>→ <a href="https://flask.palletsprojects.com/en/2.3.x/">Flask docs</a>
</dd>

<dt>Greensock<br>(GSAP)</dt>
<dd>A widely-used JavaScript library for managing animation on web pages,
  used by the <strong>race player</strong> to <strong>replay</strong> the
  races.
  <br>→ <a href="https://greensock.com/gsap">GSAP website</a>
</dd>

<dt>hamster</dt>
<dd>
  A small rodent (<em>Mesocricetus roadentus</em>) that is used as a form of
  motive power in some racing buggies.
</dd>

<dt>Heroku</dt>
<dd>
  A cloud-based service that hosts websites — see the instructions for
  <a href="hosting/heroku">installing the race server on Heroku</a>
  (there is a fee for hosting sites)
  <br>→ <a href="http://heroku.com/">Heroku website</a>
</dd>

<dt>Jinja templates</dt>
<dd>
  The templating system used inside Flask (for example, for specifying HTML
  pages).
  <br>→ <a href="htthttps://pypi.org/project/Jinja2">Jinja2 docs</a>
</dd>

<dt>mass</dt>
<dd>
  Most components of a racing buggy have a mass. The total mass of a buggy may
  be a factor of its performance during the race. The mass values are available
  as part of the <strong>specs</strong>.
</dd>

<dt>petrol</dt>
<dd>
  Gasoline. Buggy racing was written in British English, but — because CSS is
  the relevant context here — the "JSON names" (and hence column names) for
  buggy data require the US spelling of <code>color</code>. Since the table
  also includes <code>armour</code> (which isn't a CSS keyword), this is a
  sneaky but perhaps early lesson in close reading. Ouch!
</dd>

<dt>phase</dt>
<dd>
  The <strong>tasks</strong> students must do are grouped into phases. All the
  tasks in a phase should be completed before the student can move onto the
  next phase.
  <br>→ <a href="teaching/tasks-and-phases">tasks and phases</a>
</dd>

<dt>poster</dt>
<dd>
  "Poster" is an alternative name for the students' <strong>report</strong>
  (it's an anomaly from the RHUL marking scheme that we needed to use — you
  should just use the word "report").
  <br>→ <a href="teaching/the-report">students' posters (i.e., reports)</a>
</dd>

<dt>race event</dt>
<dd>
  The details of what happens in a race — running out of fuel, attacking
  another buggy, moving forward — are recorded as events, which the
  <strong>race player</strong> replays. Race events are stored in the
  <strong>race file</strong> (not the database).
  <br>→ <a href="races/replaying">replaying races</a>
</dd>

<dt>race file</dt>
<dd>
  Races are created on the <strong>race server</strong> but are run offline:
  you download the race file which contains all the data needed to run the
  race. The results are added to the race file together with the <strong>race
  events</strong>. You can upload this race file to add (and publish) the
  results of the race. The <strong>race player</strong> can replay a race
  if it has access to a race file that contains the race's events.
  The race file is in JSON format.
  <br>→ <a href="races/uploading-results">uploading race results</a>
</dd>

<dt>race player</dt>
<dd>
  The (JavaScript-powered) web page that replays the events of a race.
  By default, the race server hosts a race player, but if you make a custom
  version you can use that instead. The race player takes a <strong>race
  file</strong> as its input — it doesn't need access to the race server or
  the server's database.
  <br>→ <a href="races/replaying">replaying races</a>
</dd>

<dt>race rules</dt>
<dd>
  The rules that define whether or not a buggy is allowed to take part in a 
  given race. One of the rules is that a buggy must have an even number of 
  wheels. The rules are embedded in the <strong>specs</strong>.
</dd>

<dt>race server</dt>
<dd>
  The server running the website that accepts the buggy JSON that students
  upload from their editors in order to enter races. It's a Flask webserver
  that you need to set up to run the project.
  <br>→ <a href="hosting">installing and hosting the race server</a>
</dd>

<dt>racetrack</dt>
<dd>
  The racetrack is (of course) the nominal setting of a race — but on the server
  it effectively means a background image (typically a JPG) and an SVG file
  that describes the path the buggies will follow.
  <br>→ <a href="races/racetracks">managing and customising racetracks</a>
</dd>

<dt>replay</dt>
<dd>
  Once a race has been run, replaying it means animating the events of the race
  in the <strong>race player</strong>. It's a bit like replaying a video of the
  race, but instead of video it's a JavaScript-powered reconstruction of the
  events recorded in the <strong>race file</strong>.
  <br>→ <a href="races/replaying">replaying races</a>
</dd>

<dt>report</dt>
<dd>
  You can choose to require your students to submit a report as part of their
  project submission. Each student's report takes the form of a webpage (at
  <code>/report</code>) within their buggy editor.
  <br>→ <a href="teaching/the-report">students' reports</a>
</dd>

<dt>RHUL</dt>
<dd>
  Royal Holloway, University of London — where this Buggy Racing project was
  conceived and originally implemented.
</dd>

<dt>specs, specifications</dt>
<dd>
  The specs define the acceptable values for racing buggies, including the
  name of each component, its type, the range of acceptable values it can have,
  a description of its role, and, where applicable, its cost and mass. The specs
  also include race rules. The specs are available on the webserver both as
  human-readable web page and as tabulated data, which may (or may not) be
  useful to students building their buggy editors.
</dd>

<dt>staff user</dt>
<dd>
  A staff user on the race server is an <strong>administrator</strong> or a 
  <strong>Teaching Assistant</strong>. Staff users can access the admin pages.
  <br>→ <a href="running/user-management">user management</a>
</dd>

<dt>static content</dt>
<dd>
  Static content on the race server refers mainly to pages that need to be
  <em>published</em> before they can be accessed. There are three such
  components: the <strong>task list</strong>, the <strong>tech notes</strong>,
  and the buggy editor <strong>zipfile</strong> (that last one is optional,
  depending on how you're distributing the buggy editor source code).
  <br>
  There's a page in the tech notes about the more general business of creating
  and using <em>static content</em> on the web.
  <br>→ <a href="static-content">static content</a> (on the race server)
</dd>

<dt>task</dt>
<dd>
  A task is a unit of work for a student to do. Almost every task can be
  implemented more or less thoroughly (ideally depending on the ability and
  experience of the student).
  Tasks are grouped into phases.
  The phase is indicated by the digit at the start of the task's mnemonic name.
  <br>→ <a href="teaching/tasks-and-phases">tasks and phases</a>
</dd>

<dt>task list</dt>
<dd>
  The task list is the page on the race server that contains all of the tasks
  for students to do. It includes details and hints for each task, as well
  as buttons that allow students to enter <strong>task texts</strong> as they
  attempt them.
  <br>→ <a href="static-content/task-list">the task list</a>
</dd>

<dt>task text</dt>
<dd>
  A task text is short text a student saves on the race server describing how
  they approached or completed a task. The student can download their task
  texts (possibly as rendered markdown inside HTML) to be added to their
  <strong>report</strong> before the project is submitted (if your students are
  required to submit a report).
  <br>→ <a href="static-content/task-list">tracking progress</a> (texts help
  you with this)
</dd>

<dt>Teaching Assistant<br>(TA)</dt>
<dd>
  A staff user on the race server who has read-access to student data but
  limited config/admin access. Depending on config settings, TAs may be able
  to edit staff comments on users, and reset students' passwords for them.
  <br>→ <a href="running/user-management">user management</a>
</dd>

<dt>VS Code,<br>Visual Studio Code</dt>
<dd>
  <a href="https://code.visualstudio.com">VS Code</a> is a widely-used editor
  and interactive development environment by Microsoft. One way of running the
  buggy racing project is to set up students' code on a departmental server and
  access it through VS Code and a SSH tunnel. The advantage of using VS Code in
  this way is ease of deployment, including the Python plugins — it's
  relatively straightforward to install on Windows, MacOS and Linux — and that
  all students are (at least to start with) working in the same editor, which
  means demos and videos are consistent with what they see on their own screens.
  <br>→ <a href="customising/project">"Project" config settings</a>
  (see <code>IS_USING_REMOTE_VS_WORKSPACE</code>)
</dd>

<dt>webpack</dt>
<dd>
  A software tool that bundles up assets like JavaScript, style sheets, and
  graphics for a webserver. The race server uses webpack, which itself
  depends on node.js.
  <br>→ <a href="https://webpack.js.org">webpack docs</a>
</dd>
</dl>

---

