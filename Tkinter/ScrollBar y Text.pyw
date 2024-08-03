from tkinter import*

pr=Tk()
pr.title("Scrollbar")

miFrame=Frame(pr, width=900, height=600)
miFrame.pack()

desLabel=Label(miFrame, text="Descripción:")
desLabel.grid(row=3, column =0, sticky="w", padx=5, pady=5)

descripcion = 'Esto es una descripción'

#Espacio para escribir mucho texto.
#El width se usa para darle altura y el height se usa para darle largo.
# El método wrap sirve para que te ponga un enter automático al chocar contra
#   el final del widget, puede ser WORD o CHAR (Que lo separa por caractéres)
tdes=Text(miFrame,width=16, height=5, wrap=WORD)
#Si no se posiciona de esta manera, no te lee el yview
tdes.grid(row=3, column=1, padx=5, pady=5)


#Creas la variable de la Scrollbar
#Comand le indica a la barra a dónde pertenece.
#yview se usa para indicar que funciona de manera vertical
barra=Scrollbar(miFrame, command=tdes.yview)
#El sticky="nsew" sirve para adaptar la scrollbar al tamaño de la ventanita
barra.grid(row=3, column=2, sticky="nsew")

#Esto hace que el scrollbar indique en que parte del texto está
tdes.config(yscrollcommand=barra.set)

#Así es como se inserta texto en un bueno... Texto
# Es importante empaquetarlo con un enter, de lo contrario dará error
tdes.insert(1.0,descripcion)

pr.mainloop()
