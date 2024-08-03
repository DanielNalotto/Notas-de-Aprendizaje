class pj:
    def __init__(self):
        self.nombre=''
        self.io=''
        self.habilidad=''
    
    def datos(self):
        print("Nombre: " + self.nombre + "\nIo: " + self.io + "\nHabilidad: " + self.habilidad)

    def escoger_personaje(self):
        print("1_Shio\n2_Yusuke\n3_Haru\n")
        op = input("Opción: ")
        if op == 1:
            print("Hola")
        elif op == 2:
            print("Adios")
        
yusuke=pj()
yusuke.nombre="Yusuke"
yusuke.io="Negro"
yusuke.habilidad="Cortar"

shio=pj()
shio.nombre="Shio"
shio.io="Amarillo"
shio.habilidad="Curar"

haru=pj()
haru.nombre="Haru"
haru.io="Rojo"
haru.habilidad="Rigidez"

escoger_pesronaje()
