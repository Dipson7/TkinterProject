from tkinter import *
from PIL import ImageTk, Image


wassup = Tk()
wassup.configure(bg='black')

# title
wassup.title('                                                                                               REAL MADRID')

# icon images
# png icons does not support sometimes
wassup.iconbitmap('C:/Users/dipso/OneDrive/Pictures/Softwarica/RM.ico')

my_image1 = ImageTk.PhotoImage(Image.open("C:/Users/dipso/OneDrive/Pictures/Softwarica/benzema.png"))
my_image2 = ImageTk.PhotoImage(Image.open("C:/Users/dipso/OneDrive\Pictures/Softwarica/modric.png"))
my_image3 = ImageTk.PhotoImage(Image.open("C:/Users/dipso/OneDrive\Pictures/Softwarica/kroos.png"))
my_image4 = ImageTk.PhotoImage(Image.open("C:/Users/dipso/OneDrive\Pictures/Softwarica/marcelo.png"))

image_list = [my_image1, my_image2, my_image3, my_image4]

# adding a status bar at end
#1.
#status = Label(wassup, text="Image 1 of 5")
#2. image_list passed to get total number of list
#status = Label(wassup, text="1 of " + str(len(image_list)))
#3. status to be with border and shrinken with align on east
status = Label(wassup, text="1 of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E, bg="black", fg="white")


my_label = Label(image= my_image1)
my_label.grid(row=0, column=0, columnspan=3)

# function for forward image
def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(wassup, text=">>", command= lambda : forward(image_number + 1))
    button_back = Button(wassup, text="<<", command= lambda : back(image_number -1))

    if image_number== 5:
        button_forward=Button(wassup,text=">>", state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

# status change during image change
    status = Label(wassup, text= str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2,column=0,columnspan=3, sticky=W+E, bg="black", fg="white")

# function for backward image
def back(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(wassup, text=">>", command= lambda : forward(image_number + 1))
    button_back = Button(wassup, text="<<", command= lambda : back(image_number -1))

    if image_number == 1:
        button_back=Button(wassup,text="<<", state=DISABLED)

    my_label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)

    # status change during image change -- update status bar
    status = Label(wassup, text=str(image_number) + " of " + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


button_back = Button(wassup, text="<<", command=back, state=DISABLED, bg="black", fg="white", font="20", bd=0)
# Button quit option
button_quit = Button(wassup, text="Exit", command=wassup.quit, bg="black", fg="white", font="20", bd=0)
button_forward = Button(wassup, text=">>", command=lambda: forward(2), bg="black", fg="white", font="20", bd=0)


button_back.grid(row=1, column=0)
button_quit.grid(row=1, column=1)
button_forward.grid(row=1, column=2, pady=10)
# adding pady =10 for gap within status and button
# 1. status.grid(row=2,column=0,columnspan=3)
# sticky --> direction or stretch
status.grid(row=2,column=0,columnspan=3, sticky=W+E)

wassup.mainloop()