---
title: Running remotely through VSCode
layout: home
nav_order: 60
parent: Buggy editor
has_children: false
---


# Running on a remote server through VSCode


This is the most specific way for the students to run their editor app — it's
also by far the most complicated. It requires students to install
[Visual Studio Code](https://code.visualstudio.com) (VSCode) on the machine
they are going to be working on.

{: .note}
This mechanism allows you to host student's buggy editors on your institution's
own server. Only do this if you have the infrastructure and technical support
to run it — otherwise, it's probably easier to [run locally](running-local)
or in the cloud ([run on PythonAnywhere](running-pythonanywhere) or
[run on Replit](running-replit)).

First the editor repo is forked to each student's GitHub repo. Then a VSCode
workspace file is prepared (once the fork has been done) which can clone _that_
repo into the student's account on the remote server. The remote server must
be set up such that each student has an individual port number assigned. The
remote server uses these port numbers so that each web app can be accessed
uniquely.

{: .rhul}
This is the set-up we used _after_ the first two years of running the project
with students developing on their own machines (or in the cloud on Replit).
The advantage of this mechanism, which forces the students to work on the 
college server (at least to start with), is that we could be certain that all
students' environments were the same. It also allowed us to exploit the
VNC-based session sharing that was in place — so we could remotely support
students which isn't possible on their own, private machines. Finally having
access to the students' dev environment does mean it's possible to check on the
actual progress they are making in their code.

## Technical overview

For this mechanism, the **remote server** is something like a college teaching
server that accepts student logins — with a file system, a command-line shell,
and Python3 installed.

The remote server has Python3 installed, and assigns a unique port number to
each student that the Flask app can use. This is set as an environment variable
in each student's profile, with a name like `BUGGY_EDITOR_PORT`.

The VSCode workspace file connects to the remote server by ssh, logging into the
student's account (it prompts for their password). It then clones the student's
editor repo from their GitHub account into their home directory on the remote
server. An SSH tunnel is set up through the race server so that when the editor
(`app.py`) is run, it is bound with the unique port number to `0.0.0.0` (or
`localhost`, depending on local setup) on the student's local machine.

The student is required to enter their (remote server) password
in a couple more places during the set-up process.

The net effect is that — while VSCode is running, and the ssh tunnel is in
operation, the remote terminal (inside VSCode) can be used to run the Python
app on the remote server, while the buggy editor can be seen in the browser
locally.

The per-student port numbers are allocated as environment variables in each
student's profile on the server. If the environment variable is called
`BUGGY_EDITOR_PORT`, then the editor's `app.py` should be modified, replacing
the code that launches the app (`app.run())` at the bottom with this:

```python
if __name__ == '__main__':
    alloc_port = os.environ.get('BUGGY_EDITOR_PORT') or 5000
    app.run(debug=True, host="0.0.0.0", port=alloc_port)
```

See details on how to [customise the buggy editor](customising)
before sharing it with the students.


## Config settings required

{: .navigation}
**Admin** → **Config** → Config:**Project**

| Config setting                  | Value                                    |
|---------------------------------|------------------------------------------|
| `IS_STUDENT_USING_GITHUB_REPO`  | `Yes`                                    |
| `IS_USING_GITHUB_API_TO_FORK`   | `Yes` (the VSCode workspace file needs the GitHub details from this automatic fork process) |
| `IS_USING_REMOTE_VS_WORKSPACE`  | `Yes`                                    |
| `PROJECT_REMOTE_SERVER_ADDRESS` | The address of the remote server         |
| `PROJECT_REMOTE_SERVER_NAME`    | The name of remote server                |
| `PROJECT_REMOTE_SERVER_APP_URL` | The URL to hit in the browser to see the editor (without the individual port number) |

The server address is combined with the students' `ext_username` (or just
`username` if they don't have external usernames): for example use the address
`linux.example.ac.uk` if student Ada should log in via
`ada@linux.example.ac.uk`. The server name is used to disambiguate this server
in the instructions to the student (inside the VSCode workspace file, which
issues the commands and hence the password prompts).


## Student steps for using the VS Code workspace file

The process the students need to follow to enable this is as follows:

Once they have cloned the buggy editor into their own GitHub repo using the
automatic process, the server presents a **Download VSCode workspace** button
(this on the `/settings` path on the race server).

{: .suggest}
You can [add an announcement](../running/announcements) that appears next to
the VSCode workspace download button to help guide students to the instructions
(for example, put the instructions into the `GET-0` task's solution text, and
then link to it in the `get-editor` announcement).

* Download the VSCode workspace file (which has been customised with
  their own details — this is why it cannot happen until the editor repo has
  been forked into their own GitHub account)

* Install [Visual Studio Code (VSCode)](https://code.visualstudio.com)

* Open the workspace file using VSCode, and accept invitation to load any
  necessary plugins and packages

* Open **Terminal** tab in VSCode, click on **Run task**, and choose the one
  starting with `git clone https://github.com`

* At this point, the SSH tunnel is established. In the terminal, `cd` into the
  cloned repo's director, and run  
  `python app.py`

* The buggy editor can now be accessed in the local browser (the terminal output
  indicates the URL and, significantly, the port number to use).


---
* Previous: [Running on Replit](running-replit)
