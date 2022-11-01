import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    #Aca hay que pasarle un parametro a Id_more_Data, para saber a quien modificar y hay que ver como pasarle todos los datos o solo uno..
    mySql_insert_query = " UPDATE more_data SET Calle='Picaflor', Direccion='500', Piso_Depto='5', Ciudad='Mendoza', Provincia='Mendoza', Telefono='2984788433' WHERE Id_more_Data;"

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "registro(s) actualizado") 

except mysql.connector.Error as error:
    print("Failed to delete record into MySQL table {}".format(error))

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")