#Suma, Resta, Multiplicación, división
6+5
6-5
6*5
6/5

#División entera
6//5

#Exponente
6**5

#El módulo (%) devuelve el resto de la división
10%3


#Declarar variables
"""Para declarar una variable simplemente escribes el nombre de la variable
igual (=) y luego lo que contiene la variable.
Python automáticamente idetnifíca el tipo de objeto que es."""

variable=5

#type
"""El type sirve para identificar que tipo de variable es y te lo devuelve
como una clase.

type(variable)
class 'int'
"""

print("type(variable)")
print(type(variable))

#Round
#Se usa para redondear hacia y determinar el número de decimales.

res= 8*321.3294
print("8x321.3294 = " + str(res))
print("El anterior fue el resultado, ahora es el resultado redondeado con round")
print(round(res,2))
print("Y ahora con 4 decimales.")
print(round(res,4))
