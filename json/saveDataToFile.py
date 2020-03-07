import json

movie = {
    "title" : "Jocker",
    "release_year" : 2019,
    "won_oscar" : True,
    "actors": ("Joaquin Phoenix", "Robert De Niro", "Frances Conroy"),
    "budget" : "55–70 mln",
    "credits" : {
            "director" : "Todd Phillips",
            "writer" : "Scott Silver",
            "animation" : None
            }
}

#print(json.dumps(movie))
print(json.dumps(movie, ensure_ascii=False))

with open('sample.json', 'w', encoding='UTF-8') as file:
    json.dump(movie, file, ensure_ascii=False)
