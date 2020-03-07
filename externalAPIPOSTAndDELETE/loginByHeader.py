import requests
import json
import webbrowser
import credentials

def getJSONContentFromResponse(response):   
    try:
        content = response.json()
    except json.decoder.JSONDecodeError:
        print('Bad requests')
    else:
        return content
        
def getFavouriteCats(userId):
    params = {
        'sub_id': userId
        }
    
    r = requests.get('https://api.thecatapi.com/v1/favourites',
                     params,
                     headers=credentials.headers)
    return getJSONContentFromResponse(r)

def getRandomCat():
    r = requests.get('https://api.thecatapi.com/v1/images/search',
                     headers=credentials.headers)
    return getJSONContentFromResponse(r)

userId = 'wit2020'
name = 'Witlacy'

print('Hello', name)
favouriteCats = getFavouriteCats(userId)
print('Your favorites cats is:', favouriteCats) 
randomCat = getRandomCat()
print(randomCat[0]['url'])
