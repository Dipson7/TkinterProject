from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog

YO = Tk()
YO.configure(bg='black')
YO.title('Los Blancos')
YO.iconbitmap('C:/Users/dipso/OneDrive/Pictures/Softwarica/RM.ico')


def open():
    global my_image
    YO.filename = filedialog.askopenfilename(initialdir="C:/Users/dipso/OneDrive/Pictures/Softwarica",
                                               title="Select a file",
                                               filetypes=(("png files", "*.png"),
                                                          ("all files", "*.*")))


    ml = Label(YO, text=YO.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(YO.filename))
    ml = Label(image=my_image).pack()

A = Button(YO, text="Open File", command=open,  bg="black", fg="white", font="20").pack()

C=Button(YO, text="Quit", command=YO.destroy, bg="black", fg="white").pack()

mainloop()