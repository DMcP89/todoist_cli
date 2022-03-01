# Todoist-cli

Simple commnandl ine utility for managing tasks and projects in Todoist

## Install

Clone this repository
```
git clone https://github.com/DMcP89/todoist_cli.git
cd todoist_cli
```
Install using poetry
```
poetry install
```

## Usage
Manager command
```
$ todoist-cli
Usage: todoist-cli [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  tasks  Manage your todoist tasks [add|close|delete|list|reopen|update]
```

### Tasks
```
$ todoist-cli tasks
Usage: todoist-cli tasks [OPTIONS] COMMAND [ARGS]...

  Manage your todoist tasks [add|close|delete|list|reopen|update]

Options:
  --help  Show this message and exit.

Commands:
  add     Add a task
  close   Close a task
  delete  Delete a task
  list    Return all active tasks from a given project, default is inbox
  reopen  Reopen a task
  update  Update a task
```
#### Adding a task
```
$ todoist-cli tasks add --help
Usage: todoist-cli tasks add [OPTIONS] CONTENT

  Add a task

  CONTENT is the task to be added, uses Todoist quick add formatting

Options:
  --help  Show this message and exit.
$ todoist-cli tasks add "I'm adding a task through the cli! #Personal tomorrow"
```
#### Close a task
```
$ todoist-cli tasks close --help
Usage: todoist-cli tasks close [OPTIONS] TASK_NAME

  Close a task

  TASK_NAME is the name of the task to be closed

Options:
  --help  Show this message and exit.
$ todoist-cli tasks close "Task I'd like to close"
```
#### Delete a task
```
$ todoist-cli tasks delete --help
Usage: todoist-cli tasks delete [OPTIONS] TASK_NAME

  Delete a task

  TASK_NAME is the name of the task to delete

Options:
  --help  Show this message and exit.
$ todoist-cli tasks delete "Task I'd like to delete"
```
#### List tasks
```
$ todoist-cli tasks list --help
Usage: todoist-cli tasks list [OPTIONS] [PROJECT]

  Return all active tasks from a given project, default is inbox

  PROJECT is the name of the project to list the tasks for

Options:
  --help  Show this message and exit.
$ todoist-cli tasks list Inbox
                      Open tasks for Inbox
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Due Date ┃           Task ┃ Priority ┃ Project ┃      Labels ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━━━┩
│          │   Example task │        1 │   Inbox │          [] │
│          │ Example task 3 │        1 │   Inbox │ ['on-hold'] │
│          │ Example task 2 │        4 │   Inbox │          [] │
└──────────┴────────────────┴──────────┴─────────┴─────────────┘
```
#### Reopen a task
```
$ todoist-cli tasks reopen --help
Usage: todoist-cli tasks reopen [OPTIONS] TASK_NAME

  Reopen a task

  TASK_NAME is the name of the task to be reopened

Options:
  --help  Show this message and exit.
$ todoist-cli tasks reopen "I'd like to reopen"
```
#### Update a task
```
$ todoist-cli tasks update --help
Usage: todoist-cli tasks update [OPTIONS] TASK_NAME

  Update a task

  TASK_NAME is the name of the task to be updated

Options:
  -c, --content TEXT      New name for the task
  -d, --description TEXT  New description for the task
  -p, --priority INTEGER  Set the priority level for the task
  -l, --labels TEXT       What labels to add to the task, max:3
  --help                  Show this message and exit.
$ todoist-cli tasks update "Task I'd like updated" -c "New task name" -d "description for task"
```