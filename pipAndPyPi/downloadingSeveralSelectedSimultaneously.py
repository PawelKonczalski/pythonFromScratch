import requests
import json

r = requests.get("https://jsonplaceholder.typicode.com/todos")

def countTaskFrequency(tasks):
    completedTaskFrequencyByUser = dict()
    for entry in tasks:
        if(entry["completed"] == True):
            try:
                completedTaskFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTaskFrequencyByUser[entry["userId"]] = 1

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


r = requests.get("https://jsonplaceholder.typicode.com/users")
users = r.json()

for user in users:
    if (user["id"] in usersWithTopCompletedTasks):
        print("Give rewart user: ", user["name"])
        usersWithTopCompletedTasks.remove(user["id"])
