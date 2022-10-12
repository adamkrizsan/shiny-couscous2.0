import json
import requests


TODO_API_URL = "https://jsonplaceholder.cypress.io/todos"


def create_todo():
    response = requests.get(TODO_API_URL)
    with open("todos.json", "w") as f:
        json.dump(response.json(), f)


def read_todo(idg):
    f = open("todos.json", "r")
    todos = json.load(f)
    f.close()
    group_todos = {}
    for todo in todos:
        if id == todo["id"]:
            return todo


def update_todo(idg, todou):
    f = open("todos.json", "r")
    todos = json.load(f)
    f.close()
    for todo in todos:
        if todo["id"] == idg:
            todo = todou
    return todos


def delete_todo(idg):
    f = open("todos.json", "r")
    todos = json.load(f)
    f.close()
    f = open("todos.json", "w")
    for todo in todos:
        if todo["id"] == idg:
            todos.remove(todo)
    json.dump(todos, f)
    f.close()


if __name__ == "__main__":
    create_todo()
    read_todo(5)
    delete_todo(10)

    example_updated_todo = {
        "userId": 1,
        "id": 1,
        "title": "delectus aut autem",
        "completed": False
    }

    update_todo(24, example_updated_todo)
