#Es un bucle indeterminado, no se sabe cuantas veces se ejecuta el código
#El codigo es while "condicion": y se rompe con "break"

i=0
while i < 4:
    i +=1
    print(f"Ejecución {i}")

print("Ejecución terminada")

#While con condicioneles

edad=int(input("Introduce tu edad: "))
while edad < 18 or edad >100:
    if edad <= 18:
        print("Eres menor de edad, no puedes usar esta app :v jodete")
        break
    elif edad >= 100:
        print("¿Rilly seguis con vida? .-.\nNah jodas, intenta denuevo.")
        edad=int(input("Introduce tu edad: "))
    else:
        print(f"Muy bien, tonces tenes {edad} años, que lendo")
        break

#Funcion continue, se saltea la línea indicada

for letra in "Dan":
    if letra == "a":
        continue
    print(letra)
