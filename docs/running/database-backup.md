---
title: Database backups
layout: home
nav_order: 60
parent: Day-to-day running
---

# Backing up the database

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
> them to edit (of course) **and delete** their own texts as well as add them.
> 
> The server does _not_ keep an audit trail of edits to the texts, but if you're
> taking nightly backups then it is at least feasible that you could recover
> lost work from previous days for a distraught student. You'd probably need
> to load the SQL into a standalone database to extract the lost data, and it
> will be fiddly. There is an
> [open enhancement issue (#181)](https://github.com/buggyrace/buggy-race-server/issues/181)
> to implement a more convenient way to get old task texts back into the
> database.

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


## Static content backup

If you have a backup of the database, you don't _need_ to maintain a backup of
the static content (which you can find in the `published` directory on your
server) because you can regenerate all of those files if the database. The
database backup will include all your config settings, except the
`DATABASE_URL` setting that's [set as an environment
variable](../customising/env).

