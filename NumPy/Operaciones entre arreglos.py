import numpy as np

#Crear array de numeros pares
pares=[0,2,4,6,8,10,12,14,16,18]

#Pasar el array pares con np
array_pares= np.array(pares)
print(array_pares)

#Array de impares
array_impares = array_pares+1
print(array_impares)

#Multiplicar el array por 100
array_porCien = array_impares*100
print(array_porCien)

#Resta entre arrays
print(array_impares - array_pares)

#Dividir arrays
print(array_pares/array_impares)

#Sumar todos los numeros de una lista
print(array_impares.sum())

#Promedio de los numeros de una lista
print(array_pares.mean())

#Varianza de los numeros en una lista
"""
La Varianza es una medida de dispersión que se utiliza para representar la variabilidad de un conjunto
de datos respecto de la media aritmética de los mismo. Así, se calcula como la suma de los residuos
elevados al cuadrado y divididos entre el total de observaciones.
"""
print(array_pares.var())

#Ordenar np array
array_fibonacci=np.array([2, 34,1, 21, 0, 5, 13, 8, 3, 55, 1])
print(array_fibonacci)

#De menor a mayor
print(np.sort(array_fibonacci))

#De mayor a menor
"""
Se le pone el negativo a array_fibonnacci para que los ordene 'positivamente', siendo numeros negativos.
Luego se le pone el negativo a np.sort, para que quite el signo de negativo
"""
print(np.sort(-array_fibonacci))
print(-np.sort(-array_fibonacci))
