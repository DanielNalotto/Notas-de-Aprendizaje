from io import*

gx=open("archivo.txt","r")


#Sirve para posisionar el cursor antes de imprimir. Lee a partir de donde está
# posisionado en adelante.
gx.seek(4)

#El metodo read también posisiona el cursor, pero lee hasta donde esta posisionado.
print(gx.read(20))

gx.close()
