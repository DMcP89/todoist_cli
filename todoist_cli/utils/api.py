from todoist.api import TodoistAPI

sync_api = TodoistAPI("39787f245b4c23fe4dce45d84ad55b6903bedc45")
sync_api.sync()


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
