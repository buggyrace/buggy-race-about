---
title: Tasks config
layout: home
nav_order: 70
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
| `PROJECT_PHASE_MIN_TARGET` | This is the minimum phase you&#39;d expect an inexperienced programmer who&#39;s fully engaged in the project to have completed before running out of time. The default of 3 is based on our experience of running a 6-week project (several times) with students with only one term&#39;s prior experience of Python, and takes into account that task 3-MULTI is (deliberately) more involved than most students realise. This expectation is displayed to students (for example on the task list page). If you don&#39;t want this, set it to zero to remove the recommendation entirely.  <br/><br/> _Default value:_ `3` |
| `IS_STORING_STUDENT_TASK_TEXTS` | Do you want students to be able to record text on this server reporting they approached/did each task? If you&#39;re running the project with a report (see `PROJECT_REPORT_TYPE`), then this allows students to save notes here as they go along, which in turn gives you some visibility of their progress (which is why we implemented it). If you choose `No`, this feature will be hidden. Note that you _can_ choose `Yes`, letting students store task texts, even if the project doesn&#39;t require a report.  <br/><br/> _Default value:_ `Yes` |
| `IS_STORING_TASK_LIST_IN_DB` | When the task list is published, is the HTML page stored in the database? If you choose `No`, the cached HTML will be written as a file instead — in most cases (and especially if you are running on an ephemeral file system such as Heroku&#39;s) it&#39;s probably best to choose `Yes` and only change if you notice performance problems.  <br/><br/> _Default value:_ `Yes` |
| `TASK_NAME_FOR_VALIDATION` | The name of the task that requires use of validation. If set, this is shown as a helpful link in the explanatory text on the reports page. If you haven&#39;t customised the task list, you don&#39;t need to change this.  <br/><br/> _Default value:_ `1-VALID` |
| `TASK_NAME_FOR_GET_CODE` | The name of the task for getting the source code. If you haven&#39;t customised the task list, you don&#39;t need to change this.  <br/><br/> _Default value:_ `0-GET` |
| `TASK_NAME_FOR_ENV_VARS` | The name of the task for setting environment variables. If you haven&#39;t customised the task list, you don&#39;t need to change this.   <br/><br/> _Default value:_ `3-ENV` |
| `TASK_NAME_FOR_API` | The name of the task that require use of the upload API. If set, this is shown as a helpful link in the explanatory text on the student&#39;s API settings page. If you set this to be empty, no link is shown. You can provide multiple task names by separating them with commas. If you haven&#39;t customised the task list, you don&#39;t need to change this.  <br/><br/> _Default value:_ `4-API` |
| `TASK_TEXT_SIZE_SUGGESTION` | An indication for your students as to how much text you expect them to provide in each of their task texts. It&#39;s shown on the report page instructions, after _&#34;Suggested size for each task text:&#34;_. No suggestion is shown if you&#39;ve set it to the empty string. This applies to task texts in the report (i.e., if `PROJECT_REPORT_TYPE` is not `No report`) or on the race server if `IS_STORING_STUDENT_TASK_TEXTS` is `Yes`, and is only advisory.  <br/><br/> _Default value:_ `a couple of sentences.` |
| `IS_ENCOURAGING_TEXT_ON_EVERY_TASK` | On the task list, do you want every task to display a strapline at the bottom of its &#34;solution&#34; block encouraging students to complete the task text? This setting is ignored (so: no such message will be displayed) if `IS_STORING_STUDENT_TASK_TEXTS` is `No`.   <br/><br/> _Default value:_ `Yes` |
| `IS_ENCOURAGING_VCS_ON_EVERY_TASK` | On the task list, do you want every task (except those in phase 0) to display a message at the bottom of its &#34;solution&#34; block reminding students to commit and push to version control? You can customise the message by changing `TASK_ENCOURAGE_VCS_MESSAGE`. This setting is ignored (so: no such message will be displayed) if `IS_USING_VCS` is `No`.  <br/><br/> _Default value:_ `No` |
| `TASK_ENCOURAGE_VCS_MESSAGE` | If you are encouraging students to commit/push their work to a version control system, the race server will display this message along with each task. See `IS_ENCOURAGING_VCS_ON_EVERY_TASK` for more about this behaviour. If the special string `%VCS_NAME%` occurs in the message, it will be replaced with the value of config setting `VCS_NAME`. This setting is ignored if `IS_ENCOURAGING_VCS_ON_EVERY_TASK` is `No`  <br/><br/> _Default value:_ `Don&#39;t forget to commit any changes you make for this task and push them to %VCS_NAME%.` |
| `IS_TASK_URL_WITH_ANCHOR` | By default, task URLs go direct to the server (e.g., `/project/tasks/3-multi`) which then redirects to an anchor within the all-tasks page (e.g., `/project/tasks#task-3-multi`). This works fine on this server and makes &#34;nicer&#34; URLs, but if you don&#39;t like this behaviour, choose `Yes` to have any generated links go directly to the anchor tag.  <br/><br/> _Default value:_ `No` |
| `BUGGY_EDITOR_ISSUES_CSV_HEADER_ROW` | The header row that should appear in the task issues CSV file. If you leave it empty, no header row will be included. You only need to change this if you&#39;re using a specific mechanism to automatically load issues into your chosen version control system and discover that the default isn&#39;t working. Supply a comma-separated list of column headings/titles (spaces after commas are stripped). If you&#39;re not sure, accept the default (which works with the race server&#39;s automatic injection into GitHub, as well as GitLab&#39;s CSV-to-issue mechanism).  <br/><br/> _Default value:_ `title, description` |
| `IS_ISSUES_CSV_IN_REVERSE_ORDER` | Chosse `Yes` if you want the issues in the CSV to be in reverse order (so task `0-GET` is the last row, not the first). The web interface of GitHub and GitLab both list ther issues most-recent-first, so if you want the issues to be displayed in the same order as the numbered tasks that they map to (with `0-GET`, the first task, at the top), set this to `Yes`. This causes the highest-numbered tasks&#39; issues to be created first, and hence be the oldest. If you change this value after you&#39;ve published the task list, you should re-publish the list (because the CSV file is cached).  <br/><br/> _Default value:_ `No` |
| `IS_ISSUES_CSV_CRLF_TERMINATED` | Choose `Yes` if you need Windows newlines at the end of each line of the task issues CSV file (you probably don&#39;t need to change this).  <br/><br/> _Default value:_ `No` |

  
 ---
 * Previous: [Editor config](editor)
 * Next: [Users config](users)