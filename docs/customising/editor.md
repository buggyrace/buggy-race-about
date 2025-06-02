---
title: Editor config
layout: home
nav_order: 60
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




















## Config settings ("Editor")

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `EDITOR_DOWNLOAD_URL` | If you are not distributing the buggy editor code through a version control system, and they aren&#39;t downloading a it as a zip from the race server, what URL should they use instead? This setting is ignored if `EDITOR_DISTRIBUTION_METHOD` is not `zip`, `page`, or `other`.   <br/><br/> _Default value:_ _none/empty_ |
| `EDITOR_ZIPFILE_NAME` | If you want your students to use the default buggy editor source code served from this server (and not, for example, via a version control system), what should the zip file that students download be called? This setting is ignored unless `EDITOR_DISTRIBUTION_METHOD` is `zip`.   <br/><br/> _Default value:_ `buggy-race-editor.zip` |
| `EDITOR_HOST` | The default host that the students&#39; buggy editors use. Make sure this matches the `host` argument that the editor app is launched with (at the bottom of the editor `app.py`). This may appear in the task and tech notes, and (if you&#39;re distributing the editor source code via static zip file from this server) will be written into the `app.py` file too.  <br/><br/> _Default value:_ `localhost` |
| `EDITOR_PORT` | The default port that the students&#39; buggy editors use. Make sure this matches the `port` argument that the editor app is launched with (at the bottom of the editor `app.py`). This may appear in the task and tech notes, and (if you&#39;re distributing the editor source code via static zip file from this server) will be written into the `app.py` file too.  <br/><br/> _Default value:_ `5000` |
| `IS_WRITING_HOST_IN_EDITOR` | If you publish the buggy editor app (as a zipfile) on this server, should the `EDITOR_HOST` value be hardcoded into `app.py`? Usually, you do not want to do this, because `0.0.0.0` is going to map to the localhost anyway. This setting is only used when you generate the zip file on the race server, which you&#39;ll probably only do if `EDITOR_DISTRIBUTION_METHOD` is `zip`.  <br/><br/> _Default value:_ `No` |
| `IS_WRITING_PORT_IN_EDITOR` | If you publish the buggy editor app (as a zipfile) on this server, should the `EDITOR_PORT` value be hardcoded into `app.py`? This setting is only used when you generate the zip file on the race server, which you&#39;ll probably only do if `EDITOR_DISTRIBUTION_METHOD` is `zip`.  <br/><br/> _Default value:_ `Yes` |
| `IS_WRITING_SERVER_URL_IN_EDITOR` | If you publish the buggy editor app on this server, should the `BUGGY_RACE_SERVER_URL` be written into `app.py`? This setting won&#39;t be used if you don&#39;t generate the zipfile on this server (for example, if `IS_USING_VCS` is `Yes`) but remember you or your students do need to change it inside the buggy editor source code eventually.  <br/><br/> _Default value:_ `Yes` |

  
---

* Previous: [Project config](project)
* Next: [Tasks config](tasks)
