#Una lista es un conjunto ordenado de elementos del mismo o diferente tipo, cuyo contenido puede modificarse.
#Declaras la variables, entre los corchetes van los valores que se almacenan en la listas

personajes=["Yusuke","Haru","Shio","Shina"]

#Imprime la lista completa
print(personajes[:])

#Sorted se usa para ordenarlos elementos de una lista, por defecto es de menor a mayor
numeros= [1, 2000, 4, 50, 600]
print("Ordenados con sorted: " + str(sorted(numeros[:])))

#Con reverse le metes reversa, ah re
a= sorted(numeros, reverse=True)
print(a)

#Y así imprimis el valor más grande
a= sorted(numeros, reverse =True)
print(f"Con sorted: {a[0]}")

#Asosiando valores a objetos de la lista:
#Entre parentessis de la definición y parentesis recto al final va el nombre
#de la lista. (La lista tiene que estar hecha como lista, como está más arriba)

yus=5
shina=3
haru=3
shio=4

def nombre_def(personajes):
    return {
        "Yusuke": yus,
        "Haru": haru,
        "Shio": shio,
        "Shina": shina
        } [personajes]

print(sorted(personajes))


#Máximo de la lista
print(max(personajes))
