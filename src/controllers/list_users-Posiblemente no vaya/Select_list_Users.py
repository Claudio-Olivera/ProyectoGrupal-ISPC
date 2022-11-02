import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    #esta consulta devuelve la tabla list_users con todos los datos relacionados entre admin y user
    
    mySql_query = "select*from list_users inner join (admin, user) on list_users.Id_list_Users=list_users.Id_list_Admins;"


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

