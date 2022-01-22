# from todoist_api_python.api import TodoistAPI
from todoist.api import TodoistAPI

sync_api = TodoistAPI("39787f245b4c23fe4dce45d84ad55b6903bedc45")
# rest_api = TodoistAPI("39787f245b4c23fe4dce45d84ad55b6903bedc45")
sync_api.sync()


def add_task(content: str, project_name: str) -> None:
    try:
        sync_api.items.add(
            content, project_id=get_project_id_from_name(project_name)
        )
        sync_api.commit()
    except Exception as error:
        print(error)


def get_project_id_from_name(project_name: str) -> int:
    for project in sync_api.state["projects"]:
        if project_name == project.data["name"]:
            return project.data["id"]
    return 0
