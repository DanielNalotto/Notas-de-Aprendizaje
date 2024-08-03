from tkinter import*
from tkinter import messagebox
import sqlite3

def Log_In():

    miConexion=sqlite3.connect(Name.get())
    miCursor=miConexion.cursor()
    
    try:
        miCursor.execute("Select * from '" + Name.get() + "' where ID=" + Id.get())
        lista=miCursor.fetchall()

        for l in lista:
            pass
        if Id.get() == l[0]:
            messagebox.showinfo("Mensaje", "Ha ingresado con éxito.")
        else:
            messagebox.showerror("Error", "Contraseña incorrecta.")
    except:
        messagebox.showerror("Error","Nombre de usuario equivocado.")

    miConexion.commit()

# -------- INTERFAZ --------------------------------------------------------
root=Tk()

f1=Frame(root)
f1.pack(side=LEFT, padx=2)

f1.config(bg="lightskyblue2", width=500, height=300)

Label(f1, text="INGRESA:", bg="lightskyblue2", font=(50)).grid(row=0, columnspan=2, column=2, pady=4, sticky="n")
Label(f1, text="Nombre:", bg="lightskyblue2").grid(row=1, column=2, sticky="w", pady=4)
Label(f1, text="Usuario:", bg="lightskyblue2").grid(row=2, column=2, sticky="w", pady=4)
Label(f1, text="Contraseña:", bg="lightskyblue2").grid(row=3, column=2, sticky="w", pady=4)

Name=StringVar()
Id=StringVar()
C1=StringVar()

Entry(f1, textvariable=Name, width=20).grid(row=1, column=3, sticky="w")
Entry(f1, textvariable=Id, width=20).grid(row=2, column=3, sticky="w")
Entry(f1, textvariable=C1, width=20).grid(row=3, column=3, sticky="w")

Button(f1, text="Ingresar", command=Log_In).grid(row=4, columnspan=2, column=2, sticky="s")


root.mainloop()
