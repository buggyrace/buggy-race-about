---
title: Environment variables
layout: home
nav_order: 5
parent: Customising
has_children: false
---


# Environment variables

<details close markdown="block">
  <summary>
    Contents of this page:
  </summary>
  {: .text-delta }
- TOC
{:toc}
</details>

## About environment variables

The race server stores nearly all of its configuration in its database. The
name of each config setting is shown when you set it (go to **Admin** →
**Config** to see all the ones you can change via the web interface). You can
change them during [the setup phase](setup-phase) or later by editing them.

However, you can also set any config setting explicitly by declaring it as an
**environment variable**. Declaring any config setting in this way **always
overrides** the current setting in the database.

When the server starts up, any config settings declared via environment
variables are written to the database, overriding any existing values for those
settings.

{: .note}
_Other than during installation,_ you might never need to do this! Normally,
you change config settings via the web interface: **Admin** → **Config**.
<br>
It is important to understand that if you declare a config setting via
an environment variable, when you start (or restart) the server, this
declaration will **always override** the value in the database. You'll see a
warning in the admin interface for any settings that have been set this way
because, if you don't remove the environment variable declaration _after_ it's
been applied, any changes you make to it in the admin interface will not persist
beyond the next restart.

{: .note}
The config setting `DATABASE_URL` is, by necessity, one that must be declared
in an environment variable (since the application uses it to connect to the
database).

There are two ways to pass environment variables like this: both require you to
have access to the server (such as during installation):

* Create a `.env` file
* Set or export environment variables explicitly

## Create a `.env` file

Any declarations in a file called `.env` in the project root directory will be
used. See the file `env.example` for some notes and examples.

If you edit this file, then restart the server, settings made here will be
written into the database. Remember to then edit the `.env` file again to
remove them so that you can — if you ever need to — subsequently change them
through the web interface.

{: .note}
The `.env` file is a hidden file on Unix (because its name starts with a `.`),
so if you're using the command line on Unix, you'll need to do `ls -al` to see
it.

## Set or export environment variables explicitly

If you export an environment variable in the process that then launches the
server, it will be picked up that way. 

### On Unix

Set environment variables with the `export` command:

```bash
export DATABASE_URL=postgresql://hamster:sque4k@localhost:5432/buggy
```

### On Windows

In general, you can find the environment variables in the **Control Panel** →
**System Advanced** → **Environment Variables**.

Windows CMD:

```bash
set DATABASE_URL=postgresql://hamster:sque4k@localhost:5432/buggy
```

Windows Powershell:

```bash
$env:DATABASE_URL=postgresql://hamster:sque4k@localhost:5432/buggy
```

### On Heroku

If you're using Heroku, you can do this through a convenient web interface. Go
to the race-server app, find **Settings** and click **Reveal config settings**.


## Important variables you must or should set

You **must** set an environment variable called `DATABASE_URL` (if you don't, the
default is an SQLite database which is _not suitable for production_):

<div class="card">
  <h3 id="database_url">
    DATABASE_URL
    <span></span>
  </h3>
  <div>
    <label>Purpose</label>
    <div>
      <p>
        This tells the server application how and where to connect to the
        database. It typically provides credentials (username and password for
        database access) and connection information.
      </p>
      <p>
        See the 
        <a href="https://docs.sqlalchemy.org/en/20/core/engines.html#database-urls">SQLAlchemy docs on Database URLs</a>
        for details.  
      </p>
    </div>
  </div>
  <div>
    <label>Heroku<br>note</label>
    <div>
      <p>
        If you are hosting your server on Heroku, this setting will be created
        for you automatically when you connect the (Postgres) database to your
        app in the Heroku admin interface. In fact, on Heroku you
        <strong>cannot</strong> edit this, which is why you might need to use
        <code>IS_REWRITING_DB_URI_PW_AS_QUERY</code> and
        <code>FORCED_DB_URI_SSL_MODE</code> if the connection is refused
        (see following entries).
      </p>
      <p>
        Incidentally, Heroku generates a URI prefixed with
        <code>postgres://</code> which is deprecated in SQLAlchemy, so the race
        server automatically rewrites this to <code>postgresql://</code>.
      </p>
    </div>
  </div>
  <div>
    <label>Example<br>values</label>
    <ul>
      <li>
        <code>postgresql://username:password@hostname:5432/buggy</code>
      </li>
      <li>
        <code>mysql+mysqlconnector://username:password@localhost:3306/buggy</code>
      </li>
    </ul>
  </div>
</div>

The following environment variables might need to be set, depending on your
installation. So, if you don't set them, and your server works: great! But if
it doesn't work, these might be what you need to try:

<div class="card">
  <h3 id="is_rewriting_db_uri_pw_as_query">
    IS_REWRITING_DB_URI_PW_AS_QUERY
    <span></span>
  </h3>
  <div>
    <label>Purpose</label>
    <div>
      <p>
        If you've set your database up correctly but Flask/SQLAlchemy fails to
        connect with an error like "<code>password authentication failed for
        user...</code>" and you're <em>sure</em> you've got the correct
        username:password in the URL, then try setting this to <code>1</code>.
      </p>
      <p>
        This works by extracting the password you've put into
        <code>DATABASE_URL</code> and passing it into the application by
        rewriting the URL with the password appended as a query variable called
        <code>password</code>.
      </p>
    </div>
  </div>
  <div>
    <label>Example<br>values</label>
    <ul>
      <li>
        <code>0</code> (to do nothing, which is the default)  
      </li>
      <li>
        <code>1</code> (to rewrite the URL)
      </li>
    </ul>
  </div>
</div>

<div class="card">
  <h3 id="forced_db_uri_ssl_mode">
    FORCED_DB_URI_SSL_MODE
    <span></span>
  </h3>
  <div>
    <label>Purpose</label>
    <div>
      <p>
        This allows you to control whether or not the database connection uses
        SSL encryption. You might need this because some connections demand it
        (for example, on Heroku), whereas on localhost (if you're a developer)
        you probably don't.
      </p>
      <p>
        This works by adding the string you specify as a query variable called
        <code>sslmode</code> to the database URL passed to SQLAlchemy.
      </p>
      <p>
        For details on the possible values, see the
        <a href="https://www.postgresql.org/docs/9.0/libpq-ssl.html#LIBPQ-SSL-SSLMODE-STATEMENTS">Postgres
          docs on SSL mode</a>.
      </p>
    </div>
  </div>
  <div>
    <label>Example<br>values</label>
    <ul>
      <li>
        <em>nothing</em> (empty string, which is the default)
      </li>
      <li>
        <code>require</code> (to force SSL connection)
      </li>
      <li>
        <code>disable</code> (if you're sure you don't want it)
      </li>
    </ul>
  </div>
</div>

<div class="card">
  <h3 id="flask_app">
    FLASK_APP
    <span></span>
  </h3>
  <div>
    <label>Purpose</label>
    <div>
      <p>
        This tells Flask where to find the Python file to run to start the
        application. You might not need to specify this because the default
        value is <em>probably</em> already what you need (although that depends
        on what the working directory is when you launch the application, which
        in turn might depend on <em>how</em> you launch it).
      </p>
    </div>
  </div>
  <div>
    <label>Example<br>values</label>
    <ul>
      <li>
        <code>buggy_race_server/app.py</code> (the default value)
      </li>
      <li>
        <code>autoapp.py</code>
      </li>
    </ul>
  </div>
</div>

<div class="card">
  <h3 id="flask_app">
    AUTHORISATION_CODE
    <span></span>
  </h3>
  <div>
    <label>Purpose</label>
    <div>
      <p>
        Normally you do not want to have <code>AUTHORISATION_CODE</code>
        declared as an environment variable. The auth code is usually stored as
        a hashed value (that is, it can't be casually read) within the database.
      </p>
      <p>
        But if you <em>need</em> to override it — because you've forgotten what
        it is or you want to not use the default value when you first run the
        server immediately after installation — you can set it with a plaintext
        value in an environment variable. Remember to remove the environment
        declaration as soon as you've changed it through the web interface
        (<strong>Admin</strong> → <strong>Config</strong> →
        <strong>Auth</strong>), otherwise it will be reset when you next
        restart the server. Avoid having the auth code stored in plaintext on
        the server except for the (brief) period before when you're initialising
        it (or resetting it) before you can set it properly.
      </p>
    </div>
  </div>
</div>


Once the application is running, you can see the database settings (with
passwords redacted) at the bottom of the **System info** page (see below).

The config setting `SQLALCHEMY_DATABASE_URI` is important, but the server
automatically generates that for you from the `DATABASE_URL` environment
variable you've provided. Do not try to set it explicitly!

{: .note}
Remember that _every one_ of the config settings you can change in the web
interface (**Admin** → **Config** → **Auth**) can be set (forced) by declaring
it as an environment variable (or in the `.env` file). Be sure to use _exactly_
the same uppercase name when you declare it.

## Environment settings are saved to the database

If you launch (or restart) the race server with any config set by environment
variables, those values will be saved in the database. That is, they _will_
persist in subsequent runs (until you edit them via **Admin** → **Config**).

When you go to edit a config entry in the web interface, you'll be warned if it
was set via an environment variable.

{: .warning}
If you leave an environment variable declaration in place in the `.env` file
after you've restarted the server, any changes to that setting made through the
web interface will be lost when you next restart the server... because this env
setting is going to override it (again). This is why it's generally best to
remove any changes you made in the `.env` file once they've been applied.


## Other "system" settings ("System info")

{: .navigation}
**Admin** → **Dashboard** → **System info**

There are some config settings that the admin **Config** interface on the race
server doesn't let you edit. You can see them by looking on the **System
information** page. Many of the config settings shown there can be declared as
environment variables if you need to change them.

Settings with names that start with an underscore (`_`) are generally ones that
we don't expect you to modify, but if you do need to change them, remember to
include the underscore when you declare them as environment variables. _Be
careful changing these settings: you can break things!_

{: .note}
Unlike changes made through the web interface, any changes you make to
environment variables won't get noticed until you restart the race server.

## Saving a config snapshot (for `.env`)

{: .navigation}
**Admin** → **Dashboard** → **System info** → **Download config snapshot**

You can save a snapshot of the current config settings as a text file, in
a format suitable for use as a `.env` file (although some editing will be
required, because some sensitive data is redacted or excluded).

This may be handy at the end of a term to archive your settings if you
anticipate running the project again the following (academic?) year... because
by then you won't remember all the things you did to get it working this time
;-) You can use it to help make a new installation based on this existing one
by using this text file as the basis for the `.env` file. This is probably more
useful than a dump of the current database, because that includes a lot of
project information (students and texts, for example) that you won't want to
carry forward into a new class, and also because there are some config settings
that aren't in the database.

{: .warning}
The config snapshot is a convenience utility that helps you archive a working
config now — it's not an alternative to proper set-up. Remember that you _must_
edit the file before deploying it as a `.env` file. For example, passwords are
redacted (database connections using passwords will fail), and timestamps
should probably be removed. Removing declarations from the `.env` file is
usually safe because missing entries will fall back to sensible default values
(which may be "nothing").


---
* Previous: [Set-up phase](setup-phase)
* Next: [Authorisation config](auth)