class Node(object):

    E = None
    
    def _init_(self, E):
        self.E = E
        self.Left  = Node(None)
        self.Right = Node(None)
        
    def setElement(self, Element):
        self.E = Element

    def getElement(self):
        return self.E

    def compare(self, E2):
        if self.E > E2:
            return 1
        elif self.E < E2:
            return -1
        else:
            return 0

new = Node(10)
new.Left = Node(4)

print(new.getElement())
