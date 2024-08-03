from io import*

archivo_texto=open("archivo.txt","r")

#READLINES lee el archivo como una lista.
lineas_texto=archivo_texto.readlines()

archivo_texto.close()

#Si quieres ver una lista en especial puedes marcarlo entre
#corchetes, cómo cualquier lista.
print(lineas_texto[1])

