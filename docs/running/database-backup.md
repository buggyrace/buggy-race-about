---
title: Database backups
layout: home
nav_order: 60
parent: Day-to-day running
---

# Backing up the database

<details close markdown="block">
  <summary>
    Contents of this page:
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

{: .note}
The race server does **not** provide a backup mechanism. This page encourages
you to consider implementing regular (nightly?) backups, but it can't tell you
how: that depends on how your system is set up.  
<br>
Similarly, there is not currently a mechanism for _partially_ loading recovered
data from a backup. Nonetheless, in the event of a data loss, having a backup is
always better than not having a backup.

If you're hosting the race server yourself, you should investigate what
backups are being taken by your tech team (if there is one).

It's a good idea to take a backup of the SQL database in anticipation of two
kinds of event:

* Catastrophic technical failure
* Accidental (or otherwise) loss of student task text data

> ### Catastrophic technical failure
> 
> If you're unlucky and you have a hardware failure or some other event that
> loses your database, you'll need a backup to re-populate the database when you
> rebuild the server. Of course, the more frequently you take the backups, the
> less likely you will be to have lost much work.
> 
> ### Accidental (or otherwise) loss of student data
> 
> If you have set `IS_STORING_STUDENT_TASK_TEXTS` to `Yes` (in the "Tasks" group
> of config settings), then students who have been accumulating their task texts
> on the server are at risk of losing them, because the interface _does_ allow
> them to edit (of course) and therefore delete their own texts.
> 
> The server does _not_ keep an audit trail of edits to the texts, but if you're
> taking nightly backups then it is at least feasible that you could recover
> lost work from previous days for a distraught student. There's a utility to
> support you, but it presupposes you can load the backup into a local copy
> of a race server in order to extract them. See
> [Recovering texts](recovering-texts) for details.

## Example backup script: with Docker

If you have access to your server (for example, if you're running it within a
virtual machine) then a script like this can be run as a
[cronjob](https://en.wikipedia.org/wiki/Cron) on that VM to create timestamped
nightly zipped backups. It's executing the PostgreSQL `pg_dump` command using
Docker's `exec` command targeted at the database container (in this example,
that's called `server-db-1`).

Replace the names in the script with values that match your local installation!

```bash
#!/bin/bash

# This script is run regularly by a cron job to make backups for the Buggy Race
# Database. Proceed with caution.

# Define the container name
container_name="server-db-1"

# Define the database and backup details
database_username="buggy"
database_name="buggy_race"
backup_dir="/buggy/server/db/backups"
backup_filename="buggy_race_bk_$(date +\%Y\%m\%d).sql.gz"

# Run the command
/usr/bin/docker exec -t $container_name pg_dump -U $database_username $database_name | /usr/bin/gzip > $backup_dir/$backup_filename
```

## Heroku backups

If you're [hosting on Heroku](../hosting/heroku), then currently you can
schedule nightly backups of the _whole_ PostgreSQL database. See
[Heroku's backup documentation](https://devcenter.heroku.com/articles/heroku-postgres-backups).

You'll need to know the name of your app and possibly that of its database too
(`APP_NAME` and `DATABASE_ID` in the examples below). The app name is clearly
displayed when you log into your Heroku account. The database ID is shown as
the name of the Heroku PostgreSQL "Add-on", and will look something like
`postrgresql-banana-123`.

If you don't provide a database ID, Heroku should use your app's default
database by inspecting the `DATABASE_URL` you're using.

To schedule nightly backups (e.g., at 3am every night in the UK), do this:

```
heroku pg:backups:schedule DATABASE_ID --at "03:00 Europe/London" --app APP_NAME
Scheduling automatic daily backups of DATABASE_ID at 03:00 Europe/London... done
```

To get information on the backups you've got:

    heroku pg:backups --app APP_NAME

To download the latest backup:

    heroku pg:backups:download --app APP_NAME

The file this pulls down is in PostgreSQL's binary dump format. You can convert
it into SQL text (such as an SQL file) using
[`pg_restore`](https://www.postgresql.org/docs/current/app-pgrestore.html):

    pg_restore latest.dump -f - > sql_statements.sql

Be sure to check Heroku's information about how long backups are retained up on
their servers.

If you're storing personal data in your database (for example, GitHub
credentials or even email addresses) you need to handle your local backups just
as securely locally as you do up on Heroku. See also the information about
[privacy considerations on the race server](../hosting/privacy).

## Static content backup

If you have a backup of the database, you don't _need_ to maintain a backup of
the static content (which you can find in the `published` directory on your
server) because you can regenerate all of those files from the database. The
database backup will include all your config settings, except the
`DATABASE_URL` setting that's [set as an environment
variable](../customising/env).

## Configuration snapshot

You can save a snapshot of the current configuration settings (in the form of
a text file which can be reused as a `.env` file) — see
[saving a config snapshot](../customising/env#saving-a-config-snapshot-for-env).


