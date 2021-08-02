from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

root=Tk()

root.title('New Window')
root.iconbitmap('C:/Users/dipso/OneDrive/Pictures/Softwarica/RM.ico')

def show():
    myLabel=Label(root, text=clicked.get()).pack()

clicked=StringVar()
clicked.set("Monday")

drop=OptionMenu(root, clicked,"Monday","Tuesday","Wednesday""Thursday","Friday","Sunday")
drop.pack()

myButton=Button(root, text="Show selection", command=show).pack()

mainloop()