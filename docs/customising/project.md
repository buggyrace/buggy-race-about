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

You can also enable overriding certain project settings for individual users:
see [customising deadlines and links for individual students](../teaching/submission#customising-deadlines-and-links-for-individual-students).


## Config settings ("Project")

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `EDITOR_DISTRIBUTION_METHOD` | How do your students get the Buggy Editor source code at the start of the project? During set-up, choosing this setting affects some of the other settings in subsequent groups.  <br/><br/> _Default value:_ `zip` |
| `PROJECT_REPORT_TYPE` | If you require students to produce a report of how they tackled the tasks, indicate that here. Choose `document` if you want students to make a document, or `in editor` if the report takes the form of an additional webpage in the student&#39;s buggy editor webserver. If you choose `No report`, all mentions will be removed: see also the `IS_STORING_STUDENT_TASK_TEXTS` setting in the **Tasks** group of settings.   <br/><br/> _Default value:_ `in editor` |
| `PROJECT_REPORT_URL` | The race server will display a basic page of instructions about the report (which is especially helpful if `PROJECT_REPORT_TYPE` is `In editor`), but if you prefer to direct students to a custom page, provide a URL to use insteead. This setting is ignored if `PROJECT_REPORT_TYPE` is `No report`.  <br/><br/> _Default value:_ _none/empty_ |
| `PROJECT_POSTER_TYPE` | Do you require students to produce a poster proclaiming the features of their editor? If it&#39;s `top of report` or `bottom of report` this means it&#39;s part of the report (so `PROJECT_REPORT_TYPE` must not be `No report`). Choose `in editor` if the report takes the form of an additional webpage in the student&#39;s buggy editor webserver. If you choose `No poster`, all mentions will be removed.  <br/><br/> _Default value:_ `in editor` |
| `PROJECT_POSTER_URL` | The race server will display a basic page of instructions about the poster (which is especially helpful if `PROJECT_POSTER_TYPE` is `In editor`), but if you prefer to direct students to a custom page, provide a URL to use insteead. This setting is ignored if `PROJECT_POSTER_TYPE` is `No poster`.  <br/><br/> _Default value:_ _none/empty_ |
| `PROJECT_CODE` | If this project is known by a course or module code, use it (for example, when we ran it at Royal Holloway, it was CS1999 or CS0001). See also `PROJECT_SLUG` which is how this code may appear in filenames of any downloaded files, if you need it to be different. The full name of the project is &#34;the `PROJECT_CODE` Buggy Racing project&#34;, so if you don&#39;t have or need a course code, it&#39;s fine to leave it blank.  <br/><br/> _Default value:_ _none/empty_ |
| `PROJECT_SLUG` | This is how the `PROJECT_CODE` appears — as a prefix — in any filenames that are downloaded from the server. This is a kindness to help disambiguate files in your Downloads folder. If you leave this blank, it will default to using an automatic &#34;slugged&#34; version of your project code, if any. Note that there are some places where students can download files (e.g., tabulated specification data) too, so it&#39;s not just admin staff who will see it.  <br/><br/> _Default value:_ _none/empty_ |
| `PROJECT_SUBMISSION_DEADLINE` | If you require all students to submit their projects on a specific deadline, set it here. This is displayed prominently (if set) on the on the project page, but isn&#39;t currently used by the server for anything else. Avoid using 00:00 as a time because it confuses students — 23:59 is clearer (and 16:00 is healthier). Leave blank if you don&#39;t want to display a deadline at all (remember you can also use Announcements). You can override this deadline (even if it is empty) for specific users by setting `IS_PROJECT_SUBMISSION_DEADLINE_PER_USER` to `Yes`, and then editing the individual users.  <br/><br/> _Default value:_ _none/empty_ |
| `IS_PROJECT_SUBMISSION_DEADLINE_PER_USER` | If the project has a submission deadline (which you set with `PROJECT_SUBMISSION_DEADLINE`), and it applies to all students, choose `No`. Setting this to `Yes` allows administrators to override or set that deadline for specific students, which might be handy if you need to handle extensions or resits. _Note:_ If you set this (or _any_ of the `IS_PROJECT_*_PER_USER` settings) to `Yes`, the public project page will hide **all** of those items, even if they are not explicitly customisable, unless the user is logged-in.  <br/><br/> _Default value:_ `No` |
| `PROJECT_SUBMISSION_LINK` | Provide a link to either the web page where you&#39;ll be accepting submissions (presumably zip files) or else a page containing clear instructions for the students to follow. The buggy race server does not handle submissions itself. By default, no submission information is provided (because it&#39;s very dependent on each institution), which means no link is displayed: so you must supply one yourself. You can override this link (even if it is empty) for specific users by setting `IS_PROJECT_SUBMISSION_LINK_PER_USER` to `Yes`, and then editing the individual users.  <br/><br/> _Default value:_ _none/empty_ |
| `IS_PROJECT_SUBMISSION_LINK_PER_USER` | If the project has a submission link (which you set with `PROJECT_SUBMISSION_LINK`), and it applies to all students, choose `No`. Setting this to `Yes` allows administrators to override or set that URL for specific students. _Note:_ If you set this (or _any_ of the `IS_PROJECT_*_PER_USER` settings) to `Yes`, the public project page will hide **all** of those items, even if they are not explicitly customisable, unless the user is logged-in.  <br/><br/> _Default value:_ `No` |
| `PROJECT_NOTICE` | An optional text that, if set, will be displayed on the project page. You can override this notice (even if it is empty) for specific users by setting `IS_PROJECT_NOTICE_PER_USER` to `Yes`, and then editing the individual users. Set `IS_HTML_ENABLED_IN_PROJECT_NOTICES` to `Yes` if you want project notices (this one, and any per-user ones too) to contain HTML, but be careful because you _can_ break the project page layout if the notice contains bad HTML.  <br/><br/> _Default value:_ _none/empty_ |
| `IS_PROJECT_NOTICE_PER_USER` | Do you want to be able to override the `PROJECT_NOTICE` (even if it is empty) so a customised text is displayed to specific students? This is probably most useful if you&#39;ve also enabled the `IS_PROJECT_SUBMISSION_DEADLINE_PER_USER` or `IS_PROJECT_SUBMISSION_LINK_PER_USER` settings, so you can (if necessary) explain to the student why their deadline or link is what it is. _Note:_ If you set this (or _any_ of the `IS_PROJECT_*_PER_USER` settings) to `Yes`, the public project page will hide **all** of those items, even if they are not explicitly customisable, unless the user is logged-in.  <br/><br/> _Default value:_ `No` |
| `IS_PROJECT_ZIP_INFO_DISPLAYED` | Typically, students are expected to submit their projects as a zip file containing the buggy editor web app (including a report/poster, if you&#39;ve enabled it). The project page will display general information about those files (e.g., they should have the student&#39;s name just in case your submission process doesn&#39;t capture that: you end up with a lot of zip files with the same name otherwise). Use this setting to display or hide this general information on the &#34;project&#34; page. If set to `Yes`, remember to check that the text that appears on the project page does indeed make sense to students.  <br/><br/> _Default value:_ `Yes` |
| `PROJECT_ZIP_NAME_TYPE` | Normally the suggested filename for submissions (the students&#39; zip file) is their username + `.zip`. But if you prefer your students to use an external username or ID, you can suggest it here. If you pick a type that users don&#39;t have, it will fall back to `username` (because all users have one). This setting is ignored if `IS_PROJECT_ZIP_INFO_DISPLAYED` is `No`.  <br/><br/> _Default value:_ `username` |
| `IS_HTML_ENABLED_IN_PROJECT_NOTICES` | Can the project notice (and any custom notices, if `IS_PROJECT_NOTICE_PER_USER` is `Yes`) contain HTML? If you don&#39;t need it to be, it&#39;s best to set it to `No` (the default), so there&#39;s no risk of accidentally breaking the project page with bad HTML.  <br/><br/> _Default value:_ `No` |
| `IS_SHOWING_PROJECT_WORKFLOW` | It can be helpful for students to have a summary of the workflow process. If you set `IS_SHOWING_PROJECT_WORKFLOW` to `Yes` then the server will show either the default workflow page, or an external one if you specify `PROJECT_WORKFLOW_URL`. If you do choose to display the workflow page, when it&#39;s published take a moment to read it to confirm it matches what you expect your students to do.  <br/><br/> _Default value:_ `No` |
| `PROJECT_WORKFLOW_URL` | You can replace the default workflow page with a redirection to one you&#39;ve customised (and hosted elsewhere). If you leave this setting blank, the default page will be shown. In either case, this setting is ignored if `IS_SHOWING_PROJECT_WORKFLOW` is `No`.  <br/><br/> _Default value:_ _none/empty_ |

  
---

* Previous: [External links config](links)
* Next: [Editor config](editor)
