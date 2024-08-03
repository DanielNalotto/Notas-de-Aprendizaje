from io import*

archivo_texto=open("archivo.txt","r")

#Estas diciendo que lea el archivo y lo almacene en la variable.
texto=archivo_texto.read()

#También existe el método "readlines()" lee la información que está
# almacenada en el archivo línea a línea.

archivo_texto.close()

print(texto)

