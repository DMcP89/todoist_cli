import click
from utils import api


@click.group()
def tasks() -> None:
    pass


@tasks.command()
def list() -> None:
    click.echo("list tasks")


@tasks.command()
@click.argument("content")
def add(content: str) -> None:
    api.add_task(content)


@tasks.command()
@click.argument("task_name")
def delete(task_name: str) -> None:
    click.echo("deleteing {}".format(task_name))


@tasks.command()
def update() -> None:
    click.echo("update called")


@tasks.command()
def close() -> None:
    click.echo("close called")


@tasks.command()
def reopen() -> None:
    click.echo("reopen called")
