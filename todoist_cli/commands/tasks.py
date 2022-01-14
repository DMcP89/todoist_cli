import click
from todoist_api_python.api import TodoistAPI

rest_api = TodoistAPI("39787f245b4c23fe4dce45d84ad55b6903bedc45")


@click.group()
def tasks() -> None:
    pass


@tasks.command()
def list() -> None:
    tasks = rest_api.get_tasks()
    click.echo(tasks)


@tasks.command()
@click.argument("content")
def add(content: str) -> None:
    try:
        task = rest_api.add_task(content=content)
        print(task)
    except Exception as error:
        print(error)


@tasks.command()
def delete() -> None:
    click.echo("test called")


@tasks.command()
def update() -> None:
    click.echo("update called")


@tasks.command()
def close() -> None:
    click.echo("close called")


@tasks.command()
def reopen() -> None:
    click.echo("reopen called")
