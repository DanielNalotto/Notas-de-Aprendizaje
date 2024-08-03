#Escribir un programa que realice la siguiente operación aritmética ((3+2)//(2*5))**2.

resultado = ((3+2)/(2*5))**2
print("((3+2)/(2*5))**2 = " + str(resultado))

#Ejercicio 7

#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
# calcule el índice de masa corporal y lo almacene en una variable, y muestre por
# pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de
# masa corporal calculado redondeado con dos decimales.

peso= input("Introduzca su peso: ")
altura= input("Introduzca su altura: ")

imc = int(altura) / int(peso)

print("Su índice de masa corporal es " + str(round(imc,2)))
