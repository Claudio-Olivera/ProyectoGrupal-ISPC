import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')


#Claudio Olivera: -Esta tabla User contendrá los datos del primer registro del Usuario.
# -El password de la tabla User esta como varchar, pero se puede pasar a binary y guardarla despues de sufrir una encriptacion, como por ejemplo con sha-256.

    mySql_Create_Table_Query = """CREATE TABLE User ( 
                            Id_User int(11) NOT NULL AUTO_INCREMENT,
                            User varchar(20) NOT NULL UNIQUE,
                            Email varchar(100) NOT NULL UNIQUE,
                            Password varchar(30) NOT NULL,
                            PRIMARY KEY (Id_User)) 
                            """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("tabla de usuario creada con exito!! ")

except mysql.connector.Error as error:
    print("Fallo al crear tabla usuario en MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexion con MySQL cerrada.")
