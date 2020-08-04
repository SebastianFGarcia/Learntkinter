from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Cuadros de Mensajes")
root.iconbitmap('imagenes/python.ico')


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesnocancel("Este es mi popup!", "Hello world!")
    if response == 1:
        Label(root, text="yes").pack()
    elif response == 0:
        Label(root, text="no").pack()
    else:
        root.quit()


Button(root, text="Popup", command=popup).pack()

root.mainloop()
