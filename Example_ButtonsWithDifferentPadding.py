from tkinter import *
root = Tk()

#Button without any functions
myButton = Button(root, text="Click me")
myButton.pack()

#State disables button
myButton1 = Button(root, text="Click", state=DISABLED)
myButton1.pack()

#Button x and y  padding
myButton2 = Button(root, text="Click", padx=50)
myButton2.pack()
myButton3 = Button(root, text="Click", padx=50, pady=50)
myButton3.pack()

root.mainloop()

