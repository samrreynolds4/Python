from tkinter import *
import random

class Application(Frame):
    ##---- this will hold a frame of stuff
    def __init__(self, master):
        ## starts the frame
        super(Application, self).__init__(master)
        self.grid()

        self.btn_clicks = 0
        self.row = 0
        self.column = 0
        self.word = ("TEXT", "MWAHAHAHA", "ALSO A TEXT", "DUN DUN DUUUUUN", "CRUNCHY PEANUT BUTTER", "COOKIE")
        self.create_widgets()
       
    
    def create_widgets(self):
        ## CREATES SOME STUFF

        self.btn1 = Button(self)
        self.btn1["text"] = "TEXXXT"
        self.btn1.grid()

        self.btn2 = Button(self, text="this is a test")
        self.btn2.configure(command=self.theAction)
        self.btn2.grid()

    def theAction(self):
        self.rCol = random.randint(1, 10)
        self.rRow = random.randint(1,  20)
        
        self.btn_clicks += 1
        print("clicked")
        self.btn2["text"] = "Clicks: " + str(self.btn_clicks)
        
        Label(self, text=self.word[random.randint(0, 5)]).grid(row=self.rRow, column=self.rCol)
        

## ----- MAIN

root = Tk()

root.title("mah window")
root.geometry("200x200")

app = Application(root)
root.mainloop()

