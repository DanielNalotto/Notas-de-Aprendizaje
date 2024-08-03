#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo
#y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a
# la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por
# pantalla el grupo que le corresponde.

gen= input("¿Qué género eres, Hombre o Mujer? ")
nom= input("¿Cómo te llamas? ")

if gen.lower() == "hombre":
    if nom.lower() >"n":
        print("Perteneces al grupo A.")
    else:
        print("Estas en el grupo B.")
elif gen.lower() == "mujer":
    if nom.lower() <"m":
        print("Estas en el grupo A.")
    else:
        print("Estas en el grupo B.")
