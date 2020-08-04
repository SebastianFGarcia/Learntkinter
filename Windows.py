from tkinter import *

from PIL import ImageTk, Image

root = Tk()
root.title("Base")
root.iconbitmap('imagenes/python.ico')


def open():
    global my_img
    top = Toplevel()
    label = Label(top, text="Hello world!!").pack()
    top.title("Second Window")
    top.iconbitmap('imagenes/python.ico')
    my_img = ImageTk.PhotoImage(Image.open('imagenes/3198817.svg.png'))
    Label(top, image=my_img).pack()
    btn2 = Button(top, text="Close", command=top.destroy).pack()


btn = Button(root, text="New Window!", command=open).pack()

mainloop()
