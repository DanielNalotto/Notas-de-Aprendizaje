from tkinter import*
from tkinter import messagebox
import sqlite3


def conectation():
    miConexion=sqlite3.connect("C1")
    miCursor=miConexion.cursor()

    miCursor.execute('''create table DATA (
                     ID integer PRIMARY KEY AUTOINCREMENT,
                     NOMBRE varchar(50),
                     RAZA varchar (50),
                     CLASE varchar (50),
                     NIVEL integer,
                     COMENTARIO varchar(500))''')

    messagebox.showinfo("Mensaje", "La conexión ha sido creada con éxito.")

def des_con():
    miConexion=sqlite3.connect("C1")
    miCursor=miConexion.cursor()
    miConexion.close()
    messagebox.showinfo("Mensaje", "Se ha cerrado la conexión.")

def nuevo():
    miConexion=sqlite3.connect("C1")
    miCursor=miConexion.cursor()

    miCursor.execute("insert into DATA values(NULL, '" + Nom.get() +
                     "','" + Raz.get() +
                     "','" + Cla.get() +
                     "','" + Lvl.get() +
                     "','" + Com.get("1.0", END) +
                     "')")
    miConexion.commit()
    messagebox.showinfo("Mensaje", "Datos ingresados con exito.")
# --------------- LIMPIAR - SET 0 ------------------
def limp():
    Id.set("")
    Nom.set("")
    Raz.set("")
    Cla.set("")
    Lvl.set("")
    Com.delete(1.0, END)
    
# ----------------- BUSCAR -----------------------
def bus():
    Com.delete(1.0, END)

    miConexion=sqlite3.connect("C1")
    miCursor=miConexion.cursor()

    miCursor.execute("Select * from DATA where ID=" + Id.get())
    lista=miCursor.fetchall()

    for l in lista:
        Id.set(l[0])
        Nom.set(l[1])
        Raz.set(l[2])
        Cla.set(l[3])
        Lvl.set(l[4])
        Com.insert(1.0, l[5])
    miConexion.commit()

# ---------------MODIFICAR-------------------------
def mod():
    miConexion=sqlite3.connect("C1")
    miCursor=miConexion.cursor()

    miCursor.execute("UPDATE DATA SET NOMBRE='" + Nom.get() +
                     "',RAZA= '" + Raz.get() +
                     "',CLASE= '" + Cla.get() +
                     "',NIVEL= '" + Lvl.get() +
                     "',COMENTARIO= '" + Com.get("1.0", END) +
                     "' WHERE ID=" + Id.get())
    
    miConexion.commit()

    messagebox.showinfo("Mensaje", "Se ha modificado con éxito.")


# -------------- ELIMINAR ---------------------------

def borrar():
    miConexion=sqlite3.connect("C1")
    miCursor=miConexion.cursor()

    n=messagebox.askyesno("Mensaje", "Si borra el personaje todos los datos se perderan.\n¿Quiere continuar?")
    if n == True:
        miCursor.execute("DELETE FROM DATA WHERE ID=" + Id.get())

        miConexion.commit()
    else:
        pass
# ---------------- INTERFAZ -----------------------------------------------------------------
raiz=Tk()

menubar=Menu(raiz)
raiz.config(menu=menubar)

cas_0=Menu(menubar, tearoff=0)
cas_1=Menu(menubar, tearoff=0)

menubar.add_cascade(label="Conección", menu=cas_0)
menubar.add_cascade(label="Pesonajes", menu=cas_1)

cas_0.add_command(label="Conectar", command=conectation)
cas_0.add_command(label="Desconectar", command=des_con)

cas_1.add_command(label="Crear nuevo", command=nuevo)
cas_1.add_command(label="Eliminar Actual", command=borrar)
cas_1.add_command(label="Modificar Actual", command=mod)
cas_1.add_command(label="Abrir", command=bus)





root=Frame(raiz)
root.pack(side=TOP)

Label(root, text="ID:").grid(row=0, column=0, padx=3, pady=3)
Label(root, text="Nombre:").grid(row=1, column=0, padx=3, pady=3)
Label(root, text="Raza:").grid(row=2, column=0, padx=3, pady=3)
Label(root, text="Clase:").grid(row=3, column=0, padx=3, pady=3)
Label(root, text="Nivel:").grid(row=4, column=0, padx=3, pady=3)
Label(root, text="Comentario:").grid(row=5, column=0, padx=3, pady=3)

Id=StringVar()
Nom=StringVar()
Raz=StringVar()
Cla=StringVar()
Lvl=StringVar()

Entry(root, textvariable=Id).grid(row=0, column=1, padx=3, pady=3)
Entry(root, textvariable=Nom).grid(row=1, column=1, padx=3, pady=3)
Entry(root, textvariable=Raz).grid(row=2, column=1, padx=3, pady=3)
Entry(root, textvariable=Cla).grid(row=3, column=1, padx=3, pady=3)
Entry(root, textvariable=Lvl).grid(row=4, column=1, padx=3, pady=3)

Com=Text(root, width=15, height=5)
Com.grid(row=5, column=1, padx=3, pady=3)

scroll=Scrollbar(root, command=Com.yview)
scroll.grid(row=5, column=2)
Com.config(yscrollcommand=scroll.set)

bot=Frame(raiz)
bot.pack(side=BOTTOM)

Button(bot, text="Limpiar", command=limp).pack(side=RIGHT, padx=5, pady=5)
Button(bot, text="Buscar", command=bus).pack(side=LEFT, padx=5, pady=5)
raiz.mainloop()
