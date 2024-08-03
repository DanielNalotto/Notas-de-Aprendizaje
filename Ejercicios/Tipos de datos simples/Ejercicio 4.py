#Escribir un programa que pregunte el nombre del usuario en la consola y un
#número entero e imprima por pantalla en líneas distintas el nombre del usuario
#tantas veces como el número introducido.

nom=input("¿Cuál es tu nombre? ")
num=int(input("Ingresa un número. "))
i=1
while i<=num:
    print(nom)
    i +=1
