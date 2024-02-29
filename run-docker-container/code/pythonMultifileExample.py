import json
import requests
import pandas as pd

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
df = pd.read_json(json.dumps(todos, indent = 4, sort_keys=True))
df.to_csv("output.csv", index=False)