---
title: Glossary
layout: home
nav_order: 300
---

# Glossary

Clarification of terms used in the documentation

---
<!--
<dt></dt>
<dd></dd>
-->

<dl>

<dt>admin pages</dt>
<dd>
  Pages on the race server that can only be accessed by staff users, and allow
  access to configuration and student data.
</dd>

<dt>authorisation code<br>(auth code)</dt>
<dd>
  A code that an administrator needs to present in order to perform some
  admin functions, including changing config settings, user data, and some
  other "risky" behaviour. Depending on how big your team is, it's feasible
  for not all admin users to know the auth code.
</dd>

<dt>buggy editor</dt>
<dd>
  The basic Python Flask application that each student is given at the start
  of the project, and which they need to develop to add more features and
  funcationality.
</dd>

<dt>Flask</dt>
<dd>The lightweight Python webserver the project uses:
  <a href="https://flask.palletsprojects.com/en/2.3.x/">Flask docs</a>
</dd>

<dt>Jinja templates</dt>
<dd>
  The templating system used inside Flask (for example, for specifying HTML
  pages): <a href="https://pypi.org/project/Jinja2/">Jinja2</a>
</dd>
  
<dt>race server</dt>
<dd>
  The server running the website that accepts the buggy JSON that students
  upload from their editors in order to enter races. It's a Flask webserver
  that you need to set up to run the project.
</dd>

<dt>staff user</dt>
<dd>
  A staff user on the race server is an <strong>administrator</strong> or a 
  <strong>Teaching Assistant</strong>. Staff users can access the admin pages.
</dd>

</dl>