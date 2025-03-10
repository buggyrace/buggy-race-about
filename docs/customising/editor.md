---
title: Editor config
layout: home
nav_order: 65
parent: Customising
has_children: false
---


# Configuring the editor

{: .navigation}
**Admin** → **Config** → Config:**Editor**

Editor config settings control _how_ the Buggy Editor (which is the webapp that
each student develops) is managed.

The `EDITOR_DISTRIBUTION_METHOD` setting is critical to how your students start
your project: see [more details about distributing the code](buggy-editor/distributing-the-code).

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `EDITOR_DISTRIBUTION_METHOD` | How do your students get the Buggy Editor source code at the start of the project? During set-up, choosing this setting affects some of the other settings in subsequent groups.  <br><br> _Default value:_ `zip` |
| `EDITOR_HOST` | The default host that the students' buggy editors use. Make sure this matches the `host` argument that the editor app is launched with (at the bottom of the editor `app.py`). This may appear in the task and tech notes, and (if you're distributing the editor source code via static zip file from this server) will be written into the `app.py` file too.  <br><br> _Default value:_ `0.0.0.0` |
| `EDITOR_PORT` | The default port that the students' buggy editors use. Make sure this matches the `port` argument that the editor app is launched with (at the bottom of the editor `app.py`). This may appear in the task and tech notes, and (if you're distributing the editor source code via static zip file from this server) will be written into the `app.py` file too.  <br><br> _Default value:_ `5000` |
| `IS_WRITING_HOST_AND_PORT_IN_EDITOR` | If you publish the buggy editor app on this server, should the `EDITOR_HOST` and `EDITOR_PORT` values be written into `app.py`? This setting won't be used if you don't generate the zipfile on this server (for example, if `IS_USING_VCS` is `Yes`).  <br><br> _Default value:_ `Yes` |
| `IS_WRITING_SERVER_URL_IN_EDITOR` | If you publish the buggy editor app on this server, should the `BUGGY_RACE_SERVER_URL` be written into `app.py`? This setting won't be used if you don't generate the zipfile on this server (for example, if `IS_USING_VCS` is `Yes`) but remember you or your students do need to change it inside the buggy editor source code eventually.  <br><br> _Default value:_ `Yes` |

