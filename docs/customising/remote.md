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

These are settings that only matter if you've set `EDITOR_DISTRIBUTION_METHOD`
to `vsremote` in the "Projects" group.

_Most installations don't need these settings, so you can usually skip them!_

The `vsremote` distribution is the most compex set-up we've tried, and uses
an SSH tunnel between the students' VSCode workspace and a remote server. See
more about [distributing the code](../buggy-editor/distributing-the-code).


















## Config settings ("Remote")

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `IS_USING_REMOTE_VS_WORKSPACE` | If your students will be using a remote server (see: `PROJECT_REMOTE_SERVER_NAME`) and are running VS Code over a remote session, the race server can produce a VS Code workspace file to facilitate cloning the repo onto that server and subsequently access it through VS Code. This is quite a specific setup: if you&#39;re not sure, you almost certainly do not want this.   <br/><br/> _Default value:_ `No` |
| `PROJECT_REMOTE_SERVER_ADDRESS` | If students are going to develop on a remote server, what is its address? This is used with their external username (or just username, if they haven&#39;t got one): for example enter `linux.example.ac.uk` so student Ada can log in via `ada@linux.example.ac.uk`. If you&#39;re not using a remote project server, leave this blank (see also `PROJECT_REMOTE_SERVER_NAME`).  <br/><br/> _Default value:_ _none/empty_ |
| `PROJECT_REMOTE_SERVER_NAME` | If students are going to develop on a remote server, what is its (human-facing) name? This is used to help students identify the server they are logging into (e.g, &#34;the CompSci department&#39;s Unix server&#34;). Leave this blank if your students are all working on their own machines (i.e., not a single teaching server with login accounts, python, and personalised HTTP ports).  <br/><br/> _Default value:_ _none/empty_ |
| `PROJECT_REMOTE_SERVER_APP_URL` | If students are going to develop on a remote server, what is the URL then need to hit in their browser to see their app? Presumably it will have a custom port on the end too. If you&#39;re not using a remote project server, leave this blank.  <br/><br/> _Default value:_ _none/empty_ |

  
---
* Previous: [VCS config](vcs)
* Next: [Tech notes config](tech-notes)