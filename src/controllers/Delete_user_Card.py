import mysql.connector

def delete_user_card(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='new_schema',
                                            user='root',
                                            password='rionegri12')

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

delete_user_card([3])