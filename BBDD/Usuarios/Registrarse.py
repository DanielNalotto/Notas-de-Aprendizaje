from tkinter import*
from tkinter import messagebox
import sqlite3

def ace():
    try:
        miConexion=sqlite3.connect(Id.get())
        miCursor=miConexion.cursor()
        if len(Id.get()) >= 2:
            if len(C1.get()) >=1:
                if C1.get() == C2.get():
                    miCursor.execute("create table '" + Name.get() + "'(ID varchar(50) unique primary key, CONTRASEÑA varchar(50))")
                    miCursor.execute("insert into '" + Name.get() + "' values ('" + Id.get() +
                         "','" + C2.get() + "')")
                    miConexion.commit()
                   # miConexion.close()
                    messagebox.showinfo("Mensaje", "Se ha registrado correctamente.")
                else:
                    messagebox.showerror("Error", "La contraseña y la confirmación de contraseña no coinciden, por favor vuelva a intentarlo.")
            else:
                messagebox.showerror("Error","La contraseña debe tener más de 4 caracteres.")
        else:
            messagebox.showerror("Error","El nombre de usuario debe tener por lo menos 4 caracteres.")
    except:
        messagebox.showerror("Error", "Este nombre de usuario ya está en uso, pruebe con otro.")
        


        

# ------ INTERFAZ --------------------------------------------------------
root=Tk()
root.title("Registrate")
root.geometry("280x170")
root.resizable(False,False)

f1=Frame(root)
f1.pack(fill=BOTH, expand=True)

f1.config(bg="lightskyblue2", width=500, height=300)

Label(f1, text="REGISTRATE:", bg="lightskyblue2", font=(50)).grid(row=0, columnspan=2, column=0, pady=4, sticky="n")
Label(f1, text="Nombre:", bg="lightskyblue2").grid(row=1, column=0, sticky="w", pady=4, padx=4)
Label(f1, text="Usuario:", bg="lightskyblue2").grid(row=2, column=0, sticky="w", pady=4, padx=4)
Label(f1, text="Contraseña:", bg="lightskyblue2").grid(row=3, column=0, sticky="w", padx=4)
Label(f1, text="Confirmar\ncontraseña:", bg="lightskyblue2").grid(row=4, column=0, sticky="w", padx=4)

Name=StringVar()
Id=StringVar()
C1=StringVar()
C2=StringVar()

Entry(f1, textvariable=Name, width=25).grid(row=1, column=1, sticky="w", padx=4)
Entry(f1, textvariable=Id, width=25).grid(row=2, column=1, sticky="w", padx=4)
Entry(f1, textvariable=C1, width=25, show="*").grid(row=3, column=1, sticky="w", padx=4)
Entry(f1, textvariable=C2, width=25, show="*").grid(row=4, column=1, sticky="w", padx=4)

Button(f1, text="Aceptar", command=ace).grid(row=5, columnspan=2, column=0, sticky="s", padx=4)

root.mainloop()
