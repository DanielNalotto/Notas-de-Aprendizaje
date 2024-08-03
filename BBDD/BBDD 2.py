import sqlite3

miConexion=sqlite3.connect("Io_data_base")

miCursor=miConexion.cursor()


#Para buscar información haces lo siguiente:
#Buscas dentro del nobmre de la tabla
miCursor.execute("Select * from PJ")

variosPersonajes=miCursor.fetchall()

print(variosPersonajes)




miConexion.commit()

miConexion.close()
