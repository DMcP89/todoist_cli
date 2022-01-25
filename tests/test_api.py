from todoist_cli.utils import api


def test_add_task():
    api.add_task("Add Task from PyTest")


def test_delete_task():
    api.delete_task("Add Task from PyTest")
