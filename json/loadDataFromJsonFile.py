import json

encodeRetrieveMovie = '{"title": "Jocker", "release_year": 2019, "won_oscar": true, "actors": ["Joaquin Phoenix", "Robert De Niro", "Frances Conroy"], "budget": "55–70 mln", "credits": {"director": "Todd Phillips", "writer": "Scott Silver", "animation": null}}'

#print(json.loads(encodeRetrieveMovie))

with open('sample.json', encoding='UTF-8') as file:
    print(json.load(file))
