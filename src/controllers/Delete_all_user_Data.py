import mysql.connector 

def delete_all_user_data(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='new_schema',
                                            user='root',
                                            password='rionegri12')

    #esto esta pensado para borrar todos los datos de un usuario, como las tablas tienen borrado en cascada, al eliminar User, se eliminan tambien more_data y user_card
    
        mySql_insert_query = " DELETE FROM user WHERE Id_User= %s; "
        record = (id)
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print(cursor.rowcount, "registro(s) borrado") 

    except mysql.connector.Error as error:
        print("Failed to delete record into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

delete_all_user_data([3])