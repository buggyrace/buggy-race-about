---
title: From spreadsheet
layout: home
nav_order: 20
parent: Registering users
has_children: false
---


# Adding new students from a spreadsheet (CSV)

To register new students on the race server, you can upload a spreadsheet with
columns for their username, password, and whatever other fields you chose when
you were [configuring users](../customising/users). Specifically, you need to
upload a _comma-separated values_ (CSV) file continaing such values (you can
save a CSV file from any spreadsheet program, including Excel).

{: .navigation}
**Admin** → **Users** → **Register new students**

{: .warning}
Bulk registration of students works best if you have JavaScript enabled

The server will ignore any columns in the CSV file that it doesn't need. The
order of the columns doesn't matter, but they must have names that _exactly_
match what the server is expecting. The page contains example data (for two
users, Ada and Charlie) so you can see what the your CSV data should look like.

You can upload a CSV file (probably the simplest way) _or_ paste the CSV data
directly. In either case, make sure your CSV data includes the header row as the
very first row.

You cannot register a student with a username that's already been registered
(you'll see an error message if this happens).


## Helpful utility for creating the CSV file

If you're running the buggy racing project as part of another module, and you're
already using an online learning platform (like Moodle, Canvas, or Blackboard)
then it's very likely you've already got a spreadsheet that contains the data
you need. The server has a utility to help you turn that into a CSV file with
the precise columns you need.

{: .navigation}
**Admin** → **Users** → **Register new students** → **Pre-registration CSV utility**

{: .warning}
You must have JavaScript enabled in your browser to use this utility

* Upload the CSV file you've got that contains the students' data
* If you have secondary CSV file, from a different source, which has additional
  columns for each student, upload that too (see details below)
* Click **Show options**

You'll see a drop-down list for every column that you need. Select the
appropriate column from the titles from the CSV file(s) you uploaded.

Click **Create CSV** to generate the CSV file. If everything was OK, you'll see
a message telling you how many users have been processed, and a button marked
**Download CSV**. Click the button to get the CSV file: you can use that to
upload to register the students on the race server, and it contains the initial
passwords the students will need to log into their new accounts.

If there were any problems, you'll see an error message telling you what's
wrong.

### What data gets added

When you select which source columns to use for each column in the final CSV
file, normally the data from the corresponding cell in your source spreadsheet
(or the secondary one) is used.

* data is always trimmed (leading and trailing spaces removed)
* the `username` is always lowercase, and any internal spaces are removed
  * if identical usernames are generated, each new one is "bumped" — you'll see
    a message telling you which usernames have been bumped in this way (you
    might want to edit them in the CSV file you download afterwards)
* for the `password` column, the default option is "Generate random" which will
  create a friendly initial password (inspired by the service of
  [DinoPass](https://www.dinopass.com) — we don't use their API directly
  because of CORS limitations)
* If the data may contain multiple words, you can choose to only use some of
  them. The data is split on space (or @-sign — which lets you pick out the
  username from an email address):
  * **all** uses all the data for that cell in the CSV
  * **first word**
  * **last word**
  * **all but last**
  * **all but first**

The select menues will auto-select the matching column from your source menu,
if there is one.


### Example: using first name as a username

Suppose you've configured your race server such that students just need a
username and password (the simplest configuration). All you've got from from
college admin is a spreadsheet with columns "Full name", "class" and "email
address". Save the spreadsheet as a CSV and upload it to the Pre-registration
CSV utility, and click **Show options**.

* for username, select **Full name** but with the second option **first word**
* for password, select **Generate random** (it will have already selected this
  for you, because the source CSV didn't have a password column)
* you're not using the class or email address columns, so just ignore them
* click **Create CSV**

The username will be the lower case first word from the "full name" column. If
this would result in identical usernames, numbers are added to make the
subsequent ones unique. For example, if there are multiple students with the
first name Ada, the generated CSV will contain `ada`, `ada2`, `ada3` and so on.
The utitilty reports which names have been "bumped" in this way so you can
review, and if necessary edit, the CSV after you've downloaded it.

We don't change `ada` to `ada1` in case this isn't the mechanism you want to
use — it's often better to use the first letter of the last name to disambiguate,
for example. So really we anticipate you resolving these usernames by hand in
the CSV afterwards — add `1` to `ada` if that's how you want to do it.

### Secondary CSV

If you've got a CSV of your enrolled students and you just want to make it
suitable for registering them, you might not need a secondary CSV. It's for the
situation where the data for students has come from two, rather than one source.
In this case, you can add a secondary spreadsheet that provides additional columns
you'll be able to pick from the drop-down menues when you select columns for
the CSV. This only works if there is a column in both source and secondary CSVs
with an identical title, and with matching values for the same student. See the
case study below for an example that demonstrates how this is useful.

If you upload a secondary CSV but the utility can't find a column to use to
join it with the main CSV, you'll see a warning message. The common column
that's being used to join the rows must have the same name in both CSVs. It
will join the rows where the data in that column, in each CSV

{: .rhul}
Our CSV of enrolled students was downloaded from Moodle. But we also needed
each student's college username (used for logging onto the CompSci department's
own Unix server), which isn't held on the Moodle. So we created a secondary
CSV, downloaded via the Unix LDAP service, containing our students' email
addresses and college usernames. Because each student's email address appeared
in both spreadsheets — and we made sure the email columns in both had the same
title — the utility could use that to join together each row (for each
student). In this way, the username column from the secondary CSV appeared in
the drop-down options, and we could choose it for our `ext_username` field
(which we call College Username).






