---
title: VCS config
layout: home
nav_order: 90
parent: Customising
has_children: false
---


# Configuring VCS (Version Control System)

{: .navigation}
**Admin** → **Config** → Config:**VCS**

The VCS settings you need will depend on how you have decided to distribute
the editor source code to students: see [more about how students get the
code](../buggy-editor/distributing-the-code).

{: .note}
The default settings do not use Git or GitHub at all — the students download a
zip file directly from the race server. But the settings that control this
behaviour are nonetheless in this VCS group, because all the alternatives do use
version control.

To see which settings are required for each distribution method, see the
individual descriptions (the settings are listed in the "Set up" section).
The Config settings interface will warn you if any of your current settings
do not match suggested values for your chosen method.

<ul>
  <li><a href="../buggy-editor/distributing-the-code#method-zip"><strong>zip</strong>: Students download a zipfile from race server</a> (the default)</li>
  <li><a href="../buggy-editor/distributing-the-code#method-page"><strong>page</strong>: Students get the source code from a custom page you set up elsewhere</a></li>
  <li><a href="../buggy-editor/distributing-the-code#method-repo"><strong>repo</strong>: Students get the source code from your repo</a></li>
  <li><a href="../buggy-editor/distributing-the-code#method-preload"><strong>preload</strong>: You preload the source code by forking repos into students’ accounts</a></li>
  <li><a href="../buggy-editor/distributing-the-code#method-fork"><strong>fork</strong>: Students manually fork your repo into their own account</a></li>
  <li><a href="../buggy-editor/distributing-the-code#method-autofork"><strong>autofork</strong>: Server forks your repo into students' GitHub accounts</a></li>
  <li><a href="../buggy-editor/distributing-the-code#method-vsremote"><strong>vsremote</strong>: Server forks your repo into students' GitHub accounts and then clones via VSCode</a></li>
</ul>


## Config settings ("VCS")

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `IS_USING_VCS` | Are you using a Version Control System (VCS) like GitHub or GitLab to distribute the source code for the buggy editor to students? If you choose `Yes` there is still quite a lot of flexibility as to how it's implemented (from simply downloading from GitHub, to manually preloading students' GitLab repos, to automatically forking via an OAuth client into GitHub accounts). If you choose `No`, the students can download a zip file from this server or your own site. See also `EDITOR_DISTRIBUTION_METHOD` in the Editor group of config settings.  <br><br> _Default value:_ `No` |
| `VCS_NAME` | If you are distributing the editor code to your students through a version control system (VCS), what is it called? GitHub is common, but you might be using a different one (for example, if you're running your own installation of GitLab). This setting is used anywhere the VCS gets mentioned in texts such as in the tasks or tech notes (which you might also edit or write yourself). This setting can be ignored if `IS_USING_VCS` is `No`. See also `EDITOR_DISTRIBUTION_METHOD` in the Editor group of config settings.  <br><br> _Default value:_ `GitHub` |
| `BUGGY_EDITOR_DOWNLOAD_URL` | If you are **not** using a VCS platform like GitHub or GitLab (`IS_USING_VCS` is `No`), your students can download the buggy editor zipfile directly from this server. If you prefer to provide your own copy instead, provide a URL to your own instructions or zipfile instead. This setting is ignored if `IS_USING_VCS` is `Yes`.   <br><br> _Default value:_ _none/empty_ |
| `BUGGY_EDITOR_ZIPFILE_NAME` | If you are **not** using a VCS platform like Github or GitLab (`IS_USING_VCS` is `No`), and want to use the default buggy editor source code served from this server, what should the zip file that students download be called?  <br><br> _Default value:_ `buggy-race-editor.zip` |
| `BUGGY_EDITOR_REPO_URL` | URL to the 'buggy editor' code the students need to start the project. This will usually be the URL to your customised, forked repo. If `IS_USING_VCS` is `No`, this setting is ignored.  <br><br> _Default value:_ `https://github.com/buggyrace/buggy-race-editor` |
| `BUGGY_EDITOR_REPO_NAME` | This should match the name in the `BUGGY_EDITOR_REPO_URL` and is used in some of the GitHub API calls: if you've forked the repo and not changed its name, you won't need to change this. If `IS_USING_VCS` is `No`, this setting is ignored.  <br><br> _Default value:_ `buggy-race-editor` |
| `BUGGY_EDITOR_REPO_OWNER` | The `BUGGY_EDITOR_REPO_URL` is public and owned by `buggyrace`. If you've forked the repo (and customised it), change this to your username on the version control platform you're using (e.g., GitHub or GitLab). It should match the username that appears in `BUGGY_EDITOR_REPO_URL`. If `IS_USING_VCS` is `No`, this setting is ignored.  <br><br> _Default value:_ `buggyrace` |
| `IS_STUDENT_USING_REPO` | Should students fork the buggy editor repo into their own (version controlled) repo? Choose `No` if your students are not using a VCS (such as GitHub or GitLab). If you choose yes, remember to set `VCS_NAME` to match whichever such system you are using. This setting must align with what you've chosen for `EDITOR_DISTRIBUTION_METHOD` in the Editor group of config settings. This setting is used to ensure that the instructions students see on the race server match how you're running the project, and is ignored if `IS_USING_VCS` is `No`.  <br><br> _Default value:_ `No` |
| `STUDENT_EDITOR_REPO_DOMAIN` | The base URL to the version control site where the students' own buggy editor repos end up (for example, if they are cloned). This may well be the same base domain that's in `BUGGY_EDITOR_REPO_URL` (it should probably relate to `VCS_NAME` too). This is used to construct links from the race server to their repo by using their (VCS) username and editor repo name. This setting is ignored if `IS_STUDENT_USING_REPO` is `No`.  <br><br> _Default value:_ `https://github.com/` |
| `IS_USING_GITHUB_API_TO_FORK` | If students must work with the buggy editor in their own GitHub repo, the race server can help by automatically forking it for them, using the GitHub API. You must configure the `GITHUB_CLIENT_ID` and `GITHUB_CLIENT_SECRET` for this to work (and `IS_USING_VCS` and `IS_STUDENT_USING_REPO` must both be `Yes`). See also `EDITOR_DISTRIBUTION_METHOD` in the Editor group of config settings.  <br><br> _Default value:_ `No` |
| `IS_USING_GITHUB_API_TO_INJECT_ISSUES` | If you have set the race server to use GitHub's API to fork the buggy editor repo into each student's account, it will also also inject the tasks as GitHub issues into their repo unless you prevent it here. This setting is ignored unless both `IS_USING_VCS` and `IS_USING_GITHUB_API_TO_FORK` are both set to `Yes`.   <br><br> _Default value:_ `Yes` |
| `GITHUB_CLIENT_ID` | The GitHub client ID for the GitHub app that the server uses to fork the buggy editor repo into a student's own GitHub account.  <br><br> _Default value:_ _none/empty_ |
| `GITHUB_CLIENT_SECRET` | A string that exactly matches the client secret stored on the GitHub app that the server uses to fork the buggy editor repo into a student's own GitHub account. You only need this if `IS_USING_GITHUB_API_TO_FORK` is `Yes`.  <br><br> _Default value:_ _none/empty_ |


 ---
 * Previous: [Races config](races)
 * Next: [Creating the tasks](creating-tasks)

