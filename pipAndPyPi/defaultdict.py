import requests
import json
from collections import defaultdict

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def countTaskFrequency(tasks):
    completedTaskFrequencyByUser = defaultdict(int)
    for entry in tasks:
        if(entry["completed"] == True):
           completedTaskFrequencyByUser[entry["userId"]] += 1


    return completedTaskFrequencyByUser

def getKeysWithTopValues(myDict):
    return [
        key
        for (key, value) in my_dict.items()
        if value == max(myDict.values())
    ] 

def getUsersWithTopCompletedTasks(completedTaskFrequencyByUser):
    usersIdWithMaxCompletedAmountOfTasks = []    
    maxAmountOfCompletedTask = max(completedTaskFrequencyByUser.values())
    for userId, numberOfCompletedTask in completedTaskFrequencyByUser.items():
        if (numberOfCompletedTask == maxAmountOfCompletedTask):
            usersIdWithMaxCompletedAmountOfTasks.append(userId)

    return usersIdWithMaxCompletedAmountOfTasks

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Wrong format")
else:
    completedTaskFrequencyByUser = countTaskFrequency(tasks)
    usersWithTopCompletedTasks = getUsersWithTopCompletedTasks(completedTaskFrequencyByUser)
    print("Give rewart user id: ", usersWithTopCompletedTasks)
'''
#1
r = requests.get("https://jsonplaceholder.typicode.com/users")
users = r.json()

for user in users:
    if (user["id"] in usersWithTopCompletedTasks):
        print("Give rewart user: ", user["name"])
        usersWithTopCompletedTasks.remove(user["id"])

#2
for userId in usersWithTopCompletedTasks:
    #r = requests.get("https://jsonplaceholder.typicode.com/users/")
    r = requests.get("https://jsonplaceholder.typicode.com/users", params="id="+str(userId))
    user = r.json()
    #print("Give rewart user: ", user["name"])
    print("Give rewart user: ", user[0]["name"])
#3
def changeListIntoConjOfParam(myList, key="id"):
    conjParam = key + "="
    
    lastIteration = len(myList)
    i = 0
    for item in myList:
        i += 1
        if (i == lastIteration):
            conjParam += str(item)
        else:
            conjParam += str(item) + "&" + key + "="
    
    return conjParam
    
conjParam = changeListIntoConjOfParam(usersWithTopCompletedTasks, "id")
#conjParam = changeListIntoConjOfParam([2,7,4])
r = requests.get("https://jsonplaceholder.typicode.com/users", params=conjParam)   

users = r.json()
for user in users:
    print("Give rewart user: ", user["name"])
'''
