---
title: Project config
layout: home
nav_order: 60
parent: Customising
has_children: false
---


# Configuring the project

{: .navigation}
**Admin** → **Config** → Config:**Project**

Project config settings control _how_ you're running the project from an
academic point of view.

Config settings for the tasks — which are fundamental to how your project works
— are in a separate group: see the [task config settings](tasks) instead.
There's also a separate page about
[managing the task-list](../static-content/task-list).

You can choose whether or not you require students to create a report as part
of the project: see [the students' report](../teaching/the-report) for details.
If you're setting the `PROJECT_REPORT_TYPE` manually, the only recognised
values are nothing (empty string), `report` or `poster`.


## Config settings ("Project")

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `PROJECT_REPORT_TYPE` | If you require students to include a report of how they tackled the tasks, indicate that here ("report" or "poster" are just different names for the same thing, due to an historic anomaly). The report takes the form of an additional webpage in the student's buggy editor webserver. If you choose `No report`, all mentions will be removed: see also the `IS_STORING_STUDENT_TASK_TEXTS` setting in the **Tasks** group of settings.   <br><br> _Default value:_ `report` |
| `PROJECT_SUBMISSION_DEADLINE` | If you require all students to submit their projects on a specific deadline, set it here. This is displayed prominently (if the project is enabled) on the project page, but isn't currently used by the server for anything else. Avoid using 00:00 as a time because it confuses students — 23:59 is clearer (and 16:00 is healthier). Leave blank if you don't want to display a deadline at all (remember you can also use Announcements).  <br><br> _Default value:_ _none/empty_ |
| `PROJECT_CODE` | If this project is known by a course or module code, use it (for example, when we ran it at Royal Holloway, it was CS1999). See also `PROJECT_SLUG` which is how this code may appear in filenames of any downloaded files, if you need it to be different. The full name of the project is "the `PROJECT_CODE` Buggy Racing project", so if you don't have or need a course code, it's fine to leave it blank.  <br><br> _Default value:_ _none/empty_ |
| `PROJECT_SLUG` | This is how the `PROJECT_CODE` appears — as a prefix — in any filenames that are downloaded from the server. This is a kindness to help disambiguate files in your Downloads folder. If you leave this blank, it will default to using an automatic "slugged" version of your project code, if any. Note that there are some places where students can download files (e.g., tabulated specification data) too, so it's not just admin staff who will see it.  <br><br> _Default value:_ _none/empty_ |
| `PROJECT_SUBMISSION_LINK` | Provide a link to either the web page where you'll be accepting submissions (presumably zip files) or else a page containing clear instructions for the students to follow. The buggy race server does not handle submissions itself. By default, no submission information is provided (because it's very dependent on each institution), which means no link is displayed: so you must supply one yourself.  <br><br> _Default value:_ _none/empty_ |
| `IS_PROJECT_ZIP_INFO_DISPLAYED` | Typically, students are expected to submit their projects as a zip file containing the buggy editor web app (including a report/poster, if you've enabled it). The project page will display general information about those files (e.g., they should have the student's name just in case your submission process doesn't capture that: you end up with a lot of zip files with the same name otherwise). Use this setting to display or hide this general information on the "project" page. If set to `Yes`, remember to check that the text that appears on the project page does indeed make sense to students.  <br><br> _Default value:_ `Yes` |
| `PROJECT_ZIP_NAME_TYPE` | Normally the suggested filename for submissions (the students' zip file) is their username + `.zip`. But if you prefer your students to use an external username or ID, you can suggest it here. If you pick a type that users don't have, it will fall back to `username` (because all users have one). This setting is ignored if `IS_PROJECT_ZIP_INFO_DISPLAYED` is `No`.  <br><br> _Default value:_ `username` |
| `IS_USING_REMOTE_VS_WORKSPACE` | If your students will be using a remote server (see: `PROJECT_REMOTE_SERVER_NAME`) and are running VS Code over a remote session, the race server can produce a VS Code workspace file to facilitate cloning the repo onto that server and subsequently access it through VS Code. This is quite a specific setup: if you're not sure, you almost certainly do not want this.   <br><br> _Default value:_ `No` |
| `PROJECT_REMOTE_SERVER_ADDRESS` | If students are going to develop on a remote server, what is its address? This is used with their external username (or just username, if they haven't got one): for example enter `linux.example.ac.uk` so student Ada can log in via `ada@linux.example.ac.uk`. If you're not using a remote project server, leave this blank (see also `PROJECT_REMOTE_SERVER_NAME`).  <br><br> _Default value:_ _none/empty_ |
| `PROJECT_REMOTE_SERVER_NAME` | If students are going to develop on a remote server, what is its (human-facing) name? This is used to help students identify the server they are logging into (e.g, "the CompSci department's Unix server"). Leave this blank if your students are all working on their own machines (i.e., not a single teaching server with login accounts, python, and personalised HTTP ports).  <br><br> _Default value:_ _none/empty_ |
| `PROJECT_REMOTE_SERVER_APP_URL` | If students are going to develop on a remote server, what is the URL then need to hit in their browser to see their app? Presumably it will have a custom port on the end too. If you're not using a remote project server, leave this blank.  <br><br> _Default value:_ _none/empty_ |
| `IS_SHOWING_PROJECT_WORKFLOW` | It can be helpful for students to have a summary of the workflow process. If you set `IS_SHOWING_PROJECT_WORKFLOW` to `Yes` then the server will show either the default workflow page, or an external one if you specify `PROJECT_WORKFLOW_URL`. If you do choose to display the workflow page, when it's published take a moment to read it to confirm it matches what you expect your students to do.  <br><br> _Default value:_ `No` |
| `PROJECT_WORKFLOW_URL` | You can replace the default workflow page with a redirection to one you've customised (and hosted elsewhere). If you leave this setting blank, the default page will be shown. In either case, this setting is ignored if `IS_SHOWING_PROJECT_WORKFLOW` is `No`.  <br><br> _Default value:_ _none/empty_ |
| `PROJECT_PHASE_MIN_TARGET` | This is the minimum phase you'd expect an inexperienced programmer who's fully engaged in the project to have completed before running out of time. The default of 3 is based on our experience of running a 6-week project (several times) with students with only one term's prior experience of Python, and takes into account that task 3-MULTI is (deliberately) more involved than most students realise. This expectation is displayed to students (for example on the task list page). If you don't want this, set it to zero to remove the recommendation entirely.  <br><br> _Default value:_ `3` |
| `SUPERBASICS_URL` | There are a few places (for example in the workflow page and the tech notes) that link to a "superbasics" site which explains basic concepts for students. You can use the default, but you can also fork it and customise it, in which case put its URL here. Note that the links are to specific paths within the superbasics, which are added to this base URL, so if you host your own version be cautious about changing existing paths within it.  <br><br> _Default value:_ `https://superbasics.beholder.uk` |


---

* Previous: [Users config](users)
* Next: [Tasks config](tasks)
