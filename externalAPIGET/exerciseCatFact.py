import requests
import json
import webbrowser
import random 

choice = input('''if you want to know 5 facts about:
cats click 1
dogs click 2
Your choice: ''')

if choice == '1':
    animal = 'cat'
elif choice == '2':
    animal = 'dog'
else:
    animal = random.choice(('cat', 'dog'))
    

params = {
    'amount': 5,
    'animal_type': animal
}

r = requests.get('https://cat-fact.herokuapp.com/facts/random', params)

try:
    content = r.json()
except json.decoder.JSONDecodeError:
    print('Bad requests')
else:
    for cat in content:
         print(cat['text'])
         print()
       

