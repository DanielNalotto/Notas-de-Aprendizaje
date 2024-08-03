import sqlite3

miConexion=sqlite3.connect("PJ.1")

miCursor=miConexion.cursor()

try:
    miCursor.execute("""CREATE TABLE PER (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE VARCHAR (50),
    RAZA VARCHAR (50),
    CLASE VARCHAR (50),
    NIVEL INTEGER)""")
except:
    pass

lista= [
    ('Yusuke', 'Humano', 'Artista Marcial', 8),
    ('Ty', 'Semi-malik', 'Pícaro', 4),
    ('Ikki', 'Semi.elfo', 'Bardo', 6),
    ('Blass', 'Tiflin', 'Guerrero', 3),
    ('B', 'Tiflin', 'Brujo', 1),
    ('Gary', 'Genasi de Aire', 'Explorador', 8)
    ]

miCursor.executemany("INSERT INTO PER VALUES (NULL,?,?,?,?)", lista)

miConexion.commit()

miCursor.execute("select * from PER")
l=miCursor.fetchall()

for i in lista:
    print("Nombre: " + str(i[0]) + ", Raza: " + str(i[1]) + ", Clase: " +
          str(i[2]) + " lv " + str(i[3]) + ".")


miConexion.close()
