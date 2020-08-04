from tkinter import *

root = Tk()
root.title("Checkboxes")
root.iconbitmap("imagenes/python.ico")
root.geometry("400x400")


def show():
    mylabel = Label(root, text=var.get()).pack()


var = StringVar()

c = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off")
c.deselect()
c.pack()

myButton = Button(root, text="show Selection", command=show).pack()

mainloop()
