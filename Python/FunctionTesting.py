def main():
    print("start")
    for i in range(-10, 0):
        print(i)
    name = "test String"
    print(name[2:5])
    print(name)
    myList = list((10, 20, 30, 40))
    print(myList[0])
    myList.remove(10)
    print(myList[0])
    myList.remove(myList[0])
    print(myList)
    
main()
