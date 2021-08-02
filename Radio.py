from tkinter import *
root = Tk()

root.title("Radio Button")

Toppings = [("Pepperoni", "Pepperoni"),
            ("Cheese", "Cheese"),
            ("Mushroom", "Mushroom"),
            ("Pineapple", "Pineapple"),
]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in Toppings:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked(value):
    myLabel = Label(root, text=value)
    myLabel.pack()

myButton = Button(root, text="Click", command=lambda :clicked(pizza.get())).pack()

mainloop()
