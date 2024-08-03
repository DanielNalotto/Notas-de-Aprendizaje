from tkinter import*

Ventana=Tk()
Ventana.title("Datos")
Ventana.config(bg="sky blue")

miFrame=Frame(Ventana)
miFrame.pack()
miFrame.config(bg="Sky blue")

Nombre=Entry(miFrame)
Nombre.grid(row=0, column=1)
Nombre.config(fg="blue", justify="left")

nombreLabel=Label(miFrame, text="Usuario:")
nombreLabel.grid(row=0, column=0, sticky="w", padx=7, pady=7)
nombreLabel.config(bg="sky blue")

Pass=Entry(miFrame)
Pass.grid(row=1, column=1)
#Show se utiliza para mostrar el caracter que está entre paréntesis en lugar de
#mostrar el que se está ingresando. Puede ser cualquier carácter.
Pass.config(fg="blue", justify="left", show="*")

passLabel=Label(miFrame,text="Contraseña:")
passLabel.grid(row=1, column=0, sticky="w", padx=7, pady=7)
passLabel.config(bg="sky blue")

