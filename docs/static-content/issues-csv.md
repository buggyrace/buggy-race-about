---
title: Issues CSV
layout: home
nav_order: 12
parent: Static content
has_children: false
---

# Issues CSV 

{: .navigation}
**Admin** → **Config** → **Tasks** → **Task summary CSV** → **Download... issues CSV**

{: .note}
The issues CSV described here is optional. If you're not using it you can
skip this page!

The race server produces a comma-separated values (CSV) file that describes
the project tasks as issues. This can be useful if you're encouraging your
students to use an online version control system like GitHub or GitLab, and
want to expose them to those systems' use of issues.

{: .demo}
Download the [task issues in CSV format]({{site.content.demo_url}}/project/tasks/issues.csv).


> If you're [distributing the editor code](../buggy-editor/distributing-the-code)
> with the **autofork** method (so `IS_USING_GITHUB_API_TO_INJECT_ISSUES` is
> set to `Yes`), the race server uses this CSV to automatically inject the
> issues into your students' GitHub accounts.

The most important effect of [publishing the task list](creating-tasks)
is that the current tasks, _and_ the current values of any config settings
they reference, are rendered into HTML as the task list. Students work
directly from this task list.

However, the publishing process _also_ generates an "issues CSV". The issues
CSV is effectively a static file "frozen" to be in synch with the published
task list. It is a CSV file with two columns:

* name and title
* problem description and link to the task on the race server (markdown)

You can customise (or suppress) the header row with the
`BUGGY_EDITOR_ISSUES_CSV_HEADER_ROW` config setting in the "Tasks" group
(that is, you can change what these columns are called), or accept the
default. The default values work both with the automatic injection into
GitHub described above, and also with GitLab's [import issues from CSV
feature](https://docs.gitlab.com/ee/user/project/issues/csv_import.html).

The file is available to download via the button on the tasks admin
page, but it's also publicly available on your race server at:

* `/project/tasks/issues.csv`

This might be useful if you want to automate loading of issues with an
external script.

The name of each issue matches the name of the task (of course!) and the
description, which is markdown text, includes a link to the task on your
race server's task list.

Remember that this CSV is updated whenever you publish the task list — so
if you edit any tasks, or change any config settings that they refert to,
the CSV won't reflect those changes until you re-publish the task list.
However, that the load task admin page also allows you to download the
_current_ tasks in this form, which might not be the same as the published
issues (if you have edited the tasks since you last published them).

{: .rhul }
We used the auto-injection of tasks as GitHub issues into students'
editor repos to encourage them to see how that platform uses them. Most
students didn't use them — which is fine, because it's an optional extra
and we'd chosen not to make use of Git part of the module. However, for
students who were on top of their programming, it provides an excellent
introduction into how _feature branches_ and even _closing issues from
within commit messages_ can work.
