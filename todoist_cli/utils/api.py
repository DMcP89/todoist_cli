from typing import Any, Dict

from todoist.api import TodoistAPI

sync_api = TodoistAPI("39787f245b4c23fe4dce45d84ad55b6903bedc45")
sync_api.sync()


def list_tasks(project: str) -> list[dict[str, Any]]:
    try:
        tasks = sync_api.projects.get_data(
            get_id_from_name(project, "projects")
        )["items"]
        return sorted(
            list(map(extract_task_details, tasks)), key=lambda i: i["priority"]
        )
    except Exception as error:
        print(error)
    return []


def extract_task_details(task: dict[str, str]) -> dict[str, Any]:
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
    except Exception as error:
        print(error)


def get_id_from_name(name: str, type: str) -> int:
    for object in sync_api.state[type]:
        if "name" in object.data and name == object.data["name"]:
            return object.data["id"]
        elif "content" in object.data and name == object.data["content"]:
            return object.data["id"]
    return -1
