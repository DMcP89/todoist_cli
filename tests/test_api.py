import os

os.environ['TODOIST_TOKEN'] = "Test-Token"

from todoist_cli.utils import api
from unittest.mock import MagicMock
from todoist.models import Item
from todoist.api import TodoistAPI

api.sync_api.commit = MagicMock(return_value=None)
api.sync_api.sync = MagicMock(return_value=None)

test_item_content = "Add Task from PyTest"
test_item_data = {
    'added_by_uid': 2947981,
    'assigned_by_uid': None,
    'checked': 0,
    'child_order': 1,
    'collapsed': 0,
    'content': test_item_content,
    'date_added': '2022-02-07T03:00:57Z',
    'date_completed': None,
    'day_order': -1,
    'description': '',
    'due': None,
    'id': 5571086177,
    'in_history': 0,
    'is_deleted': 0,
    'labels': [],
    'legacy_project_id': 131917843,
    'parent_id': None,
    'priority': 1,
    'project_id': 937224211,
    'responsible_uid': None,
    'section_id': None,
    'sync_id': None,
    'user_id': 2947981
}
test_item = Item(TodoistAPI, test_item_data)
test_item.update = MagicMock(return_value=None)
test_item.complete = MagicMock(return_value=None)
test_item.uncomplete = MagicMock(return_value=None)
api.sync_api.items.get_by_id = MagicMock(return_value=test_item)
api.sync_api.projects.get_data = MagicMock(return_value={"items": [test_item_data]})

def test_add_task():
    api.sync_api.quick.add = MagicMock(return_value=None)
    api.add_task(test_item_content)
    api.sync_api.quick.add.assert_called_with(test_item_content)


def test_update_task():
    update_data = {"priority":4, "description": "Updated description from PyTest"}
    api.update_task(test_item_content, update_data)
    test_item.update.assert_called_with(**update_data)


def test_close_task():
    api.close_task(test_item_content)
    test_item.complete.assert_called()


def test_reopen_task():
    api.reopen_task(test_item_content)
    test_item.uncomplete.assert_called()


def test_list_task():
    tasks = api.list_tasks("Inbox")
    assert tasks is not None


def test_delete_task():
    api.delete_task(test_item_content)
