#Escriba un programa que pida el año actual y un año cualquiera y que escriba
#cuántos años han pasado desde ese año o cuántos años faltan para llegar
#a ese año.

a = int(input("Escriba el año actual. "))
b = int(input("Escriba un año cualquiera. "))

if a>b:
    print("Han pasado " + str(a-b) + " desde el año " + str(b) + ".")

elif (a-b)==1 or (b-a)==1:
    print("La diferencia entre ambos años es 1.")

elif a==b:
    print("Es el mismo año.")

else:
    print("Faltan " + str(b-a) + " años para el año " + str(b) + ".")
