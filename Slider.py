from tkinter import *

SUP = Tk()
SUP.configure(bg='black')
SUP.title('Slider')
SUP.iconbitmap('C:/Users/dipso/OneDrive/Pictures/Softwarica/RM.ico')

#Vertical Slider

vertical = Scale(SUP, from_=0, to=450, bg="black", fg="white")
vertical.pack()

#Horizontal Slider
horizontal = Scale(SUP, from_=0, to=450, orient=HORIZONTAL, bg="black", fg="white")
horizontal.pack()

#my_label = Label(SUP, text=horizontal.get()).pack()
#Function slide craeated
def slide():
    my_label = Label(SUP, text=horizontal.get()).pack()

    SUP.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

#Function called
my_btn = Button(SUP, text="Click Me", command=slide, bg="black", fg="white").pack()

mainloop()