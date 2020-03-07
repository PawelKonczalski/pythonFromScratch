import requests
import json

r = requests.get('https://jsonplaceholder.typicode.com/todos')

#tasks = json.loads(r.text)
try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print('Wrong format')
else:
    print('ok')
    print(tasks[0:4])
