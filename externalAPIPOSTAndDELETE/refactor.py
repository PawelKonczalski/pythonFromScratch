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
    return getJSONContentFromResponse(r)[0]

def addFavouriteCat(catId, userId):
    catData = {
        'image_id': catId,
        'sub_id': userId
        }
    
    r = requests.post('https://api.thecatapi.com/v1/favourites/',
                    json = catData,
                    headers=credentials.headers)
    return getJSONContentFromResponse(r)

def removeFavoriteCat(userId, favouritCatId):
    r = requests.delete('https://api.thecatapi.com/v1/favourites/'+favouritCatId,
                    headers=credentials.headers)
    return getJSONContentFromResponse(r)

userId = 'wit2020'
name = 'Witlacy'

print('Hello', name)
favouriteCats = getFavouriteCats(userId)
print('Your favorites cats is:', favouriteCats) 
randomCat = getRandomCat()
print(randomCat['url'])

addToFavourites = input('Do you want to add this cat to favorite? Y/N: ')

if(addToFavourites.upper() == 'Y'):
    resultFromAddingFavouriteCat = addFavouriteCat(randomCat['id'], userId)
    newAddedCatInfo = {resultFromAddingFavouriteCat['id']: randomCat['url']}
else:
    print('Something go wrong')
newAddedCatInfo = {}
favouriteCatsById = {
    favouriteCat['id']: favouriteCat['image']['url']
    for favouriteCat in favouriteCats
    }
favouriteCatsById.update(newAddedCatInfo)

print(favouriteCatsById)

favouritCatId = input('do you want to delete cat form favorite? Enter cat id: ')
    
print(removeFavoriteCat(userId, favouritCatId))
