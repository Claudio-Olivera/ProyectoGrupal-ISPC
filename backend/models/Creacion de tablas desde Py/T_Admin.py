import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='1234')

#Claudio Olivera: -Esta tabla Admin contendrá los datos del administrador del sistema.
# -El password de la tabla Admin esta como varchar, pero se puede pasar a binary y guardarla despues de sufrir una encriptacion, como por ejemplo con sha-256.

    mySql_Create_Table_Query = """CREATE TABLE Admin ( 
                            Id_Admin int(11) NOT NULL UNIQUE,
                            Username varchar(20) NOT NULL UNIQUE,
                            Email varchar(100) NOT NULL UNIQUE,
                            Password varchar(30) NOT NULL,
                            PRIMARY KEY (Id_Admin)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("tabla de admin creada con exito!! ")

except mysql.connector.Error as error:
    print("Fallo al crear tabla admin en MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexion con MySQL cerrada.")