from email.utils import parsedate
import json
from tokenize import group
import requests


TODO_API_URL = "https://jsonplaceholder.cypress.io/todos"


def create_todo():
    response = requests.get(TODO_API_URL)
    with open("todos.json", "w") as f:
        json.dump(response.json(), f)
    return response.json()


todos = create_todo()


def read_todo(idg):
    f = open("todos.json", "r")
    todos = json.load(f)
    group_todos = {}
    for todo in todos:
        id = todo["userId"]
        if id not in group_todos:
            group_todos[id] = []
        group_todos[id].append(todo)


read_todo(3)


def update_todo(idg, file_obj):
    for todo in file_obj:
        if todo["id"] == idg:
            todo["title"] = todo["title"] + '#'
            print(todo["title"])

    return file_obj


update_todo(23, todos)


def delete_todo(idg, file_obj):
    f = open("todos.json", "w")
    for todo in file_obj:
        if todo["id"] == idg:
            file_obj.remove(todo)
    json.dump(file_obj, f)


<<<<<<< HEAD
delete_todo(24, todos)
=======
delete_todo(24, todos)
>>>>>>> 537d3f4e5eaa71b8b18c57ae82b6aecea497b26d
