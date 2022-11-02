import mysql.connector

def get_only_user_card(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    #Esta consulta devuelve solo los datos de la tabla user
    # Hay que pasarle el id_user que quiero consultar.

        mySql_query = "select*from user_card WHERE user_card.Id_user_card = %s;"

        record=(id)
        cursor = connection.cursor()
        cursor.execute(mySql_query, record)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to select data related to user_card table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

