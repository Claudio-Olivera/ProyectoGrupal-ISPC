import mysql.connector 

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    #esto esta pensado para borrar admin con"id_admin = 2" se aclara que id de admin borrar, o se pone una variable, que viene desde una def de funcion para que borre ese id que se le indique desde el front. 

    mySql_insert_query = " DELETE FROM admin WHERE Id_admin; "

    
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "registro(s) borrado") 

except mysql.connector.Error as error:
    print("Failed to delete record into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")