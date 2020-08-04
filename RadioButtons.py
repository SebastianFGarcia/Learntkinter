from tkinter import *

root = Tk()
root.title("Radio Buttons")
root.iconbitmap('imagenes/python.ico')

# r = IntVar()
# r.set("2")

MODES = [
    ("Pollo", "Pollo"),
    ("Hawaiana", "Hawaiana"),
    ("Carne", "Carne"),
    ("Mexicana", "Mexicana"),
]

pizza = StringVar()
pizza.set("Pollo")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def click(value):
    milabel1 = Label(root, text=value)
    milabel1.pack()


# Radiobutton(root, text="Opcion 1", variable=r, value=1, command=lambda: click(r.get())).pack()
# Radiobutton(root, text="Opcion 2", variable=r, value=2, command=lambda: click(r.get())).pack()

miLabel = Label(root, text=pizza.get())
miLabel.pack()

myButton = Button(root, text="Click me!", command=lambda: click(pizza.get()))
myButton.pack()

root.mainloop()
