#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no

a= int(input("¿Cuál es tu edad? "))
b= int(input("¿Cuáles son tus ingresos mensuales en euros? "))

if a>=18 and b >=1000:
    print("Felicidades, puedes tributar.")
else:
    print("No puedes tributar")
