#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre
#por pantalla.

materias=["Matemáticas", "Historia", "Biología"]
print(materias)

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
#El "for" ... "in" se usa para enumerar en forma de lista.
for materia in materias:
    print("Yo estudio " + materia)
