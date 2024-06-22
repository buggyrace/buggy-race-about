---
title: Tasks config
layout: home
nav_order: 65
parent: Customising
has_children: false
---

# Configuring tasks

{: .navigation}
**Admin** → **Config** → Config:**Tasks**

The task config settings mostly concern informing the server of any
customisations you've made to the tasks that your students will be doing. 
 
See more about [creating the tasks](creating-tasks), which you can do when you
have completed set-up phase.






## Config settings ("Tasks")

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `IS_STORING_STUDENT_TASK_TEXTS` | Do you want students to be able to record text on this server reporting they approached/did each task? If you're running the project with a report (see `PROJECT_REPORT_TYPE`), then this allows students to save notes here as they go along, which in turn gives you some visibility of their progress (which is why we implemented it). If you choose `No`, this feature will be hidden. Note that you _can_ choose `Yes`, letting students store task texts, even if the project doesn't require a report.  <br><br> _Default value:_ `Yes` |
| `TASK_NAME_FOR_VALIDATION` | The name of the task that requires use of validation. If set, this is shown as a helpful link in the explanatory text on the reports page. If you haven't customised the task list, you don't need to change this.  <br><br> _Default value:_ `1-VALID` |
| `TASK_NAME_FOR_GET_CODE` | The name of the task for getting the source code. If you haven't customised the task list, you don't need to change this.  <br><br> _Default value:_ `0-GET` |
| `TASK_NAME_FOR_ENV_VARS` | The name of the task for setting environment variables. If you haven't customised the task list, you don't need to change this.   <br><br> _Default value:_ `3-ENV` |
| `TASK_NAME_FOR_API` | The name of the task that require use of the upload API. If set, this is shown as a helpful link in the explanatory text on the student's API settings page. If you set this to be empty, no link is shown. You can provide multiple task names by separating them with commas. If you haven't customised the task list, you don't need to change this.  <br><br> _Default value:_ `4-API` |
| `TASK_TEXT_SIZE_SUGGESTION` | An indication for your students as to how much text you expect them to provide in each of their task texts. It's shown on the report page instructions, after _"Suggested size for each task text:"_. No suggestion is shown if you've set it to the empty string or `IS_STORING_STUDENT_TASK_TEXTS` is `No`.  <br><br> _Default value:_ `a couple of sentences.` |
| `IS_ENCOURAGING_TEXT_ON_EVERY_TASK` | On the task list, do you want every task to display a strapline at the bottom of its "solution" block encouraging students to complete the task text? This setting is ignored (so: no such message will be displayed) if `IS_STORING_STUDENT_TASK_TEXTS` is `No`.   <br><br> _Default value:_ `Yes` |
| `IS_TASK_URL_WITH_ANCHOR` | By default, task URLs go direct to the server (e.g., `/project/tasks/3-multi`) which then redirects to an anchor within the all-tasks page (e.g., `/project/tasks#task-3-multi`). This works fine on this server and makes "nicer" URLs, but if you don't like this behaviour, choose `Yes` to have any generated links go directly to the anchor tag.  <br><br> _Default value:_ `No` |
| `BUGGY_EDITOR_ISSUES_CSV_HEADER_ROW` | The header row that should appear in the task issues CSV file. If you leave it empty, no header row will be included. You only need to change this if you're using a specific mechanism to automatically load issues into your chosen version control system and discover that the default isn't working. Supply a comma-separated list of column headings/titles (spaces after commas are stripped). If you're not sure, accept the default (which works with the race server's automatic injection into GitHub, as well as GitLab's CSV-to-issue mechanism).  <br><br> _Default value:_ `title, description` |
| `IS_ISSUES_CSV_CRLF_TERMINATED` | Choose `Yes` if you need Windows newlines at the end of each line of the task issues CSV file (you probably don't need to change this).  <br><br> _Default value:_ `No` |


 ---
 * Previous: [Project config](project)
 * Next: [Tech notes config](tech-notes)