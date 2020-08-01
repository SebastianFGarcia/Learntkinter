from tkinter import *

root = Tk()
root.iconbitmap('imagenes/python.ico')
root.title("Sliders")
root.geometry("400x400")

vertical = Scale(root, from_=0, to=400)
vertical.pack()

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

my_label = Label(root, text=horizontal.get()).pack()


def slide():
    my_label = Label(root, text=str(horizontal.get()) + "x" + str(vertical.get())).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


my_btn = Button(root, text="Click me!", command=slide).pack()
mainloop()
