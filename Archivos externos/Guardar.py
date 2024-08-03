import pickle

class Persona:

    def_init_(self, nombre, genero, edad):
        self.nombre=nombre
        self.genero=genero
        self.edad=edad
        print ("Se ha creado una persona nueva con el nombre de ", + self.nombre)

    def_str_(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)

p=Persona("Yusuke", "Masculina", "20")
