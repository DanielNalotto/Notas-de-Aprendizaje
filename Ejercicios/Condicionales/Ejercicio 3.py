#Escribir un programa que pida al usuario dos números y muestre por pantalla
# su división. Si el divisor es cero el programa debe mostrar un error.

print("Vamos a realizar una división, escribe los números utilizando el teclado.")
a= int(input("Introduce el dividendo: "))
b= int(input("Introduce el divisor: "))

if b==0:
    print("Error, el divisor no puede ser cero.")
else:
    r = b / a
    print("El resultado de la división es " + str(r) + ".")
    
    
