import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')


#Claudio Olivera: -El password de la tabla user esta como varchar, pero se puede pasar a binary y guardarla despues de sufrir una encriptacion, como por ejemplo con sha-256

    mySql_Create_Table_Query = """CREATE TABLE User_card ( 
                            Id_User_card int(11) NOT NULL,
                            Mascotas varchar(50) NOT NULL, 
                            Presentacion varchar(250) NOT NULL,
                            Imagen varchar(100) NOT NULL,
                            Id_more_Data int(11) NOT NULL,
                            CONSTRAINT FK_Card_TO_more_Data FOREIGN KEY (Id_more_Data) REFERENCES more_Data(Id_more_Data),
                            PRIMARY KEY (Id_User_card)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("tabla de more_Data creada con exito!! ")

except mysql.connector.Error as error:
    print("Fallo al crear tabla en MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexion con MySQL cerrada.")