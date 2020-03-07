import requests
import json
import pprint

params = {
    'site': 'stackoverflow',
    'sort': 'votes',
    'order': 'desc',
    'fromdate': '2020-03-01',
    'tagged': 'python',
    'min': 10
    
}

r = requests.get('https://api.stackexchange.com/2.2/questions', params)

try:
    questions = r.json()
except json.decoder.JSONDecodeError:
    print('Bad requests')
else:
    pprint.pprint(questions)
