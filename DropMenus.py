from tkinter import *

root = Tk()
root.iconbitmap("imagenes/python.ico")
root.title("Drop Menus")
root.geometry("400x400")


def show():
    myLabel = Label(root, text=clicked.get()).pack()


options = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", ]
clicked = StringVar()
clicked.set(options[0])
drop = OptionMenu(root, clicked, *options)
drop.pack()

myButton = Button(root, text="Click me!", command=show).pack()

mainloop()
