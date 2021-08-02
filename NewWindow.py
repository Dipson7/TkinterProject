from tkinter import*
from PIL import ImageTk, Image
from tkinter import messagebox

LOL=Tk()
LOL.configure(bg='black')

LOL.title('New Window')
LOL.iconbitmap('C:/Users/dipso/OneDrive/Pictures/Softwarica/RM.ico')

def open():
    global my_img
    top= Toplevel()
    top.configure(bg='black')
    top.title('KING KARIM')
    top.iconbitmap('C:/Users/dipso/OneDrive/Pictures/Softwarica/RM.ico')
    my_img=ImageTk.PhotoImage(Image.open("C:/Users/dipso/OneDrive/Pictures/Softwarica/benzema.png"))
    my_label=Label(top, image=my_img).pack()

    A=Button(top, text="Quit", command=top.destroy, bg="black", fg="white", font="50").pack()

B=Button(LOL, text="The Best Number 9", command=open, bg="black", fg="white", font="20").pack()

C=Button(LOL, text="Quit", command=LOL.destroy, bg="black", fg="white").pack()

LOL.mainloop()