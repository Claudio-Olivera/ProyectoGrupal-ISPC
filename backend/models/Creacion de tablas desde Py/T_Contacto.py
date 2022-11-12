import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')


#Claudio Olivera: - Esta tabla Contacto se genera sin ser conectada a otras tablas, no se necesitan autenticaciones de usuario ya que esta echa para que cualquiera que acceda a la web, pueda enviar un mensaje. 

    mySql_Create_Table_Query = """CREATE TABLE Contacto ( 
                            Id_Contacto int(11) NOT NULL,
                            Name varchar(100) NOT NULL,
                            Email varchar(100) NOT NULL,
                            Message varchar(250) NOT NULL,
                            PRIMARY KEY (Id_Contacto)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("tabla de Contacto creada con exito!! ")

except mysql.connector.Error as error:
    print("Fallo al crear tabla Contacto en MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conexion con MySQL cerrada.")