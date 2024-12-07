# Task Tracker CLI

As a simple solution to [task_tracker](https://roadmap.sh/projects/task-tracker) from [roadmap.sh](roadmap.sh), this is a command-line interface application created to manage your tasks through various commands.

## Key Features

Supported functions include:

- Add a new task
- Delete a task
- Update a task description
- Mark a task as *in-progress/done*
- List tasks and filter them by status

## Installation and Usage

### Install via pip

Run the following command to install:

```bash
pip install git+https://github.com/ndongdoan/task_trackerCLI.git
```

### Run from command line

Here are examples for all commands:

```bash
#To add a new task
$ task add "Practice LeetCode"
$ task add "Go take a shower"

#To update a task's description
$ task update 1 "Touch grass"

#To delete a task 
$ task delete 1

#To mark a task as in-progress
$ task mark-in-progress 2

#To mark a task as done
$ task mark-done 2

#To list tasks (-s and --status are both accepted)
$ task list
$ task list -s todo
$ task list --status in-progress
$ task list -s done
```

## Project & Main Script Structure

### Project Structure

- **task_tracker**: Package folder.
  - **\_\_init__.py**: Initialize this as a package and include optional basic metadata (can be left empty).
  - **cli.py**: Main script logic.
- **setup.py**: Allow users to install package.
- **README.md**: Detailed project's description

### Main Script Structure

- ```main()```: Parse users' command and return with the corresponding functions along with writing to the database file.
- ```supported_cmd()```: Return the dictionary that stores info about all functions.
- ```get_input(cmd_dict: dict[str, dict])```: Process users' commands and return with their corresponding functions based on the command dictionary.
- ```save_database(database: dict[str, dict], database_path: str)```: Write new data to the database file.
- ```get_database(database_path: str)```: Load content from the database file.
- ```add(database: dict[str, dict], description: str)```: Add a new task with their description.
- ```delete(database: dict[str, dict], id: str)```: Delete a task with the given ID.
- ```update(database: dict[str, dict], id: str, description: str)```: Update a task description.
- ```in_progress(database: dict[str, dict], id: str)```: Mark a task's status as in-progress.
- ```done(database: dict[str, dict], id: str)```: Mark a task's status as done.
- ```list_task(database: dict[str, dict], status="all")```: List tasks with the option to filter them based on their status.
