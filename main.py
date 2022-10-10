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
    
def update_todo(idg):
    f = open("todos.json", "w")
    todos = json.load(f)
    mod_todos = {}
    for todo in todos:
        if todo["userId"] == idg:
            mod_todos.append(todo)
    #for todo in mod_todos:
        #edit todos
    #for todo in todos                                  #merge todos
        #for todom in mod_todos
            #if todo["userId"] == todom["userId"] and todo["id"] == todom["id"]:
                #todo = todom
    json.dump(todos, f)
    return mod_todos
    
    

def delete_todo(idg):
    f = open("todos.json", "r")
    todos = json.load(f)
    for i in range(len(todos)):
        if todos[i]['id'] == idg:
            del todos[i]
    json.dump(todos, f)

delete_todo(23)
    



    
