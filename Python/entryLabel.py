from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()


        self.create_stuff()

    def create_stuff(self):
        self.btn1 = Button(self, text="SUBMIT WORD")
        self.btn1.grid(row=4, column=2)
        self.btn1.configure(command=self.submit)
        self.word = Entry(self)
        self.word.grid(row=1, column=2)
        
    def submit(self):
        if self.word.get() == "":
            self.wText = "NO"
        else:
            self.wText = self.word.get()

        self.temp = Button(self, text=self.wText, command=self.theCommand).grid()
        

    def theCommand(self):
        Label(self, text="YOU PRESSED IIIT" + self.wText).grid()
        
##------ Main
root = Tk()
root.title("MAH WINDOOOW")
root.geometry("300x300")

app = Application(root)
root.mainloop()
