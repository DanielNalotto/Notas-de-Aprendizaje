#Usas el método open, enre paréntesis pones primero
#Primero va la dirección y el nombre del archivo y segundo
#El modo, por defecto es Read si no aclaras.

f=open("YS.txt", "r")
print(f.read())

#Existen diferentes modos:

#"r" Read, Abris un archivo para leero y da error si no existe.

#"a" Append, Abris un archivo para agregar contenido, lo crea si no existe.

#"w" Write, Abris un archivo para escribirlo, lo creas si no existe.

#"x" Create, Creas un archivo, te da error si ya existe.


#Si lo almacenas en la variable y la imprimis te salta el texto en IDE 
