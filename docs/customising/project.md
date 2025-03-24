---
title: Project config
layout: home
nav_order: 50
parent: Customising
has_children: false
---


# Configuring the project

{: .navigation}
**Admin** → **Config** → Config:**Project**

Project config settings control _how_ you're running the project from an
academic point of view.

This is also where you specify the `EDITOR_DISTRIBUTION_METHOD`, which controls
how your students get their copy of the buggy editor (the source code they are
going to develop). This affects what settings you must choose in other groups,
so is a critical setting. For more about this, see
[distributing the editor code](../buggy-editor/distributing-the-code).

Config settings for the tasks — which are fundamental to how your project works
— are in a separate group: see the [task config settings](tasks) instead.
There's also a separate page about
[managing the task-list](../static-content/task-list).

You can choose whether or not you require students to create a report and/or
a poster as part of the project: see
[the students' report and poster](../teaching/report-and-poster) for details.

## Config settings ("Project")

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `EDITOR_DISTRIBUTION_METHOD` | How do your students get the Buggy Editor source code at the start of the project? During set-up, choosing this setting affects some of the other settings in subsequent groups.  <br><br> _Default value:_ `zip` |
| `PROJECT_REPORT_TYPE` | If you require students to produce a report of how they tackled the tasks, indicate that here. Choose `document` if you want students to make a document, or `in editor` if the report takes the form of an additional webpage in the student's buggy editor webserver. If you choose `No report`, all mentions will be removed: see also the `IS_STORING_STUDENT_TASK_TEXTS` setting in the **Tasks** group of settings.   <br><br> _Default value:_ `in editor` |
| `PROJECT_REPORT_URL` | The race server will display a basic page of instructions about the report (which is especially helpful if `PROJECT_REPORT_TYPE` is `In editor`), but if you prefer to direct students to a custom page, provide a URL to use insteead. This setting is ignored if `PROJECT_REPORT_TYPE` is `No report`.  <br><br> _Default value:_ _none/empty_ |
| `PROJECT_POSTER_TYPE` | Do you require students to produce a poster proclaiming the features of their editor? If it's `top of report` or `bottom of report` this means it's part of the report (so `PROJECT_REPORT_TYPE` must not be `No report`). Choose `in editor` if the report takes the form of an additional webpage in the student's buggy editor webserver. If you choose `No poster`, all mentions will be removed.  <br><br> _Default value:_ `in editor` |
| `PROJECT_POSTER_URL` | The race server will display a basic page of instructions about the poster (which is especially helpful if `PROJECT_POSTER_TYPE` is `In editor`), but if you prefer to direct students to a custom page, provide a URL to use insteead. This setting is ignored if `PROJECT_POSTER_TYPE` is `No poster`.  <br><br> _Default value:_ _none/empty_ |
| `PROJECT_SUBMISSION_DEADLINE` | If you require all students to submit their projects on a specific deadline, set it here. This is displayed prominently (if the project is enabled) on the project page, but isn't currently used by the server for anything else. Avoid using 00:00 as a time because it confuses students — 23:59 is clearer (and 16:00 is healthier). Leave blank if you don't want to display a deadline at all (remember you can also use Announcements).  <br><br> _Default value:_ _none/empty_ |
| `PROJECT_CODE` | If this project is known by a course or module code, use it (for example, when we ran it at Royal Holloway, it was CS1999). See also `PROJECT_SLUG` which is how this code may appear in filenames of any downloaded files, if you need it to be different. The full name of the project is "the `PROJECT_CODE` Buggy Racing project", so if you don't have or need a course code, it's fine to leave it blank.  <br><br> _Default value:_ _none/empty_ |
| `PROJECT_SLUG` | This is how the `PROJECT_CODE` appears — as a prefix — in any filenames that are downloaded from the server. This is a kindness to help disambiguate files in your Downloads folder. If you leave this blank, it will default to using an automatic "slugged" version of your project code, if any. Note that there are some places where students can download files (e.g., tabulated specification data) too, so it's not just admin staff who will see it.  <br><br> _Default value:_ _none/empty_ |
| `PROJECT_SUBMISSION_LINK` | Provide a link to either the web page where you'll be accepting submissions (presumably zip files) or else a page containing clear instructions for the students to follow. The buggy race server does not handle submissions itself. By default, no submission information is provided (because it's very dependent on each institution), which means no link is displayed: so you must supply one yourself.  <br><br> _Default value:_ _none/empty_ |
| `IS_PROJECT_ZIP_INFO_DISPLAYED` | Typically, students are expected to submit their projects as a zip file containing the buggy editor web app (including a report/poster, if you've enabled it). The project page will display general information about those files (e.g., they should have the student's name just in case your submission process doesn't capture that: you end up with a lot of zip files with the same name otherwise). Use this setting to display or hide this general information on the "project" page. If set to `Yes`, remember to check that the text that appears on the project page does indeed make sense to students.  <br><br> _Default value:_ `Yes` |
| `PROJECT_ZIP_NAME_TYPE` | Normally the suggested filename for submissions (the students' zip file) is their username + `.zip`. But if you prefer your students to use an external username or ID, you can suggest it here. If you pick a type that users don't have, it will fall back to `username` (because all users have one). This setting is ignored if `IS_PROJECT_ZIP_INFO_DISPLAYED` is `No`.  <br><br> _Default value:_ `username` |
| `IS_SHOWING_PROJECT_WORKFLOW` | It can be helpful for students to have a summary of the workflow process. If you set `IS_SHOWING_PROJECT_WORKFLOW` to `Yes` then the server will show either the default workflow page, or an external one if you specify `PROJECT_WORKFLOW_URL`. If you do choose to display the workflow page, when it's published take a moment to read it to confirm it matches what you expect your students to do.  <br><br> _Default value:_ `No` |
| `PROJECT_WORKFLOW_URL` | You can replace the default workflow page with a redirection to one you've customised (and hosted elsewhere). If you leave this setting blank, the default page will be shown. In either case, this setting is ignored if `IS_SHOWING_PROJECT_WORKFLOW` is `No`.  <br><br> _Default value:_ _none/empty_ |


---

* Previous: [External links config](links)
* Next: [Editor config](editor)
