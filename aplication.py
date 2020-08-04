from tkinter import *

root = Tk()
# Creando labels
###myLabel1 = Label(root, text="hello wold").grid(row=0, column=0)
###myLabel2 = Label(root, text="hello wold").grid(row=1, column=2)
###myLabel3 = Label(root, text="hello wold").grid(row=2, column=3)

# Creando Cajas de Texto
# BG = Background
# Borderwidth = Borde
e = Entry(root, width=50)
e.pack()
e.insert(0, "Escriba algo")


# e.get() extrae el texto
# Creando botones
def myClick():
    myLabel1 = Label(root, text=e.get())
    myLabel1.pack()


# Text= texto del boton
# Padx=ancho del boton
# Pady = alto del boton
# Command = Funciones que hace el boton
# Fg = colores de las letras
# Bg = Background del boton
# myButton = Button(root, text="hola", padx=50, pady= 10, command= myClick, fg="blue", bg="green")
myButton = Button(root, text="hola", command=myClick)
myButton.pack()

root.mainloop()
