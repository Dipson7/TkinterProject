from tkinter import *
root = Tk()

def myClick():
    myLabel = Label(root, text="Button is clicked")
    myLabel.pack()

myButton = Button(root, text="Click", command=myClick, fg="black", bg="gray")
myButton.pack()

root.mainloop()