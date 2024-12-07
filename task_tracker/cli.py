from datetime import datetime
from tabulate import tabulate
from argparse import ArgumentParser
from typing import Callable
import json
import sys
import os


def main() -> None:
    db_path: str = os.path.expanduser("~/task_tracker.json")
    database: dict[str, dict] = get_database(db_path)

    commands_dict: dict[str, dict] = supported_cmd()

    inp, args = get_input(commands_dict)

    try:
        inp(database, **args)
    except KeyError:
        sys.exit("No task with this ID")

    save_database(database, db_path)


#Supported commands
def supported_cmd() -> dict[str, dict]:
    return {
        "add": {
            "do": add,
            "help": "Add a new task",
            "args": [
                {"name": "description", "help": "Description of the new task"}
            ]
        },
        "delete": {
            "do": delete,
            "help": "Delete a task",
            "args": [
                {"name": "id", "help": "ID of the task"}
            ]
        },
        "update": {
            "do": update,
            "help": "Update a task",
            "args": [
                {"name": "id", "help": "ID of the task"},
                {"name": "description", "help": "New description of the task"}
            ]
        },
        "mark-in-progress": {
            "do": in_progress,
            "help": "Mark a task as in-progress",
            "args": [
                {"name": "id", "help": "ID of the task"}
            ]
        },
        "mark-done": {
            "do": done,
            "help": "Mark a task as done",
            "args": [
                {"name": "id", "help": "ID of the task"}
            ]
        },
        "list": {
            "do": list_task,
            "help": "List tasks based on their status",
            "args": [
                {
                    "name": "--status",
                    "choices": ["all", "todo", "in-progress", "done"],
                    "default": "all",
                    "help": "Filter tasks by status"
                }
            ]
        }
    }

#Get input
def get_input(cmd_dict: dict[str, dict]) -> tuple[Callable, dict]:
    parser = ArgumentParser(description="A Task Tracker CLI")
    sub_parser = parser.add_subparsers(dest="command", required=True)

    for cmd, details in cmd_dict.items():
        cmd_parser = sub_parser.add_parser(cmd, help=details["help"])
        for a in details["args"]:
            cmd_parser.add_argument(a["name"], **{k: v for k, v in a.items() if k != "name"})
    
    arguments = parser.parse_args().__dict__
    inp: Callable = cmd_dict[arguments.pop("command")]["do"]

    return inp, arguments

#Write new data to the JSON file
def save_database(database: dict[str, dict], database_path: str) -> None:
    with open(database_path, "w") as f:
        json.dump(database, f, indent=4)

#Get data from the JSON file
def get_database(database_path: str) -> dict[str, dict]:
    try:
        with open(database_path) as f:
            database = json.load(f)
    except FileNotFoundError:
        database = {}
    return database


#Methods
#Add tasks to the database
def add(database: dict[str, dict], description: str) -> None:
    today: str = datetime.today().isoformat(sep=" ", timespec="seconds")
    id: str = str(int(max("0", *database.keys())) + 1)

    database[id] = {
        "Description": description,
        "Status": "todo",
        "Created-at": today,
        "Updated-at": today,
    }
    list_task({id: database[id]})

#Delete tasks and update the ID
def delete(database: dict[str, dict], id: str) -> None:
    list_task({id: database[id]})
    del(database[id])

#Update the description and status of the task
def update(database: dict[str, dict], id: str, description: str) -> None:
    database[id]["Description"] = description
    database[id]["Updated-at"] = datetime.today().isoformat(sep = " ", timespec="seconds")
    list_task({id: database[id]})

#Change task status to "in-progress"
def in_progress(database: dict[str, dict], id: str) -> None:
    database[id]["Status"] = "in-progress"
    database[id]["Updated-at"] = datetime.today().isoformat(sep = " ", timespec="seconds")
    list_task({id: database[id]})

#Change task status to "done"
def done(database: dict[str, dict], id: str) -> None:
    database[id]["Status"] = "done"
    database[id]["Updated-at"] = datetime.today().isoformat(sep = " ", timespec="seconds")
    list_task({id: database[id]})

#List current tasks in the database
def list_task(database: dict[str, dict], status="all") -> None:
    header = ["ID", "Description", "Status", "Created-at", "Updated-at"]
    table = []
    for num, task in database.items():
        if status == "all" or task["Status"] == status:
            table.append([num, *task.values()])
    print(tabulate(table, headers=header, tablefmt="grid"))


if __name__ == "__main__":
    main()