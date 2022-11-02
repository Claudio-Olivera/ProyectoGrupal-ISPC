import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    #esta consulta devuelve todos los usuarios registrados como admin
    mySql_query = "select*from admin"


    cursor = connection.cursor()
    cursor.execute(mySql_query)

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()

except mysql.connector.Error as error:
    print("Failed to select from admin table. {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")