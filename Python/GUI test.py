from tkinter import *

##------- Main -------
root = Tk()
root.title("mah windowwwww")
root.geometry("100x200")


app = Frame(root)
app.grid()

button = Button(app, text = "This is a Button :D")
button.grid()

button2 = Button(app)
button2.configure(text="BUTTONSSSSSSS")
button2.grid()
button3 = Button(app)
button3["text"] = "THIS IS MY TEXT"
button3.grid()

root.mainloop()
