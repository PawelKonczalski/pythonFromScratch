import requests
import json
import webbrowser
import random 

params = {
    'breed_ids': 'beng',
    'limit': 5
}

r = requests.get('https://api.thecatapi.com/v1/images/search?', params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print('Bad requests')
else:
    for catImg in content:
         webbrowser.open_new_tab(catImg['url'])

      
