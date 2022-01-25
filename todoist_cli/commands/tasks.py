import click
from rich.console import Console
from rich.table import Table

from todoist_cli.utils import api


@click.group()
def tasks() -> None:
    pass


@tasks.command()
@click.argument("project", required=False)
def list(project: str) -> None:
    """Return all active tasks from a given project, default is inbox"""
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
    api.add_task(content)


@tasks.command()
@click.argument("task_name")
def delete(task_name: str) -> None:
    api.delete_task(task_name)


@tasks.command()
def update() -> None:
    click.echo("update called")


@tasks.command()
def close() -> None:
    click.echo("close called")


@tasks.command()
def reopen() -> None:
    click.echo("reopen called")
