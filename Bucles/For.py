# el bucle for es determinado (sabes cuando se termina)

# for "variable" in "elemento a recorrer":

pj=["Yusuke", "Shio", "Haru"]

ap=["Kurosawa", "Nakamura", "Sadao"]

for personaje in pj:
    print("Hola " + str(personaje))

#Si queres que no se imprima con salto de línea haces esto, usas el end.
    #Entre las comillas del end le metes como querés que termine la impresion

for apellido in ap:
    print("Sr. " + str(apellido), end=" bienvenido. ")


#Si pones una palabra (String) te recorre por la cantidad de caracteres, mira.

for i in "la_reputa_que_te_pario":
    print("Putos todos")

#Bucle for con condicional if

z=input("Escribi un email cualquiera: ")
email=False

for i in z:
    if (i == "@"):
        email=True
if email== True:
    print("Escribiste un email, felicidades...")
else:
    print("No escribiste un email.. ¿Tas pa la joda bo?")

#for con range

cadena=input("Escribe algo que quieras que se repita 10 veces: ")
for i in range(10):
    print(str(cadena) + " " + str(i))

#Cosas raras que no entiendo pero tan chidas, te agarra la i sin meterle str, si no le metes la f no te hace la cosa chida

for i in range(4):
    print(f"Valor de la variable {i}")


