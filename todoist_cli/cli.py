import click

from todoist_cli.commands.tasks import tasks


@click.group()
def todo() -> None:
    pass


todo.add_command(tasks)


if __name__ == "__main__":
    todo()
