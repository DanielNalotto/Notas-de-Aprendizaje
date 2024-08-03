#Open es el metodo que se usa para abrir un archivo externo,
# se está especificando que solo se va a importar ese, no todos los archivos
# de a librería io.

from io import*

#Dentro de los parentesis pide(el nombre del archivo a abrir, el modo en el que
#lo vas a abrir)

#Un archivo se puede abrir en los siguientes modos:
#Lectura: Solo puedes leer la informacion
#Escritura: Crea un archivo de texto en el cual puedes escribir contenido. (w)
#Append: Para agregar información a un archivo que ya estaba escrito.

archivo_texto=open("archivo.txt","w")

#\n es un salto de línea, un enter.
frase="Hola mundo, ¿to piola? \nNightwing es el mejor."

#Esto es para guardar la frase en el archivo
archivo_texto.write(frase)

#Esto sirve para cerrar el archivo
archivo_texto.close()
