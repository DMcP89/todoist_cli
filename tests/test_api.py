from todoist_cli.utils import api


def test_add_task():
    api.add_task("Add Task from PyTest")
    api.sync_api.sync()


def test_update_task():
    api.update_task("Add Task from PyTest", {"priority":4, "description": "Updated description from PyTest"})


def test_close_task():
    api.close_task("Add Task from PyTest")


def test_reopen_task():
    api.reopen_task("Add Task from PyTest")


def test_list_task():
    tasks = api.list_tasks("Inbox")
    assert tasks is not None


def test_delete_task():
    api.delete_task("Add Task from PyTest")
