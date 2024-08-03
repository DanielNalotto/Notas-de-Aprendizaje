from tkinter import*

ventana=Tk()

ventana.title("Datos")

nombreFrame=Frame(ventana, width=800, height=550)
nombreFrame.pack()

Nombre=Entry(nombreFrame)
#Ubica la variable utilizando el metodo grid (grilla)
Nombre.grid(row=0, column=1)
#fg es para darle color a la letra, justify es para alinear el texto.
Nombre.config(fg="blue", justify="left")

nombreLabel=Label(nombreFrame, text="Nombre:")
#padx y pady sirven para darle un espacio entre los labels
nombreLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)

Clase=Entry(nombreFrame)
Clase.grid(row=1, column=1)
Clase.config(fg="blue", justify="left")

claseLabel=Label(nombreFrame, text="Clase:")
#Sticky se utiliza para alinear el texto, utiliza los puntos cardinales en ingles
#Sólo las iniciales alcanzan (n,s,w,e)
claseLabel.grid(row=1, column=0, sticky="w", padx=5, pady=5)

Raza=Entry(nombreFrame)
Raza.grid(row=2, column=1)
Raza.config(fg="blue", justify="left")

razaLabel=Label(nombreFrame, text="Raza:")
razaLabel.grid(row=2, column=0, sticky="w", padx=5, pady=5)




ventana.mainloop()
