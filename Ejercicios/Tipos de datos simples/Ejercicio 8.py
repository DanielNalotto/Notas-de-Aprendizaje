#Escribir un programa que pida al usuario dos números enteros y muestre por
# pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m>
# son los números introducidos por el usuario, y <c> y <r> son el cociente y el
# resto de la división entera respectivamente.


a= int(input("Introduce un número entero: "))
b= int(input("Introduce otro número entero: "))
c = a // b
r = a % b

print(str(a) + " / " + str(b) + " = " + str(c) + ". El resto de la división es " + str(r) + ".")
    
