#Así creas la clase, re facil.
#Todas las clases "coche" que crees van a tener estas propiedades.
class Coche():
    # --- Ahora creas las propiedades de la clase
    largoChasis=250
    anchoChasis=120
    rueda=4
    enmarcha=False

    #Así creas un método, el metodo es lo que puede hacer la clase, el comportamiento que tiene
    def arrancar(self):
        self.enmarcha=True

    def estado(self):
        if(self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"

#Así haces una instanciación de clase
miCoche=Coche()
print("El largo del coche es " + str(miCoche.largoChasis))
miCoche.arrancar()

print(miCoche.estado())
