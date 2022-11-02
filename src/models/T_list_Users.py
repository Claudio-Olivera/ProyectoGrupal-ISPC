""" import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12') """

#Claudio Olivera: -Esta tabla list_Users sera intermedia entre la tabla Admin y la tabla User.
#Es necesaria? hay que hacer una tabla intermedia para esto? ¿muchos usuarios pueden tener muchos admins y viceversa? (revisar si esta correcto este planteamiento)

    """ mySql_Create_Table_Query = """ """CREATE TABLE list_Users ( 
                            Id_list_Users int(11),
                            Id_list_Admins int(11),
                            CONSTRAINT FK_list_Users_TO_Admin FOREIGN KEY (Id_list_Admins) REFERENCES Admin(Id_Admin),
                            CONSTRAINT FK_list_Users_TO_User FOREIGN KEY (Id_list_Users) REFERENCES User(Id_User))
                            """

  """   cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("tabla de list_Users creada con exito!! ")

except mysql.connector.Error as error:
    print("Fallo al crear tabla list_Users en MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexion con MySQL cerrada.") """