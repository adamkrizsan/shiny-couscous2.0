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


def update_todo(idg):
    f = open("todos.json", "r")
    todos = json.load(f)
    for todo in todos:
        if todo["id"] == idg:
            todo["title"] = todo["title"] + '#'
            todo_u = todo["title"]
            print(todo["title"])

    return todo_u


update_todo(23)


def delete_todo(idg):
    f = open("todos.json", "r")
    todos = json.load(f)
    f.close()
    f = open("todos.json", "w")
    for todo in todos:
        if todo["id"] == idg:
            todos.remove(todo)
    json.dump(todos, f)


delete_todo(24)
