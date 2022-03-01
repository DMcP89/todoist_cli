from typing import Tuple

import click
from rich.console import Console
from rich.table import Table

from todoist_cli.utils import api


@click.group()
def tasks() -> None:
    """
    Manage your todoist tasks [add|close|delete|list|reopen|update]
    """
    pass


@tasks.command()
@click.argument("project", required=False)
def list(project: str) -> None:
    """Return all active tasks from a given project, default is inbox

    PROJECT is the name of the project to list the tasks for
    """
    if not project:
        project = "Inbox"
    tasks = api.list_tasks(project)
    table = Table(title="Open tasks for {}".format(project))
    table.add_column("Due Date", justify="right", style="cyan", no_wrap=True)
    table.add_column("Task", justify="right", style="magenta")
    table.add_column("Priority", justify="right", style="red")
    table.add_column("Project", justify="right", style="cyan")
    table.add_column("Labels", justify="right", style="green")

    for task in tasks:
        table.add_row(
            task["due"],
            task["content"],
            str(task["priority"]),
            task["project"],
            str(task["labels"]),
        )

    console = Console()
    console.print(table)


@tasks.command()
@click.argument("content")
def add(content: str) -> None:
    """Add a task

    CONTENT is the task to be added, uses Todoist quick add formatting
    """
    api.add_task(content)


@tasks.command()
@click.argument("task_name")
def delete(task_name: str) -> None:
    """Delete a task

    TASK_NAME is the name of the task to delete
    """
    api.delete_task(task_name)


@tasks.command()
@click.argument("task_name")
@click.option(
    "-c", "--content", "content", type=str, help="New name for the task"
)
@click.option(
    "-d",
    "--description",
    "description",
    type=str,
    help="New description for the task",
)
@click.option(
    "-p",
    "--priority",
    "priority",
    type=int,
    help="Set the priority level for the task",
)
@click.option(
    "-l",
    "--labels",
    "labels",
    multiple=True,
    help="What labels to add to the task, max:3",
)
def update(
    task_name: str,
    content: str,
    description: str,
    priority: int,
    labels: Tuple[str],
) -> None:
    """Update a task

    TASK_NAME is the name of the task to be updated
    """
    update_data = {
        "content": content,
        "description": description,
        "priority": priority,
        "labels": labels,
    }
    api.update_task(task_name, update_data)


@tasks.command()
@click.argument("task_name")
def close(task_name: str) -> None:
    """Close a task
    
    TASK_NAME is the name of the task to be closed
    """
    api.close_task(task_name)


@tasks.command()
@click.argument("task_name")
def reopen(task_name: str) -> None:
    """Reopen a task
    
    TASK_NAME is the name of the task to be reopened
    """
    api.reopen_task(task_name)
