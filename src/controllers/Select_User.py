import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    #esta consulta devuelve todos los datos de user y le suma los datos de user_card y more_data, esta forma obtengo en 1 consulta todos los datos relacionados a user.

    mySql_query = "select*from user inner JOIN (more_data, user_Card) on user_card.Id_user_Card = more_data.Id_more_Data;"


    cursor = connection.cursor()
    cursor.execute(mySql_query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")