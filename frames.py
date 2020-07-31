from tkinter import *

root = Tk()
root.title("Frames")
root.iconbitmap('imagenes/python.ico')

frame = LabelFrame(root, text="Este es mi Cuadro", padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="No haga Clic aca ")
b.pack()

root.mainloop()
