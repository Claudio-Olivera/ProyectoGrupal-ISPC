import mysql.connector

def get_all_contacto():
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    #Esta consulta devuelve todos los datos de user y con los datos de user_card y more_data,de esta forma obtengo en 1 consulta todos los datos relacionados a user.
    # Hay que pasarle el id_user que quiero consultar.

        mySql_query = "select*from contacto;"

        cursor = connection.cursor()
        cursor.execute(mySql_query)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to select all data related to contacto table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

