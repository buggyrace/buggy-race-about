---
title: GitHub config
layout: home
nav_order: 90
parent: Customising
has_children: false
---


# Configuring GitHub

{: .navigation}
**Admin** → **Config** → Config:**GitHub**

The GitHub settings you need will depend on how you have decided to distribute
the editor source code to students: see [more about how students get the
code](../buggy-editor/distributing-the-code).

{: .note}
The default settings do not use Git or GitHub at all — the students download a
zip file directly from the race server. But the settings that control this
behaviour are all in this "GitHub" group.

To see which settings are required for each distribution method, see the
individual descriptions (the settings are listed in the "Set up" section):

<ol class="upper-alpha">
  <li><a href="../buggy-editor/distributing-the-code#method-a">Students download a zipfile from race server</a> (the default)</li>
  <li><a href="../buggy-editor/distributing-the-code#method-b">Students get the source code from a custom page you set up elsewhere</a></li>
  <li><a href="../buggy-editor/distributing-the-code#method-c">Students get the source code from your repo</a></li>
  <li><a href="../buggy-editor/distributing-the-code#method-d">Students manually fork your repo into their own account</a></li>
  <li><a href="../buggy-editor/distributing-the-code#method-e">Server forks your repo into students' GitHub accounts</a></li>
  <li><a href="../buggy-editor/distributing-the-code#method-f">Server forks your repo into students' GitHub accounts and then clones via VSCode</a></li>
</ol>


## Config settings ("GitHub")

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `IS_USING_GITHUB` | Are you using GitHub to distribute the source code for the buggy editor to students? If you choose `Yes` there is still quite a lot of flexibility as to how it's implemented (from simply downloading from GitHub to automatically forking it into their GitHub account). If you choose `No`, the students can download a zip file from this server (or you can override this with your own copy).  <br><br> _Default value:_ `No` |
| `BUGGY_EDITOR_DOWNLOAD_URL` | If you are **not** using GitHub (`IS_USING_GITHUB` is `No`), your students can download the buggy editor zipfile from this server. If you prefer to provide your own copy instead, provide a URL to your own instructions or zipfile instead. This setting is ignored if `IS_USING_GITHUB` is `Yes`.   <br><br> _Default value:_ _none/empty_ |
| `BUGGY_EDITOR_ZIPFILE_NAME` | If you are **not** using GitHub (`IS_USING_GITHUB` is `No`), and want to use the default buggy editor source code served from this server, what is the name of the zip file?  <br><br> _Default value:_ `buggy-race-editor.zip` |
| `BUGGY_EDITOR_GITHUB_URL` | URL to the 'buggy editor' code the students need to start the project. This is a public repo and unless you've forked it to make a custom one, you probably don't need to change this.  <br><br> _Default value:_ `https://github.com/buggyrace/buggy-race-editor` |
| `BUGGY_EDITOR_REPO_NAME` | This should match the name in the `BUGGY_EDITOR_GITHUB_URL` and is used in some of the GitHub API calls: if you haven't changed the repo URL then you won't need to change this.  <br><br> _Default value:_ `buggy-race-editor` |
| `BUGGY_EDITOR_REPO_OWNER` | The `BUGGY_EDITOR_GITHUB_URL` is public and owned by `buggyrace`. You don't need to change this unless you've forked your own custom version of the repo.  <br><br> _Default value:_ `buggyrace` |
| `IS_STUDENT_USING_GITHUB_REPO` | Should students fork the buggy editor repo into their own GitHub repo? Choose `No` if your students are not using GitHub. If you choose `Yes`, make sure you've set `IS_USING_GITHUB_API_TO_FORK` if you want this to be automated via the race server.  <br><br> _Default value:_ `Yes` |
| `IS_USING_GITHUB_API_TO_FORK` | If students must work with the buggy editor in their own GitHub repo, the race server can help by automatically forking it for them, using the GitHub API. You must configure the `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET` for this to work (and `IS_STUDENT_USING_GITHUB_REPO`. must be `Yes`).  <br><br> _Default value:_ `No` |
| `IS_USING_GITHUB_API_TO_INJECT_ISSUES` | If you have set the race server to use GitHub's API to fork the buggy editor repo into each student's account, it will also also inject the tasks as GitHub issues into their repo unless you prevent it here. This setting is ignored if `IS_USING_GITHUB_API_TO_FORK` is set to `No`.   <br><br> _Default value:_ `Yes` |
| `GITHUB_CLIENT_ID` | The GitHub client ID for the GitHub app that the server uses to fork the buggy editor repo into a student's own GitHub account.  <br><br> _Default value:_ _none/empty_ |
| `GITHUB_CLIENT_SECRET` | A string that exactly matches the client secret stored on the GitHub app that the server uses to fork the buggy editor repo into a student's own GitHub account.  <br><br> _Default value:_ _none/empty_ |


 ---
 * Previous: [Races config](races)
 * Next: [Creating the tasks](creating-tasks)