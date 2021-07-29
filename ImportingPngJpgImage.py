from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title("Image insertion")

root.iconbitmap('C:/Users/dipso/OneDrive/Pictures/Softwarica/Cal.ico')

my_image = ImageTk.PhotoImage(Image.open('C:/Users/dipso/OneDrive/Pictures/Softwarica/panda.jpg'))
my_label = Label(image=my_image)
my_label.pack()

quit_image = ImageTk.PhotoImage(Image.open('C:/Users/dipso/OneDrive/Pictures/Softwarica/dice.png'))
button_quit = Button(root, image=quit_image, command=root.quit)
button_quit.pack()

root.mainloop()