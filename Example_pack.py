from tkinter import *
root = Tk()
redbutton = Button(root, text="LEFT", fg="green") #this is to create buttons in python
redbutton.pack(side=LEFT) #this is to show it to the screen
redbutton = Button(root, text="RIGHT", fg="blue")
redbutton.pack(side=RIGHT)
redbutton = Button(root, text="TOP", fg="black")
redbutton.pack(side=TOP)
redbutton = Button(root, text="BOTTOM", fg="red")
redbutton.pack(side=BOTTOM)

root.mainloop()