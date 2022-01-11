import click

from .commands import tasks


@click.group()
def todo() -> None:
    pass


todo.add_command(tasks.tasks)
