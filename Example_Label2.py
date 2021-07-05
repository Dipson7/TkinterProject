from tkinter import *
root = Tk()

#To create a label widget
myLabel1 = Label(root, text="Tkinter Program Beginning")
myLabel2 = Label(root, text="I am Groot")
myLabel3 = Label(root, text="Sup Rocket")

#To show it to the screen based on x-axis and y-axis
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)

root.mainloop()

