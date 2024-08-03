from tkinter import*
from tkinter import messagebox
import sqlite3

def nn1():
    def ace():
            try:
                miConexion=sqlite3.connect(Id.get())
                miCursor=miConexion.cursor()
                if len(Id.get()) > 4:
                    if len(C1.get()) >=4:
                        if C1.get() == C2.get():
                            miCursor.execute('''create table DATOS_USUARIO(
                                 NICK varchar(50) unique primary key,
                                 CONTRASEÑA varchar(50)
                                 )''')
                            miCursor.execute("insert into DATOS_USUARIO values ('" + Id.get() +
                                 "','" + C2.get() + "')")
                            miConexion.commit()
                            miConexion.close()
                            messagebox.showinfo("Mensaje", "Se ha registrado correctamente.")
                        else:
                            messagebox.showerror("Error", "La contraseña y la confirmación de contraseña no coinciden, por favor vuelva a intentarlo.")
                    else:
                        messagebox.showerror("Error","La contraseña debe tener más de 4 caracteres.")
                else:
                    messagebox.showerror("Error","El nombre de usuario debe tener por lo menos 4 caracteres.")
                    print(Id.get())
                    print(len(Id.get()))
            except:
                messagebox.showerror("Error", "Este nombre de usuario ya está en uso, pruebe con otro.")
        
    root=Tk()
    root.title("Registrate")
    root.geometry("280x170")
    root.resizable(False,False)

    f1=Frame(root)
    f1.pack(fill=BOTH, expand=True)

    f1.config(bg="lightskyblue2", width=500, height=300)

    Label(f1, text="REGISTRATE:", bg="lightskyblue2", font=(50)).grid(row=0, columnspan=2, column=0, pady=4, sticky="n")
    Label(f1, text="Usuario:", bg="lightskyblue2").grid(row=1, column=0, sticky="w", pady=4, padx=4)
    Label(f1, text="Contraseña:", bg="lightskyblue2").grid(row=2, column=0, sticky="w", pady=4, padx=4)
    Label(f1, text="Confirmar\ncontraseña:", bg="lightskyblue2").grid(row=3, column=0, sticky="w", padx=4)

    Id=StringVar()
    C1=StringVar()
    C2=StringVar()

    Entry(f1, textvariable=Id, width=25).grid(row=1, column=1, sticky="w", padx=4)
    Entry(f1, textvariable=C1, width=25, show="*").grid(row=2, column=1, sticky="w", padx=4)
    Entry(f1, textvariable=C2, width=25, show="*").grid(row=3, column=1, sticky="w", padx=4)

    Button(f1, text="Aceptar", command=ace).grid(row=4, columnspan=2, column=0, sticky="s", padx=4)

    root.mainloop()


def nn2():
    def Log_In():
        bien=False
        muy=False
    
        miConexion=sqlite3.connect(Id.get())
        miCursor=miConexion.cursor()

        miCursor.execute("Select * from '" + Id.get() + "' where NICK=" + Id.get())
        lista=miCursor.fetchall()

        if lista[0] == Id.get():
            bien=True
        else:
            messagebox.showerror("Error", "El nombre de usuario es incorrecto.")
        if lista[1] == C1.get():
            muy=True       
        else:
            messagebox.showerror("Error", "La contraseña es incorrecta.")
        if muy==True and bien==True:
            messagebox.showinfo("Mensaje","Bienvenido.")
# -------- INTERFAZ --------------------------------------------------------
    root=Tk()

    f1=Frame(root)
    f1.pack(side=LEFT, padx=2)

    f1.config(bg="lightskyblue2", width=500, height=300)

    Label(f1, text="INGRESA:", bg="lightskyblue2", font=(50)).grid(row=0, columnspan=2, column=2, pady=4, sticky="n")
    Label(f1, text="Usuario:", bg="lightskyblue2").grid(row=1, column=2, sticky="w", pady=4)
    Label(f1, text="Contraseña:", bg="lightskyblue2").grid(row=2, column=2, sticky="w", pady=4)

    Id=StringVar()
    C1=StringVar()

    Entry(f1, textvariable=Id, width=20).grid(row=1, column=3, sticky="w")
    Entry(f1, textvariable=C1, width=20).grid(row=2, column=3, sticky="w")

    Button(f1, text="Ingresar", command=Log_In).grid(row=4, columnspan=2, column=2, sticky="s")
    root.mainloop()

# ------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------

root=Tk()
Button(root, text="Registrarse", command=nn1).pack()
Button(root, text="Ingresar", command=nn2).pack()
