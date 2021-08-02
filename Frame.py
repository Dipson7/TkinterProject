from tkinter import *
root = Tk()

Frame = LabelFrame(root, text="frame", padx=5, pady=5)
Frame.pack(padx=10, pady=10)
myButton = Button(Frame, text="Click Me")
myButton.pack()

root.mainloop()
