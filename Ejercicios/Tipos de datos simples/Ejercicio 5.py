
#Escribir un programa que pregunte el nombre del usuario en la consola y después
#de que el usuario lo introduzca muestre por pantalla <NOMBRE> tiene <n> letras,
#donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras
#que tienen el nombre.

name=input("Dime tu nombre y te diré cuántos carácteres tiene. ")
y=len(name)
print("Tu nombre tiene " + str(y) + " carácteres.")

#Más fácil se puede hacer de esta manera:

n=input("Nombre: ")
print("Tu nombre tiene " + str(len(n)) + " carácteres.")

#El resultado es igual pero una manera es más simple que la otra, dependiendo para que
# lo vayas a usar.
