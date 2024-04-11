---
title: Glossary
layout: home
nav_order: 300
---

# Glossary

Clarification of terms used in the project and its documentation.

<!-- If you edit this file, run utils/tidy-glossary.py to  -->
<!-- make a copy with the index auto-generated for you :-) -->


<!-- glossary index start -->
<ul class="glossary-index">
<li><a href="#admin-pages">admin&nbsp;pages</a></li>
<li><a href="#administrator">administrator</a></li>
<li><a href="#announcement">announcement</a></li>
<li><a href="#asbp">ASBP</a></li>
<li><a href="#authorisation-code">authorisation&nbsp;code</a></li>
<li><a href="#buggy">buggy</a></li>
<li><a href="#buggy-editor">buggy&nbsp;editor</a></li>
<li><a href="#comments">comments</a></li>
<li><a href="#config-setting">config&nbsp;setting</a></li>
<li><a href="#cost">cost</a></li>
<li><a href="#demo-site">demo&nbsp;site</a></li>
<li><a href="#demo-user">demo&nbsp;user</a></li>
<li><a href="#docker">Docker</a></li>
<li><a href="#ext_id">ext_id</a></li>
<li><a href="#ext_username">ext_username</a></li>
<li><a href="#flask">Flask</a></li>
<li><a href="#greensock">Greensock</a></li>
<li><a href="#hamster">hamster</a></li>
<li><a href="#heroku">Heroku</a></li>
<li><a href="#jinja-templates">Jinja&nbsp;templates</a></li>
<li><a href="#mass">mass</a></li>
<li><a href="#petrol">petrol</a></li>
<li><a href="#phase">phase</a></li>
<li><a href="#poster">poster</a></li>
<li><a href="#race-event">race&nbsp;event</a></li>
<li><a href="#race-file">race&nbsp;file</a></li>
<li><a href="#race-player">race&nbsp;player</a></li>
<li><a href="#race-rules">race&nbsp;rules</a></li>
<li><a href="#race-server">race&nbsp;server</a></li>
<li><a href="#racetrack">racetrack</a></li>
<li><a href="#replay">replay</a></li>
<li><a href="#report">report</a></li>
<li><a href="#rhul">RHUL</a></li>
<li><a href="#set-up-phase">set-up&nbsp;phase</a></li>
<li><a href="#specs">specs</a></li>
<li><a href="#staff-user">staff&nbsp;user</a></li>
<li><a href="#static-content">static&nbsp;content</a></li>
<li><a href="#submission">submission</a></li>
<li><a href="#task">task</a></li>
<li><a href="#task-list">task&nbsp;list</a></li>
<li><a href="#task-text">task&nbsp;text</a></li>
<li><a href="#teaching-assistant">Teaching&nbsp;Assistant</a></li>
<li><a href="#tech-notes">tech&nbsp;notes</a></li>
<li><a href="#violation">violation</a></li>
<li><a href="#vs-code">VS&nbsp;Code</a></li>
<li><a href="#webpack">webpack</a></li>
<li><a href="#zipfile">zipfile</a></li>
</ul>
<!-- glossary index end -->

---

<dl class="glossary">

<dt id="admin-pages">admin pages</dt>
<dd>
  Pages on the race server that can only be accessed by staff users, and allow
  access to configuration and student data. Paths in URLs generally start with
  <code>/admin</code>. Admin-only links tend to be pale yellow buttons, to
  distinguish from public links.
  <br>→ <a href="running/dashboard">the admin dashboard</a>
</dd>

<dt id="administrator">administrator</dt>
<dd>
  An administrator is a <a href="#staff-user">staff user</a> with full access
  to all the admin capabilities of the race server. Some admin functions also
  require knowing the <a href="#authorisation-code">authorisation code</a>.
  There should always be at least one administrator (the username/account is
  created during the <a href="#set-up-phase">set-up phase</a>).
  <br>→ <a href="running/user-management">user management</a>
</dd>

<dt id="announcement">announcement</dt>
<dd>
  Announcements are messages that are displayed either at the top of every
  page on the race server (except the tech notes), or in specific places
  (such as the login screen). 
  <br>→ <a href="running/announcements">managing announcements</a>
</dd>

<dt id="asbp">ASBP</dt>
<dd>
  The <em>Acme School of Buggy Programming</em>, a fictitious institution and
  the default value for the "Org" (Organisation) config settings, which you use
  to customise the buggy server to match your own institution.
  <br>→ <a href="customising/org">"Org" config settings</a>
</dd>

<dt id="authorisation-code">authorisation code,<br>auth code</dt>
<dd>
  A code that an administrator needs to present in order to perform some
  admin functions, including changing config settings, user data, and some
  other "risky" behaviour. Depending on how big your team is, it's feasible
  for not all admin users to know the auth code.
  <br>→ <a href="customising/auth">configuring authorisation</a>
</dd>

<dt id="buggy">buggy</dt>
<dd>
  A racing buggy. In the project, the student develops an app for editing
  the specification of a buggy, which is expressed as JSON data.
</dd>


<dt id="buggy-editor">buggy editor</dt>
<dd>
  The basic Python Flask application that each student is given at the start
  of the project, and which they need to develop to add more features and
  functionality.
  <br>→ <a href="buggy-editor">about the buggy editor</a>
</dd>

<dt id="comments">comments</dt>
<dd>
  Comments on a user are only visible to staff users (depending on config
  settings, all staff may be able to edit them, or just administrators).
  <br>→ <a href="running/user-management#commenting-on-a-user">commenting on users</a>
</dd>

<dt id="config-setting">config setting</dt>
<dd>
  The config settings control the behaviour and customisation of the race
  server. You can edit them in the config <a href="#admin-pages">admin
  pages</a> (that is, through the web interface), but they can also be set use
  environment variables if you have access to the server itself. For
  convenience, config settings are grouped thematically (for example, all the
  config settings affecting races are in the group "Races").
  <br>→ <a href="customising">customising (with config settings)</a>
</dd>

<dt id="cost">cost</dt>
<dd>
  Most components of a racing buggy have a cost. The total cost of a buggy is
  the sum of the costs of all its components. Cost matters because one of the
  <a href="#race-rules">race rules</a> is that a buggy's total cost must be
  equal or less than the cost threshold of the race: if it's not, the buggy has
  a race <a href="#violation">violation</a> and can't participate in that
  race.
</dd>

<dt id="demo-site">demo site</dt>
<dd>
  We run a demonstration server at 
  <a href="{{ site.content.demo_url }}">{{ site.content.demo_url }}</a> so you
  can see what your might server will look like. Contact us and ask for an admin
  login to have a poke around backstage.
  <br>→ <a href="{{ site.content.demo_url }}">go to the demo site</a>
</dd>

<dt id="demo-user">demo user</dt>
<dd>
  This is a special flag we set on admin users on the <a href="#demo-site">demo
  site</a> so they can't accidentally lock other admins (us) out of the demo
  site. If you spot this at all it will only be on our demo site — you won't
  see this on your own site because yours isn't a demo!
</dd>

<dt id="docker">Docker</dt>
<dd>
    Docker is a software tool that wraps applications in "containers" that
    work in different environments in isolation. The race server is "dockerised"
    so it can be installed using Docker.
    <br>→ <a href="https://www.docker.com">Docker website</a>
</dd>

<dt id="ext_id">ext_id</dt>
<dd>
  An "external identifier", which is a field you can choose to add to all
  users. This may be helpful if you need to link students in another system,
  for example if you're using an online framework like Moodle. The race server
  doesn't use this — it's just for your information (but might be handy if you
  need to automate submission of marks or feedback, for example).
  <br>→ <a href="customising/users">"Users" config settings</a>
</dd>

<dt id="ext_username">ext_username</dt>
<dd>
  An "external username", which is a field you can choose to add to all users.
  This may be useful if you identify students by their college username, for
  example (or if your students are running the buggy editor on a remote server
  via VSCode and they need this to login to that, external, server).
  <br>→ <a href="customising/users">"Users" config settings</a>
</dd>

<dt id="flask">Flask</dt>
<dd>The lightweight Python webserver the project uses.
  <br>→ <a href="https://flask.palletsprojects.com/en/2.3.x/">Flask docs</a>
</dd>

<dt id="greensock">Greensock<br>(GSAP)</dt>
<dd>
  A widely-used JavaScript library for managing animation on web pages, used by
  the <a href="#race-player">race player</a> to <a href="#replay">replay</a>
  the races.
  <br>→ <a href="https://greensock.com/gsap">GSAP website</a>
</dd>

<dt id="hamster">hamster</dt>
<dd>
  A small rodent (<em>Mesocricetus roadentus</em>) that is used as a form of
  motive power in some racing buggies.
</dd>

<dt id="heroku">Heroku</dt>
<dd>
  A cloud-based service that hosts websites — see the instructions for
  <a href="hosting/heroku">installing the race server on Heroku</a>
  (there is a fee for hosting sites)
  <br>→ <a href="http://heroku.com/">Heroku website</a>
</dd>

<dt id="jinja-templates">Jinja templates</dt>
<dd>
  The templating system used inside Flask (for example, for specifying HTML
  pages).
  <br>→ <a href="https://pypi.org/project/Jinja2">Jinja2 docs</a>
</dd>

<dt id="mass">mass</dt>
<dd>
  Most components of a racing buggy have a mass. The total mass of a buggy may
  be a factor of its performance during the race. The mass values are available
  as part of the <a href="#specs">specs</a>.
</dd>

<dt id="petrol">petrol</dt>
<dd>
  Gasoline. Buggy racing was written in British English, but — because CSS is
  the relevant context here — the "JSON names" (and hence column names) for
  buggy data require the US spelling of <code>color</code>. Since the table
  also includes <code>armour</code> (which isn't a CSS keyword), this is a
  sneaky but perhaps early lesson in close reading. Ouch!
</dd>

<dt id="phase">phase</dt>
<dd>
  The <a href="#task">tasks</a> students must do are grouped into phases. All
  the tasks in a phase should be completed before the student can move onto the
  next phase.
  <br>→ <a href="teaching/tasks-and-phases">tasks and phases</a>
</dd>

<dt id="poster">poster</dt>
<dd>
  "Poster" is an alternative name for the students' <a
  href="#report">report</a> (it's an anomaly from the RHUL marking scheme that
  we needed to use — you should just use the word "report").
  <br>→ <a href="teaching/the-report">students' posters (i.e., reports)</a>
</dd>

<dt id="race-event">race event</dt>
<dd>
  The details of what happens in a race — running out of fuel, attacking
  another buggy, moving forward — are recorded as events, which the
  <a href="#race-player">race player</a> replays. Race events are stored in the
  <a href="#race-file">race file</a> (not the database).
  <br>→ <a href="races/replaying">replaying races</a>
</dd>

<dt id="race-file">race file</dt>
<dd>
  Races are created on the <a href="#race-server">race server</a> but are run
  offline: you download the race file which contains all the data needed to run
  the race. The results are added to the race file together with the <a
  href="#race-event">race events</a>. You can upload this race file to add (and
  publish) the results of the race. The <a href="#race-player">race player</a>
  can replay a race if it has access to a race file that contains the race's
  events. The race file is in JSON format.
  <br>→ <a href="races/uploading-results">uploading race results</a>
</dd>

<dt id="race-player">race player</dt>
<dd>
  The (JavaScript-powered) web page that replays the events of a race. By
  default, the race server hosts a race player, but if you make a custom
  version you can use that instead. The race player takes a <a
  href="#race-file">race file</a> as its input — it doesn't need access to the
  race server or the server's database.
  <br>→ <a href="races/replaying">replaying races</a>
</dd>

<dt id="race-rules">race rules</dt>
<dd>
  The rules that define whether or not a buggy is allowed to take part in a 
  given race. One of the rules is that a buggy must have an even number of 
  wheels. The rules are embedded in the <a href="#specs">specs</a>.
</dd>

<dt id="race-server">race server</dt>
<dd>
  The server running the website that accepts the buggy JSON that students
  upload from their editors in order to enter races. It's a Flask webserver
  that you need to set up to run the project.
  <br>→ <a href="hosting">installing and hosting the race server</a>
</dd>

<dt id="racetrack">racetrack</dt>
<dd>
  The racetrack is (of course) the nominal setting of a race — but on the
  server it effectively means a background image (typically a JPG) and an SVG
  file that describes the path the buggies will follow.
  <br>→ <a href="races/racetracks">managing and customising racetracks</a>
</dd>

<dt id="replay">replay</dt>
<dd>
  Once a race has been run, replaying it means animating the events of the race
  in the <a href="#race-player">race player</a>. It's a bit like replaying a
  video of the race, but instead of video it's a JavaScript-powered
  reconstruction of the events recorded in the <a href="#race-file">race
  file</a>. <br>→ <a href="races/replaying">replaying races</a>
</dd>

<dt id="report">report</dt>
<dd>
  You can choose to require your students to submit a report as part of their
  project submission. Each student's report takes the form of a webpage (at
  <code>/report</code>) within their buggy editor.
  <br>→ <a href="teaching/the-report">students' reports</a>
</dd>

<dt id="rhul">RHUL</dt>
<dd>
  Royal Holloway, University of London — where this Buggy Racing project was
  conceived and originally implemented.
  <br>→ <a href="https://www.royalholloway.ac.uk/research-and-teaching/departments-and-schools/computer-science/">RHUL Computer Science</a>
</dd>

<dt id="set-up-phase">set-up phase</dt>
<dd>
  When the race server is first started, you <em>must</em> change or confirm
  all the <a href="#config-setting">config settings</a>. Until you've done
  this, the server is in the <a href="#set-up-phase">set-up phase</a> and will
  not let you access any other pages (except the login, in case you interrupt
  the browser session while you're in this phase).
  <br>→ <a href="customising/setup-phase">the set-up phase</a>
</dd>

<dt id="specs">specs,<br>specifications</dt>
<dd>
  The specs define the acceptable values for racing buggies, including the name
  of each component, its type, the range of acceptable values it can have, a
  description of its role, and, where applicable, its cost and mass. The specs
  also include race rules. The specs are available on the webserver both as
  human-readable web page and as tabulated data, which may (or may not) be
  useful to students building their buggy editors.
  <br>→ <a href="{{ site.content.demo_url }}/specs">specs on the demo site</a>
</dd>

<dt id="staff-user">staff user</dt>
<dd>
  A staff user on the race server is an <a href="#administrator">administrator</a> or a
  <a href="#teaching-assistant">Teaching Assistant</a>. Staff users can
  access the admin pages.
  <br>→ <a href="running/user-management">user management</a>
</dd>

<dt id="static-content">static content</dt>
<dd>
  Static content on the race server refers mainly to pages that need to be
  <em>published</em> before they can be accessed. There are three such
  components: the <a href="#task-list">task list</a>, the <a
  href="#tech-notes">tech notes</a>, and the buggy editor <a
  href="#zipfile">zipfile</a> (that last one is optional, depending on how
  you're distributing the buggy editor source code).
  <br>
  There's a page in the tech notes about the more general business of creating
  and using <em>static content</em> on the web (<a
  href="{{site.content.demo_url}}/tech-notes/static-vs-dynamic">see it on the
  demo server</a>).
  <br>→ <a href="static-content">static content</a> (on the race server)
</dd>

<dt id="submission">submission, submit</dt>
<dd>
  If you're running the project as an assessed piece of work, which may or may
  not include a <a href="#report">report</a>, then you'll probably need a mechanism by which students submit their work. The server doesn't handle
  submission itself, but you can use some of the
  <a href="customising/project">"Project" config settings</a> to inform
  students about how and when to submit their work.
  <br>→ <a href="teaching/submission">how students submit </a> 
</dd>

<dt id="task">task</dt>
<dd>
  A task is a unit of work for a student to do. Almost every task can be
  implemented more or less thoroughly (ideally depending on the ability and
  experience of the student).
  Tasks are grouped into phases.
  The phase is indicated by the digit at the start of the task's mnemonic name.
  <br>→ <a href="teaching/tasks-and-phases">tasks and phases</a>
</dd>

<dt id="task-list">task list</dt>
<dd>
  The task list is the page on the race server that contains all of the tasks
  for students to do. It includes details and hints for each task, as well as
  buttons that allow students to enter <a href="#task-text">task texts</a> as
  they attempt them.
  <br>→ <a href="static-content/task-list">the task list</a>
</dd>

<dt id="task-text">task text</dt>
<dd>
  A task text is short text a student saves on the race server describing how
  they approached or completed a task. The student can download their task
  texts (possibly as rendered markdown inside HTML) to be added to their
  <a href="#report">report</a> before the project is submitted (if your students are
  required to submit a report).
  <br>→ <a href="static-content/task-list">tracking progress</a> (texts help
  you with this)
</dd>

<dt id="teaching-assistant">Teaching Assistant<br>(TA)</dt>
<dd>
  A staff user on the race server who has read-access to student data but
  limited config/admin access. Depending on config settings, TAs may be able
  to edit staff comments on users, and reset students' passwords for them.
  <br>→ <a href="running/user-management">user management</a>
</dd>

<dt id="tech-notes">tech notes</dt>
<dd>
  This race server includes a set of static web pages that provide supporting
  material about some of the technical aspects of the project — for example, on
  the demo server see <a href="{{ site.content.demo_url
  }}/tech-notes/flask-webserver">how Flask works as a webserver</a>. The tech
  notes can't be edited in place, but you can make and host your own copy and
  link to those instead.
  <br>→ <a href="static-content/tech-notes">tech notes</a>
</dd>

<dt id="violation">violation</dt>
<dd>
  A racing buggy only qualifies for a race if it satisfies all the <a
  href="#race-rules">race rules</a>. When you run a race, the rules are checked
  (technically, this could be called "scrutineering") and each rule that fails
  is a <em>violation</em>. When the race results are published, the violations
  for each non-runner are shown. This is significant because a key incentive
  for a student to build a good <a href="#buggy-editor">buggy editor</a> is to
  detect and prevent violations.
  <br>→ <a href="races/">running races</a>
</dd>

<dt id="vs-code">VS Code,<br>Visual Studio Code</dt>
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

<dt id="webpack">webpack</dt>
<dd>
  A software tool that bundles up assets like JavaScript, style sheets, and
  graphics for a webserver. The race server uses webpack, which itself
  depends on node.js.
  <br>→ <a href="https://webpack.js.org">webpack docs</a>
</dd>

<dt id="zipfile">zipfile</dt>
<dd>
  On the race server, there's a special case of the <a
  href="#buggy-editor">buggy editor</a> source code being made available as a
  zipped archive. This is the (default) way that it's distributed to students,
  but isn't needed if you're using GitHub. The contents of the zipfile are
  typically customised before being created, so this is one of the items of <a
  href="#static-content">static content</a> on the race server that you may
  need to publish.
  <br>→ <a href="buggy-editor/distributing-the-code">distributing the code</a>
</dd>

</dl>

---

