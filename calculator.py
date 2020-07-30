from tkinter import *

root = Tk()
root.title("Calculadora")

Ctext = Entry(root, width=40, borderwidth=5)
Ctext.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


#
def button_click(number):
    current = Ctext.get()
    Ctext.delete(0, END)
    Ctext.insert(0, str(current) + str(number))
    return


def button_clear():
    Ctext.delete(0, END)


def button_suma():
    primer_numero = Ctext.get()
    global f_num
    global operacion
    operacion = "suma"
    f_num = float(primer_numero)
    Ctext.delete(0, END)


def button_resta():
    primer_numero = Ctext.get()
    global f_num
    global operacion
    operacion = "resta"
    f_num = float(primer_numero)
    Ctext.delete(0, END)


def button_multiplicacion():
    primer_numero = Ctext.get()
    global f_num
    global operacion
    operacion = "multiplicacion"
    f_num = float(primer_numero)
    Ctext.delete(0, END)


def button_divicion():
    primer_numero = Ctext.get()
    global f_num
    global operacion
    operacion = "divicion"
    f_num = float(primer_numero)
    Ctext.delete(0, END)


def button_equal():
    segundo_numero = Ctext.get()
    Ctext.delete(0, END)
    if operacion == "suma":
        Ctext.insert(0, f_num + float(segundo_numero))
    elif operacion == "resta":
        Ctext.insert(0, f_num - float(segundo_numero))
    elif operacion == "multiplicacion":
        Ctext.insert(0, f_num * float(segundo_numero))
    elif operacion == "divicion":
        Ctext.insert(0, f_num / float(segundo_numero))


# definir botones
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))

button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))

button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

button_suma = Button(root, text="+", padx=39, pady=20, command=button_suma)
button_resta = Button(root, text="-", padx=40, pady=20, command=button_resta)
button_multiplicacion = Button(root, text="x", padx=40, pady=20, command=button_multiplicacion)
button_divicion = Button(root, text="/", padx=40, pady=20, command=button_divicion)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_suma.grid(row=5, column=0)
button_resta.grid(row=5, column=1)
button_multiplicacion.grid(row=5, column=2)
button_divicion.grid(row=6, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=6, column=1, columnspan=2)

root.mainloop()
