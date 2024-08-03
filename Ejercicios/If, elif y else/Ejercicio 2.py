#Escriba un programa que pida dos números y que conteste cuál es el menor
# y cuál el mayor o que escriba que son iguales.

a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))

if a<b:
    print(str(a) + " es mayor que " + str(b) + ".")
elif a==b:
    print(str(a) + " es igual a " + str(b))
else:
    print(str(b) + " es menor que " + str(a))
