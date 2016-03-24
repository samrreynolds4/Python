import random

def createList(size):
    theList = list()
    n = 0
    while n < size:
        rand = round(random.random()*10000)
        theList.append(rand)
        n = n + 1

    return theList
    


arr = createList(1000)
num = arr[0]
n = 0
while (n < 1000):
    if (arr[n] < num):
        num = arr[n]
    else:
        n = n + 1

print(num)
