---
title: Remote config
layout: home
nav_order: 120
parent: Customising
has_children: false
---


# Configuring the remote server

{: .navigation}
**Admin** → **Config** → Config:**Remote**

These are settings that you only need if you've set
`EDITOR_DISTRIBUTION_METHOD` to `vsremote` (because it needs extra
config). This requires an SSH tunnel between the students' VSCode
workspace and a remote server. If you're using any other method,
including the default, these settings will be ignored.

## Config settings ("Remote")

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `IS_USING_REMOTE_VS_WORKSPACE` | If your students will be using a remote server (see: `PROJECT_REMOTE_SERVER_NAME`) and are running VS Code over a remote session, the race server can produce a VS Code workspace file to facilitate cloning the repo onto that server and subsequently access it through VS Code. This is quite a specific setup: if you're not sure, you almost certainly do not want this.   <br><br> _Default value:_ `No` |
| `PROJECT_REMOTE_SERVER_ADDRESS` | If students are going to develop on a remote server, what is its address? This is used with their external username (or just username, if they haven't got one): for example enter `linux.example.ac.uk` so student Ada can log in via `ada@linux.example.ac.uk`. If you're not using a remote project server, leave this blank (see also `PROJECT_REMOTE_SERVER_NAME`).  <br><br> _Default value:_ _none/empty_ |
| `PROJECT_REMOTE_SERVER_NAME` | If students are going to develop on a remote server, what is its (human-facing) name? This is used to help students identify the server they are logging into (e.g, "the CompSci department's Unix server"). Leave this blank if your students are all working on their own machines (i.e., not a single teaching server with login accounts, python, and personalised HTTP ports).  <br><br> _Default value:_ _none/empty_ |
| `PROJECT_REMOTE_SERVER_APP_URL` | If students are going to develop on a remote server, what is the URL then need to hit in their browser to see their app? Presumably it will have a custom port on the end too. If you're not using a remote project server, leave this blank.  <br><br> _Default value:_ _none/empty_ |


---
* Previous: [Authorisation config](auth)
* Next: [Organisation config](org)