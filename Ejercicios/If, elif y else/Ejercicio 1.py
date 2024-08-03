#Escriba un programa que pida dos números enteros y que calcule su división,
# escribiendo si la división es exacta o no.

print("A continuación se le pedira que ingrese dos números enteros para realizar una división.")
a = int(input("Ingrese el dividendo: "))
b = int(input("Ingrese el divisor: "))

if b > 0:
    if a%b == 0:
        print("El cociente de su división es " + str(a/b) + ".")
    else:
        print("El cociente de su división es " + str(round(a/b,2)) + " y el resto es " + str(a%b) + ".")
else:
    print("El divisor no puede ser 0.")
