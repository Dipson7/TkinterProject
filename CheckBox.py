from tkinter import*

check=Tk()
check.configure(bg='black')

check.title('New Window')
check.iconbitmap('C:/Users/dipso/OneDrive/Pictures/Softwarica/RM.ico')

def show():
    myLabel=Label(check, text=var.get()).pack()
    
var=StringVar()

#anything can be written in on/off string input
checkButton=Checkbutton(check, text="Check this box", variable=var, onvalue="On", offvalue="Off")

#Checkbox is selected automatically on default
checkButton.deselect()
checkButton.pack()

myButton=Button(check, text="Show Selection", command=show, bg="black", fg="white").pack()

mainloop()

