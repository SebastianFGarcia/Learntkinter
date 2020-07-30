from tkinter import *

root = Tk()
#Creando labels
#myLabel1 = Label(root, text="hello wold").grid(row=0, column=0)
#myLabel2 = Label(root, text="hello wold").grid(row=1, column=2)
#myLabel3 = Label(root, text="hello wold").grid(row=2, column=3)
#Creando botones
def myClick():
    myLabel1 = Label(root, text="hello wold")
    myLabel1.pack()

myButton = Button(root, text="hola", padx=50, pady= 10, command= myClick )
myButton.pack()

root.mainloop()
