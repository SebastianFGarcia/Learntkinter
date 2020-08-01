from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Archivos")
root.iconbitmap('imagenes/python.ico')


def open():
    global my_img
    root.filename = filedialog.askopenfilename(initialdir="imagenes/", title="Seleccione un archivo",
                                               filetypes=(("Png", "*.png"), ("Todos los Archivos", "*.*")))
    label = Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    label2 = Label(root, image=my_img).pack()


btn = Button(root, text="Abrir Archivo", command=open).pack()

mainloop()
