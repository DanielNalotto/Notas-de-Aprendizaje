#Escribir un programa que pregunte al usuario su edad y muestre por pantalla
# si es mayor de edad o no.

n = int(input("¿Cuántos años tienes? "))

if n>=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

a= input("Elije una contraseña. ")

b= input("Vuelve a ingresar tu contraseña. ")

if a == b:
    print("La contraseña es correcta.")
else:
    print("La contraseña que has ingresado es inválida.")
    
