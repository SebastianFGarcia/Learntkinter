from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Imagenes")

#Icono de la aplicacion
root.iconbitmap('imagenes\python.ico')


my_image = ImageTk.PhotoImage(Image.open("imagenes\python.png"))
my_label = Label(image = my_image,pady=100,padx=100).pack()

#boton de salida
button_exit = Button(root,text="Salida", command=root.quit)
button_exit.pack()

root.mainloop()