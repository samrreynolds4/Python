from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.showMenu()

    def showMenu(self):
        self.x_entry = Entry(self).grid(column=0, row=0)
        self.x_label = Label(self, text="X pos").grid(column=1, row=0)

        self.y_label = Label(self, text="Y pos").grid(column=1, row=1)
        self.y_entry = Entry(self).grid(column=0, row=1)

        self.force_label = Label(self, text="Force: ").grid(column=1, row=2)
        self.force_entry = Entry(self).grid(column=0, row=2)

        self.accel_label = Label(self, text="Acceleration: ").grid(column=1, row=3)
        self.acceleration_entry = Entry(self).grid(column=0, row=3)
        
        

class graphPoint(object):
    def __init__(self, x, y, force, acceleration):
        self.x = x
        self.y = y
        self.force = force
        self.acceleration = acceleration

    
    def setCoord(self, x, y):
        self.x = x
        self.y = y

    def setForce(self, f):
        self.force = f

    def setAcceleration(self, a):
        self.acceleration = a

##------Main
root = Tk()
root.title("Graph")
root.geometry("300x300")

app = Application(root)
root.mainloop()
