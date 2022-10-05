from email.utils import parsedate
import json
from tokenize import group
import requests


TODO_API_URL = "https://jsonplaceholder.cypress.io/todos"

def create_todo():
    response = requests.get(TODO_API_URL)
    with open("todos.json", "w") as f:
        json.dump(response.json(), f)
    
create_todo()

def read_todo(idg):
    f = open("todos.json", "r")
    todos = json.load(f)
    group_todos = {}
    for todo in todos:
        id = todo["userId"]    
        if id not in group_todos:
            group_todos[id] = []
        group_todos[id].append(todo)
    for todo in group_todos[idg]:
        print(todo) 
    
    

read_todo(3)
    
