## Task tracker cli

By task tracker you can add, update and delete tasks and list all tasks or list all tasks with certain status.

This project is built for the purpose of learning whose URL is [Task Tracker CLI](https://roadmap.sh/projects/task-tracker).

### How to use the task tracker

#### First step

open the file `task_tracker.py` in a python editor and run it.

#### Second step

type the command in the cmd and if you want to quit, just type `q` to quit.

### All commands you need to use the task tracker

##### Add task

command line:
`task-cli add "task description"` 
where the double quotation mark is needed and this format, otherwise it will be regarded as nonsense words.

##### Update task

command line:
`task-cli update task_id_number "task description"` 
which is the same as above and you need to offer the task's id number.

##### Delete task

command line:
`task-cli delete task_id_number`
which is the same as above.

##### List all tasks

command line:
`task-cli list`

##### List all tasks you plan to do

command line:
`task-cli list todo`

##### List all tasks that have been done

command line:
`task-cli list done`

##### List all tasks that are in progress

command line:
`task-cli list in-progress`
