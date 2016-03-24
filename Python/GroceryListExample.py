def showRemoveMenu(groceryList):
    x = 10
    userRemoval = -1
    
    print("/" * x)
    print("/" * int(x / 4) + str(groceryList))

    for i in range(len(groceryList)):
        print("/" * int(x / 4) + str(i+1) + ".", str(groceryList[i]))
    
    while not(0 < int(userRemoval) < len(groceryList)):
        userRemoval = input("Enter the item number you would like to remove: ")
    
        
    if userRemoval:
        print("Removing ", groceryList[int(userRemoval)])

        groceryList.remove(groceryList[int(userRemoval) - 1])
        showRemoveMenu(groceryList)
    else:
        printMenu()

def showAddMenu(groceryList):
    x = 10
    userItem = " "
    
    print("/" * x)
    while userItem:
        userItem = input("/" * int(x / 4) + " Enter an item: ")
        groceryList.append(userItem)
        
    print("/" * x)
    printMenu(groceryList)

def printMenu(groceryList):
    x = 10

    print(groceryList)
    print("/" * x)
    print("/" * int(x / 4) + "press 1 - 2 tp select a menu item")
    print("/" * int(x / 4) + "1. Add items")
    print("/" * int(x / 4) + "2. Remove items")
    print("/" * x)

    userSelection = input("Enter your menu selection: ")
    if userSelection == "1":
        showAddMenu(groceryList)
    elif userSelection == "2":
        showRemoveMenu(groceryList)
    else:
        printMenu(groceryList)
    

def main():
    size = 6
    groceryList = ["test", "test2", "test3"]
    printMenu(groceryList)
    
    
main()
