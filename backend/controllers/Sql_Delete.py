import mysql.connector


            #---------------------- BORRADO DE ADMIN POR ID -------------------- #  
def delete_admin(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='1234')

    #esto esta pensado para borrar admin con"id_admin = 2" se aclara que id de admin borrar, o se pone una variable, que viene desde una def de funcion para que borre ese id que se le indique desde el front. 

        mySql_insert_query = " DELETE FROM admin WHERE Id_admin= %s "

        record = (id)
        cursor = connection.cursor()
        cursor.execute((mySql_insert_query),record)
        connection.commit()
        print(cursor.rowcount, "registro(s) borrado") 

    except mysql.connector.Error as error:
        print("Failed to delete admin into Admin table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


            #---------------------- BORRADO DE TODOS LOS DATOS DE USER -------------------- #  
def delete_all_user_data(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='new_schema',
                                            user='root',
                                            password='1234')

    #esto esta pensado para borrar todos los datos de un usuario, como las tablas tienen borrado en cascada, al eliminar User, se eliminan tambien more_data y user_card
    
        mySql_insert_query = " DELETE FROM user WHERE Id_User= %s; "
        record = (id)
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print(cursor.rowcount, "registro(s) borrado") 

    except mysql.connector.Error as error:
        print("Failed to delete user into User table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")




            #---------------------- BORRADO DE MENSAJE DE CONTACTO -------------------- #
def delete_contacto(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='new_schema',
                                            user='root',
                                            password='1234')

    #esto esta pensado para borrar contacto con"id_contacto = 2" se aclara que id de admin borrar, o se pone una variable, que viene desde una def de funcion para que borre ese id que se le indique desde el front. 

        mySql_insert_query = " DELETE FROM contacto WHERE Id_Contacto=%s; "

        record = (id)
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print(cursor.rowcount, "registro(s) borrado") 

    except mysql.connector.Error as error:
        print("Failed to delete data into Contacto table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


            #---------------------- BORRADO SOLO DE USER CARD -------------------- #
def delete_user_card(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='new_schema',
                                            user='root',
                                            password='1234')

    #Con esta consulta borro los datos de user_card si tiene id_user_card, pero esto deberia cambiarse con una variable al numero de id del usuario automaticamente, o al numero de "esa" card que el usuario esta seleccionando. Asimismo el usuario no deberia poder eliminar otros id que no sean el de SU CARD.
        mySql_insert_query = " DELETE FROM user_card WHERE Id_user_Card=%s ;"

        record = (id)
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print(cursor.rowcount, "registro(s) borrado") 

    except mysql.connector.Error as error:
        print("Failed to delete card into user_Card table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

