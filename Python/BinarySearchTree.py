class Node(object):
    E = None

    def __init__(self, E):
        self.E = E
        self.Left = None
        self.Right = None

    def compare(self, E2):
        if self.E > E2:
            return 1
        elif self.E < E2:
            return -1
        else:
            return 0

class BST(object):
    Size = 0
    
    def __init__(self):
        self.root = Node(None)
        self.Navigator = self.root
    
    def add(self, E):
        ++self.Size
        current = self.root
        new = Node(E)
        parent = current
        if self.root.E == None:
            self.root = Node(None)
        else:
            while current.E:
                
                if new.compare(current.Left.E < 0):
                    parent = current
                    current = current.Left
                elif new.compare(current.Right.E > 0):
                    parent = current
                    current = current.Right
                else:
                    break
            
        if new.compare(parent.E) < 0:
            new.Left = parent.Left
            parent.Left = new.Left
        else:
                new.Right = parent.Right
                parent.Right = new.Right

        print("Added")
    

    def printRoot(self):
        print(self.root.E)

    def Left(self):
        print(self.root.Left.E)
        Navigator = root.Left

    def Right(self):
        print(self.root.Right.E)
        Navigator = root.Right

    def Root(self):
        print(root.E)
        Navigator = root
            
Tree = BST()
Tree.add(1)
Tree.add(4)
Tree.add(10)
Tree.add(12)
Tree.add(29)
Tree.add(30)

Tree.Root()
Tree.Left()
Tree.Left()

       
        
    

