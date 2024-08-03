import numpy as np

#Crear array normal
num_primos1 = [2,3,5,7,11,13,17,19,23,29]
print(num_primos1)

#Crear array con NumPy
num_primos2 = np.array(num_primos1)
print(num_primos2)

#Crear un array de ceros
zero_array = np.zeros(10)
print(zero_array)

#Crear un array con numeros
num_array = np.arange(10)
print(num_array)

#Crear un array con un rango e iteración predefinido
ite_array = np.arange(0,20,2) #Inicio, Final, Iteracion
print(ite_array)

#Reestructurar un arreglo para que sea bidimensional
print(ite_array.reshape(2,5))
