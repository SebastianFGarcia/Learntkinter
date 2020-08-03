from tkinter import *
import sqlite3

root = Tk()
root.title("Databases")
root.iconbitmap("imagenes/python.ico")
root.geometry("400x600")

# Crear base de datos o unirse a una
conn = sqlite3.connect('address_book.db')
# Crear cusror
c = conn.cursor()

# Crear las tablas
'''
c.execute("""
    CREATE TABLE addresses(
        primer_nombre text,
        segundo_nombre text,
        apellidos text,
        direccion text,
        ciudad text,
        zipcode integer
    )
""")
'''


# Crear el boton de eliminar
def delete():
    conn = sqlite3.connect('address_book.db')
    # Crear cusror
    c = conn.cursor()

    # Eliminar de la tabla
    c.execute("DELETE FROM addresses WHERE oid=" + select_box.get())
    select_box.delete(0, END)

    # Cambios del Commit
    conn.commit()

    # Cerrar conexion
    conn.close()


def submit_update():
    conn = sqlite3.connect('address_book.db')
    # Crear cusror
    c = conn.cursor()
    oid = select_box.get()
    # insertar en la tabla
    c.execute(
        "UPDATE addresses SET primer_nombre = :primer, segundo_nombre = :segundo, apellidos = :apellidos, direccion = :direccion, ciudad = :ciudad, zipcode = :zipcode  WHERE oid = :oid",
        {
            'primer': ep_nombre.get(),
            'segundo': es_nombre.get(),
            'apellidos': eapellidos.get(),
            'direccion': edireccion.get(),
            'ciudad': eciudad.get(),
            'zipcode': ezipcode.get(),
            'oid' : oid
        })

    # Cambios del Commit
    conn.commit()

    # Cerrar conexion
    conn.close()
    # limpiar las cajas de texto
    ep_nombre.delete(0, END)
    es_nombre.delete(0, END)
    eapellidos.delete(0, END)
    edireccion.delete(0, END)
    eciudad.delete(0, END)
    ezipcode.delete(0, END)
    edit.destroy()

def update():
    global edit
    edit = Tk()
    edit.title("Editar")
    edit.iconbitmap("imagenes/python.ico")
    edit.geometry("400x250")
    conn = sqlite3.connect('address_book.db')
    # Crear cusror
    c = conn.cursor()

    lp_nombre = Label(edit, text="Primer nombre: ")
    ls_nombre = Label(edit, text="Segundo nombre: ")
    lapellidos = Label(edit, text="Apellidos: ")
    ldireccion = Label(edit, text="Dirección: ")
    lciudad = Label(edit, text="Ciudad: ")
    lzipcode = Label(edit, text="Zip Code: ")

    lp_nombre.grid(row=0, column=0, padx=(20, 0), pady=(10, 5), sticky=W)
    ls_nombre.grid(row=1, column=0, padx=20, pady=5, sticky=W)
    lapellidos.grid(row=2, column=0, padx=20, pady=5, sticky=W)
    ldireccion.grid(row=3, column=0, padx=20, pady=5, sticky=W)
    lciudad.grid(row=4, column=0, padx=20, pady=5, sticky=W)
    lzipcode.grid(row=5, column=0, padx=20, pady=5, sticky=W)

    # variables Globales
    global ep_nombre, es_nombre, eapellidos, edireccion, eciudad, ezipcode

    # Cajas de texto

    ep_nombre = Entry(edit, width=30)
    es_nombre = Entry(edit, width=30)
    eapellidos = Entry(edit, width=30)
    edireccion = Entry(edit, width=30)
    eciudad = Entry(edit, width=30)
    ezipcode = Entry(edit, width=30)

    ep_nombre.grid(row=0, column=1, pady=(10, 5))
    es_nombre.grid(row=1, column=1, pady=5)
    eapellidos.grid(row=2, column=1, pady=5)
    edireccion.grid(row=3, column=1, pady=5)
    eciudad.grid(row=4, column=1, pady=5)
    ezipcode.grid(row=5, column=1, pady=5)

    # Actualizar la tabla
    c.execute("SELECT * FROM addresses WHERE oid =" + select_box.get())
    record = c.fetchone()

    ep_nombre.insert(0, record[0])
    es_nombre.insert(0, record[1])
    eapellidos.insert(0, record[2])
    edireccion.insert(0, record[3])
    eciudad.insert(0, record[4])
    ezipcode.insert(0, record[5])


    # Boton de enviar
    btn_submit_update = Button(edit, text="Actualizar", command=submit_update)
    btn_submit_update.grid(row=6, column=0, columnspan=2, pady=10, padx=20, ipadx=100)
    # Cambios del Commit
    conn.commit()

    # Cerrar conexion
    conn.close()
    edit.mainloop()


# Crear funcion de enviar
def submit():
    conn = sqlite3.connect('address_book.db')
    # Crear cusror
    c = conn.cursor()

    # insertar en la tabla
    c.execute("INSERT INTO addresses VALUES(:p_nombre, :s_nombre, :apellidos, :direccion, :ciudad, :zipcode)",
              {
                  'p_nombre': p_nombre.get(),
                  's_nombre': s_nombre.get(),
                  'apellidos': apellidos.get(),
                  'direccion': direccion.get(),
                  'ciudad': ciudad.get(),
                  'zipcode': zipcode.get(),
              }
              )

    # Cambios del Commit
    conn.commit()

    # Cerrar conexion
    conn.close()
    # limpiar las cajas de texto
    p_nombre.delete(0, END)
    s_nombre.delete(0, END)
    apellidos.delete(0, END)
    direccion.delete(0, END)
    ciudad.delete(0, END)
    zipcode.delete(0, END)


# Creamos la funcion de la consulta

def query():
    conn = sqlite3.connect('address_book.db')
    # Crear cusror
    c = conn.cursor()

    # insertar en la tabla
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    print_records = ''
    for record in records:
        print_records += f"{record[0]} {record[1]} \t {record[6]}\n"

    query_label = Label(root, text=print_records)
    query_label.grid(row=8, column=0, columnspan=2, sticky=W, padx=20)

    # Cambios del Commit
    conn.commit()

    # Cerrar conexion
    conn.close()


# Labels

lp_nombre = Label(root, text="Primer nombre: ")
ls_nombre = Label(root, text="Segundo nombre: ")
lapellidos = Label(root, text="Apellidos: ")
ldireccion = Label(root, text="Dirección: ")
lciudad = Label(root, text="Ciudad: ")
lzipcode = Label(root, text="Zip Code: ")

lp_nombre.grid(row=0, column=0, padx=(20, 0), pady=(10, 5), sticky=W)
ls_nombre.grid(row=1, column=0, padx=20, pady=5, sticky=W)
lapellidos.grid(row=2, column=0, padx=20, pady=5, sticky=W)
ldireccion.grid(row=3, column=0, padx=20, pady=5, sticky=W)
lciudad.grid(row=4, column=0, padx=20, pady=5, sticky=W)
lzipcode.grid(row=5, column=0, padx=20, pady=5, sticky=W)

lselect_box = Label(root, text="ID #")
lselect_box.grid(row=9, column=0, padx=20, pady=5, sticky=W)

# Cajas de texto

p_nombre = Entry(root, width=30)
s_nombre = Entry(root, width=30)
apellidos = Entry(root, width=30)
direccion = Entry(root, width=30)
ciudad = Entry(root, width=30)
zipcode = Entry(root, width=30)

select_box = Entry(root, width=30)
select_box.grid(row=9, column=1)

p_nombre.grid(row=0, column=1, pady=(10, 5))
s_nombre.grid(row=1, column=1, pady=5)
apellidos.grid(row=2, column=1, pady=5)
direccion.grid(row=3, column=1, pady=5)
ciudad.grid(row=4, column=1, pady=5)
zipcode.grid(row=5, column=1, pady=5)

# Boton de enviar
btn_submit = Button(root, text="Enviar a la base de datos", command=submit)
btn_submit.grid(row=6, column=0, columnspan=2, pady=10, padx=20, ipadx=100)

# Boton de la consulta
query_btn = Button(root, text="Listar", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=20, ipadx=150)

# Boton de eliminar
delete_btn = Button(root, text="Eliminar", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=20, ipadx=143)

# Boton de Actualizar
update_btn = Button(root, text="Actualizar", command=update)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=20, ipadx=143)

# Cambios del Commit
conn.commit()

# Cerrar conexion
conn.close()
root.mainloop()
