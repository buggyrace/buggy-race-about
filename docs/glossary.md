---
title: Glossary
layout: home
nav_order: 300
---

# Glossary

Clarification of terms used in project and its documentation.

---
<!--
<dt></dt>
<dd></dd>
-->

<dl>

<dt>ASBP</dt>
<dd>
  The <em>Acme School of Buggy Programming</em>, a fictitious institution and
  the default value for the "Org" (Organisation) config settings, which you use
  to customise the buggy server to match your own institution.
</dd>

<dt>admin pages</dt>
<dd>
  Pages on the race server that can only be accessed by staff users, and allow
  access to configuration and student data. Paths in URLs start with
  <code>/admin</code>. Admin-only links tend to be pale yellow buttons, to
  distinguish from public links.
</dd>

<dt>administrator</dt>
<dd>
  An administrator is a <strong>staff user</strong> with full access to all the
  admin capabilities of the race server. Some admin functions also require
  knowing the <strong>auth code</strong>. There should always be at least one
  administrator (the username/account is created during the
  <strong>set-up phase</strong>).
</dd>

<dt>announcement</dt>
<dd>
  Announcements are messages that are displayed either at the top of every
  page on the race server (except the tech notes), or in specific places
  (such as the login screen). 
  <a href="running/announcements">About managing announcements</a>.
</dd>

<dt>authorisation code<br>(auth code)</dt>
<dd>
  A code that an administrator needs to present in order to perform some
  admin functions, including changing config settings, user data, and some
  other "risky" behaviour. Depending on how big your team is, it's feasible
  for not all admin users to know the auth code.
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
</dd>

<dt>config setting</dt>
<dd>
  The config settings control the behaviour and customisation of the race
  server. You can edit them in the config <strong>admin pages</strong> (that
  is, through the web interface), but they can also be set use environment
  variables if you have access to the server itself. For convenience, config
  settings are grouped thematically (for example, all the config settings
  affecting races are in the group "Races").
</dd>

<dt>comments</dt>
<dd>
  Comments on a user are only visible to staff users (depending on config
  settings, all staff may be able to edit them, or just administrators).
</dd>

<dt>cost</dt>
<dd>
  Most components of a racing buggy have a cost. The total cost of a buggy is
  the sum of the costs of all its components. Cost matters because one of the
  <strong>race rules</strong> is that a buggy's total cost must be equal or less
  than the cost threshold of the race: if it's not, the buggy has a
  <strong>race violation</strong> and can't participate in that race.
</dd>

<dt>ext_username</dt>
<dd>
  An "external username", which is a field you can choose to add to all users.
  This may be useful if you identify students by their college username, for
  example (or if your students are running the buggy editor on a remote server
  via VSCode and they need this to login to that, external, server).
</dd>

<dt>Flask</dt>
<dd>The lightweight Python webserver the project uses:
  <a href="https://flask.palletsprojects.com/en/2.3.x/">Flask docs</a>
</dd>

<dt>hamster</dt>
<dd>
  A small rodent (<em>Mesocricetus roadentus</em>) that is used as a form of
  motive power in some racing buggies.
</dd>

<dt>Jinja templates</dt>
<dd>
  The templating system used inside Flask (for example, for specifying HTML
  pages): <a href="https://pypi.org/project/Jinja2/">Jinja2</a>
</dd>

<dt>mass</dt>
<dd>
  Most components of a racing buggy have a mass. The total mass of a buggy may
  be a factor of its performance during the race. The mass values are available
  as part of the <strong>specs</strong>.
</dd>

<dt>phase</dt>
<dd>
  The <strong>tasks</strong> students must do are grouped into phases. All the
  tasks in a phase should be completed before the student can move onto the
  next phase.
</dd>

<dt>poster</dt>
<dd>
  "Poster" is an alternative name for the students' <strong>report</strong>
  (it's an anomaly from the RHUL marking scheme that we needed to use — you
  should just use the word "report").
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
</dd>

<dt>report</dt>
<dd>
  You can choose to require your students to submit a report as part of their
  project submission. Each student's report takes the form of a webpage (at
  <code>/report</code>) within their buggy editor.
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
</dd>

<dt>task</dt>
<dd>
  A task is a unit of work for a student to do. Almost every task can be
  implemented more or less thoroughly (ideally depending on the ability and
  experience of the student).
  Tasks are grouped into phases.
  The phase is indicated by the digit at the start of the task's mnemonic name.
</dd>

<dt>task list</dt>
<dd>
  The task list is the page on the race server that contains all of the tasks
  for students to do. It includes details and hints for each task, as well
  as buttons that allow students to enter <strong>task texts</strong> as they
  attempt them.
</dd>

<dt>task text</dt>
<dd>
  A task text is short text a student saves on the race server describing how
  they approached or completed a task. The student can download their task
  texts (possibly as rendered markdown inside HTML) to be added to their
  <strong>report</strong> before the project is submitted (if your students are
  required to submit a report).
</dd>

<dt>Teaching Assistant (TA)</dt>
<dd>
  A staff user on the race server who has read-access to student data but
  limited config/admin access. Depending on config settings, TAs may be able
  to edit staff comments on users, and reset students' passwords for them.
</dd>

</dl>