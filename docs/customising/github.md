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
code](../buggy-editor/getting-the-code)

By default, the editor repo is _not_ forked into students' accounts
automatically. If you've decided that your students will be required to use
GitHub, this automation can be very helpful — but remember that you'll also
need to configure the OAuth app on GitHub to make this work.



## Config settings ("GitHub")

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `BUGGY_EDITOR_GITHUB_URL` | URL to the 'buggy editor' code the students need to start the project. This is a public repo and unless you've forked it to make a custom one, you probably don't need to change this.  <br><br> _Default value:_ `https://github.com/buggyrace/buggy-race-editor` |
| `BUGGY_EDITOR_REPO_NAME` | This should match the name in the `BUGGY_EDITOR_GITHUB_URL` and is used in some of the GitHub API calls: if you haven't changed the repo URL then you won't need to change this.  <br><br> _Default value:_ `buggy-race-editor` |
| `BUGGY_EDITOR_REPO_OWNER` | The `BUGGY_EDITOR_GITHUB_URL` is public and owned by `buggyrace`. You don't need to change this unless you've forked your own custom version of the repo.  <br><br> _Default value:_ `buggyrace` |
| `IS_STUDENT_USING_GITHUB_REPO` | Should students fork the buggy editor repo into their own GitHub repo? Choose `No` if your students are not using GitHub. If you choose `Yes`, make sure you've set `IS_USING_GITHUB_API_TO_FORK` if you want this to be automated via the race server.  <br><br> _Default value:_ `Yes` |
| `IS_USING_GITHUB_API_TO_FORK` | If students must work with the buggy editor in their own GitHub repo, the race server can help by automatically forking it for them, using the GitHub API. You must configure the `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET` for this to work (and `IS_STUDENT_USING_GITHUB_REPO`. must be `Yes`).  <br><br> _Default value:_ `No` |
| `IS_USING_GITHUB_API_TO_INJECT_ISSUES` | If you have set the race server to use GitHub's API to fork the buggy editor repo into each student's account, it will also also inject the tasks as GitHub issues into their repo unless you prevent it here. This setting is ignored if `IS_USING_GITHUB_API_TO_FORK` is set to `No`.   <br><br> _Default value:_ `Yes` |
| `GITHUB_CLIENT_ID` | The GitHub client ID for the GitHub app that the server uses to fork the buggy editor repo into a student's own GitHub account.  <br><br> _Default value:_ _none/empty_ |
| `GITHUB_CLIENT_SECRET` | A string that exactly matches the client secret stored on the GitHub app that the server uses tofork the buggy editor repo into a student's own GitHub account.  <br><br> _Default value:_ _none/empty_ |


      