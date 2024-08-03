from tkinter import*

dan=Tk()

nombreFrame=Frame(dan, width=800, height=550)
nombreFrame.pack()

miNombre=StringVar()

Nombre=Entry(nombreFrame, textvariable=miNombre)
Nombre.grid(row=0, column=1)
Nombre.config(fg="blue", justify="left")

nombreLabel=Label(nombreFrame, text="Si sos Maca apreta el botón")
nombreLabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)


#Se define la acción antes de que aparezca el boton
def evento():
    miNombre.set("Te amo")

#Creas la variable del boton
#El parametro command le da una instruccion al boton
boton=Button(dan,text="Botón", command=evento)
boton.pack()

dan.mainloop()
