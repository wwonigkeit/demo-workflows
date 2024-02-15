import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)

# Pretty Printing JSON string back
print(json.dumps(todos, indent = 4, sort_keys=True))