import mysql.connector

def get_complete_user_data(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    #Esta consulta devuelve todos los datos de user y con los datos de user_card y more_data,de esta forma obtengo en 1 consulta todos los datos relacionados a user.
    # Hay que pasarle el id_user que quiero consultar.

        mySql_query = "select*from user inner JOIN (more_data, user_Card) on user_card.Id_user_Card = more_data.Id_more_Data WHERE user.id_user = %s;"

        record=(id)
        cursor = connection.cursor()
        cursor.execute(mySql_query, record)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to select all data related to User table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

get_complete_user_data([1])