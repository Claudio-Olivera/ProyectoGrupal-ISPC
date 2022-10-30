import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')


#Claudio Olivera: -Esta tabla user_card es para que el usuario pueda guardar la información de su tarjeta de cuidador. 
# Tiene una relacion 1 a 1 con la tabla more_Data (revisar si lo hice bien).

    mySql_Create_Table_Query = """CREATE TABLE user_card ( 
                            Id_user_card int(11) NOT NULL,
                            Mascotas varchar(50) NOT NULL, 
                            Presentacion varchar(250) NOT NULL,
                            Imagen varchar(100) NOT NULL,
                            Id_more_Data int(11) NOT NULL,
                            CONSTRAINT FK_Card_TO_more_Data FOREIGN KEY (Id_more_Data) REFERENCES more_Data(Id_more_Data),
                            PRIMARY KEY (Id_user_card)) """

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