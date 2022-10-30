import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')


#Claudio Olivera: -El password de la tabla user esta como varchar, pero se puede pasar a binary y guardarla despues de sufrir una encriptacion, como por ejemplo con sha-256

    mySql_Create_Table_Query = """CREATE TABLE more_Data ( 
                            Id_more_Data int(11) NOT NULL,
                            Name varchar(20) NOT NULL,
                            LastName varchar(50) NOT NULL,
                            Calle varchar(30) NOT NULL,
                            Direccion varchar(30) NOT NULL,
                            Piso_Depto varchar(30),
                            Ciudad varchar(30) NOT NULL,
                            Provincia varchar(30) NOT NULL,
                            Telefono varchar(20) NOT NULL,
                            Id_user int(11) NOT NULL,
                            CONSTRAINT FK_moreData_TO_User FOREIGN KEY (Id_user) REFERENCES User(Id_User) 
                            ON UPDATE RESTRICT ON DELETE CASCADE,
                            PRIMARY KEY (Id_more_Data)) """

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