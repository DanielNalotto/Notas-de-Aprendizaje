class Personaje:
    #Aquí definis lo de abajo
    def __init__(self, nom, col, age):
        #Esto es lo de abajo :v
        self.nombre= f"Nombre: {nom}"
        self.color= f"Color de io: {col}"
        self.edad= f"Edad: {age}"

    def print_info(self):
        print(self.nombre)
        print(self.color)
        print(self.edad)
     
yus = Personaje('Yusuke Kurosawa', 'Negro', "20")
shio=Personaje("Shio Nakamura", "Amarillo", "21")
 
yus.print_info()
shio.print_info()
