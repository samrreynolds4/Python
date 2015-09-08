

class List:
    def __init__(self, E):
        self.Head = Node(E)
        print("nothing in the head man")
        self.current = self.Head
        if E != None:
            self.size = 1
        else:
            self.size = 0
            
        self.index = 0

    def add(self, E):
        
        if self.Head.data == None:
            print("nothing in the head man")
            self.Head = Node(E)
            self.current = self.Head
            self.size = 1
        else:
            self.current.next = Node(E)
            self.current.previous = self.current
            self.current = self.current.next
            self.index += 1
            self.size += 1
        
    def Iter_Next(self):
        if self.current != None:
            self.previous = self.current
            self.current = self.current.next
            self.index += 1
            return self.previous.data
        else:
            print("Nothing there!")

    def iter_Prev(self):
        if self.current != None & self.index != 0:
            previous = self.current
            self.current = self.current.previous
            self.index -= 1
            return previous.data
        else:
            return current.data
    
    
    def Iter_Head(self):
        self.current = self.Head

    def indexOf(self, num):
        if num > (self.size-1):
            print("index too big!")
        elif num == 0:
            return self.Head.data
        else:
            self.current = self.Head
            self.index = 0
                
            for i in range(num):
                print(i)
                print(self.Iter_Next())

            return self.current.data


class Node(object):
    def __init__(self, E):
        self.data = E
        self.next = None
        self.previous = None
    


def facto(num):
    n = 1
    for i in range(num):
        n *= num - i
    return n

def linearSearch(index):
    print(elements.indexOf(index))
    if index < elements.size-1:
        i=index+1
        for i in range(elements.size):
            print(elements.indexOf(i))
        index += 1
        linearSearch(index)
    else:
        print("done")


##---------Main----------##
elements = List(None)
pairs = 1
while(pairs <= 1):  
    pairs = int(input("Enter how many go into a pair: "))
recurse = pairs
while(1):

    element = input("Enter element: ")
    print(elements.size)
    
    if element == "":
        if elements.size < pairs:
            print("Enter at least ", pairs - elements.size, " more elements")
        else:
            break
    else:
        elements.add(element)

n = elements.size
print("facto size: ", facto(n))
print(facto(5))
print("facto pairs: ", facto(pairs))
print("facto k: ", facto(n - pairs))
unique = (facto(elements.size)) / (facto(pairs) * (facto(elements.size - pairs)))
linearSearch(0)


            
        
    

        
