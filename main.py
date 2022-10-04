from email.utils import parsedate
import json
import requests
import json

TODO_API_URL = "https://jsonplaceholder.cypress.io/todos"

def save_todos():
    response = requests.get(TODO_API_URL)
    with open("todos.json", "w") as f:
        json.dump(response.json(), f)
    f.close()

save_todos()

