import time

def function_performance(func, how_many_times = 1, *arg):
    sum = 0
    
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sum = sum + (end-start)
        
    return sum

setContainer = {i for i in range(100000)}
listContainer = [i for i in range(100000)]

def findElement(itemSought, containerName):
    return itemSought in containerName
    
print(function_performance(findElement, 200, 1534, setContainer))
print(function_performance(findElement, 200, 1534, listContainer))
