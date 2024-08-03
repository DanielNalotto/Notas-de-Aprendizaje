import numpy as np

#Crear lista de pares
pares = np.arange(0,20,2).reshape(2,5)
print(pares)

#Seleccionar primer item de la lista de pares
print(pares[0][0])

#Seleccinar algun otro elemento
print(pares[1][3])

#Seleccionar varios elementos
print(pares[1,:])

#Seleccionar por fila
print(pares[:,3])

#Utilizar filtros
array_fibonacci=np.array([2, 34,1, 21, 0, 5, 13, 8, 3, 55, 1])
print(array_fibonacci)

#Pedir los numeros menores a 20
"Al pedir <20, estas dandole una condición lógica a la lista, lo cual devuelve verdadero o falso"
print(array_fibonacci<20)
"Al ponerlo entre corchetes, seguido del nombre del array, imprime los datos"
print(array_fibonacci[array_fibonacci<20])