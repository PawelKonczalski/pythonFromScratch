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

def addFavouriteCat(catId, userId):
    catData = {
        'image_id': catId,
        'sub_id': userId
        }
    
    r = requests.post('https://api.thecatapi.com/v1/favourites/',
                    json = catData,
                    headers=credentials.headers)
    return getJSONContentFromResponse(r)   

userId = 'wit2020'
name = 'Witlacy'

print('Hello', name)
favouriteCats = getFavouriteCats(userId)
print('Your favorites cats is:', favouriteCats) 
randomCat = getRandomCat()
print(randomCat[0]['url'])

addToFavourites = input('Do you want to add this cat to favorite? Y/N: ')

if(addToFavourites.upper() == 'Y'):
    print(addFavouriteCat(randomCat[0]['id'], userId))
else:
    print('Something go wrong')
    

