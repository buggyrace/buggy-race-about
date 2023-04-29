---
title: Tasks config
layout: home
nav_order: 65
parent: Customising
has_children: false
---


# Configuring tasks

{: .directions}
**Admin** → **Config** → Config:**Tasks**

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
 
 
 
See more about [managing the tech notes](../static-content/tech-notes).

## Config settings ("Tasks")

{: .config-settings}
| Setting  | Description   |
|----------|---------------|
| `IS_STORING_STUDENT_TASK_TEXTS` | Do you want students to be able to record text on this server reporting they approached/did each task? If you're running the project with a report (see `PROJECT_REPORT_TYPE`), then this allows students to save notes here as they go along, which in turn gives you some visibility of their progress (which is why we implemented it). If you choose `No`, this feature will be hidden. Note that you _can_ choose `Yes`, letting students store task texts, even if the project doesn't require a report.  <br><br> _Default value:_ `Yes` |
| `TASK_NAME_FOR_VALIDATION` | The name of the task that requires use of validation. If set, this is shown as a helpful link in the explanotary text on the reports page. If you haven't customised the task list, you don't need to change this.  <br><br> _Default value:_ `1-VALID` |
| `TASK_NAME_FOR_GET_CODE` | The name of the task for getting the source code. If you haven't customised the task list, you don't need to change this.  <br><br> _Default value:_ `0-GET` |
| `TASK_NAME_FOR_ENV_VARS` | The name of the task for setting environment variables. If you haven't customised the task list, you don't need to change this.   <br><br> _Default value:_ `3-ENV` |
| `TASK_NAME_FOR_API` | The name of the task that require use of the upload API. If set, this is shown as a helpful link in the explanotary text on the student's API settings page. If you set this to be empty, no link is shown. You can provide mulitple task names by separating them with commas. If you haven't customised the task list, you don't need to change this.  <br><br> _Default value:_ `4-API` |
| `IS_TASK_URL_WITH_ANCHOR` | By default, task URLs go direct to the server (e.g., `/project/tasks/3-multi`) which then redirects to an anchor within the all-tasks page (e.g., `/project/tasks#task-3-multi`). This works fine on this server and makes "nicer" URLs, but if you don't like this behaviour, choose `Yes` to have any generated links go directly to the anchor tag.  <br><br> _Default value:_ `No` |
| `IS_ISSUES_CSV_CRLF_TERMINATED` | Choose `Yes` if you need Windows newlines at the end of each line of the task issues CSV file (you probably don't need to change this).  <br><br> _Default value:_ `No` |

 ---
 * Previous: [Project config](project)
 * Next: [Tech notes config](tech-notes)