import json
import pprint

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
encodeMovie = json.dumps(movie, ensure_ascii=False, indent=4)

with open('sample.json', 'w', encoding='UTF-8') as file:
    json.dump(movie, file, ensure_ascii=False)

print(encodeMovie)

with open('sample.json', encoding='UTF-8') as file:
    result = json.load(file)

#print(json.dumps(result, indent=4, ensure_ascii=False))

pprint.pprint(result)
