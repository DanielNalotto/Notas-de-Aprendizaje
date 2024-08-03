class Perro():
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.trucos = []    # crea una nueva lista vacía para cada perro

    def agregar_truco(self, truco):
        self.trucos.append(truco)

d = Perro('Fido')
e = Perro('Buddy')
d.agregar_truco(input("¿Qué habilidad quieres aprender?"))
e.agregar_truco('hacerse el muerto')
d.trucos
e.trucos

print(d.trucos)
