import os
import traceback
from typing import Any, Dict, List

from todoist.api import TodoistAPI

sync_api = TodoistAPI(os.getenv("TODOIST_TOKEN"))
sync_api.sync()


def list_tasks(project: str) -> List[Dict[str, Any]]:
    try:
        tasks = sync_api.projects.get_data(
            get_id_from_name(project, "projects")
        )
        return sorted(
            list(map(extract_task_details, tasks["items"])),
            key=lambda i: i["priority"],
        )
    except Exception:
        print(traceback.format_exc())
    return []


def extract_task_details(task: Dict[str, Any]) -> Dict[str, Any]:
    new_task = {}
    new_task["content"] = task["content"]
    if task["due"]:
        new_task["due"] = task["due"]["date"]
    else:
        new_task["due"] = ""
    new_task["priority"] = task["priority"]
    new_task["project"] = get_name_from_id(task["project_id"], "projects")
    new_task["labels"] = list(
        map(lambda p: get_name_from_id(p, "labels"), task["labels"])
    )
    return new_task


def get_name_from_id(id: str, type: str) -> str:
    return getattr(sync_api, type).get_by_id(id).data["name"]


def add_task(content: str) -> None:
    try:
        sync_api.quick.add(content)
        sync_api.sync()
    except Exception:
        print(traceback.format_exc())


def delete_task(content: str) -> None:
    try:
        task = sync_api.items.get_by_id(get_id_from_name(content, "items"))
        task.delete()
        sync_api.commit()
    except Exception:
        print(traceback.format_exc())


def get_id_from_name(name: str, type: str) -> int:
    for object in sync_api.state[type]:
        if "name" in object.data and name == object.data["name"]:
            return object.data["id"]
        elif "content" in object.data and name == object.data["content"]:
            return object.data["id"]
    return -1


def update_task(task_name: str, update_data: Dict[str, Any]) -> None:
    item = sync_api.items.get_by_id(get_id_from_name(task_name, "items"))
    item.update(**update_data)
    sync_api.commit()
    sync_api.sync()
