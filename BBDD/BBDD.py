import sqlite3

#Creas la conexion
miConexion=sqlite3.connect("Personajes_Io")

#Para crear una tabla, primero creas un cursor
miCursor=miConexion.cursor()

#Ejecutar query (consulta) SQL
#Creas la tabla, al lado le pones el nombre y entre paréntesis los campos de esta.
#VARCHAR es para poner letras entre paréntesis va el rango de caracteres
#INTEGER es para poner enteros

#Esto lo ejecutas la primera vez, es decir, creas el programa, lo ejecutas, y
# luego invalidas la línea, porque si no estarías creando continuamente bases de
# datos.

#miCursor.execute("""CREATE TABLE PERSONAJES (NOMBRE VARCHAR(50), APELLIDO VARCHAR(50), EDAD INTEGER)""")

#Para insertar datos dentro de la BBDD usas Insert into
#Funny fact, para usar comillas internas, si afuera usas las dobles, adentro
# usas las simples.

#Luego de ejecutar esta orden, la anulas como la anterior
#miCursor.execute("Insert into PERSONAJES values('Yusuke', 'Kurosawa', '21')")

#El .commit() va después de cada instrucción, para confirmar.

#A continuación se muestra como agregar varios contenidos a la base de datos de una
# Para eso se usan listas y tuplas

#Luego de ejecutarlo, lo comentas todo (también se puede eliminar, pero sino
# no se entendería nada de esto :V
#variosPersonajes=[
#    ('Shio', 'Nakamura', '22'),
#    ('Haru', 'Sadao', '22'),
#    ('Adam', 'Walst', '21'),
#    ('Shiru', 'Takahashi', '16')
#    ]

#Para meterlo cambia, si agregas un valor a una lista
#Pones tantos ? como campos haya para llenar
#En el segundo campo poes el nombre de la lista
miCursor.executemany("Insert into PERSONAJES values (?,?,?)", variosPersonajes)

#Después de eso, tenés que confirmar cambios usando la conexion
miConexion.commit()

#Cerras la conexion
miConexion.close()
