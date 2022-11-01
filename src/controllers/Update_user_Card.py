import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    #Aca hay que pasarle un parametro a Id_user_Card, para saber a quien modificar y hay que ver como pasarle todos los datos o solo uno..
    mySql_insert_query = " UPDATE user_card SET Mascotas='Aves, Reptiles', Presentacion='Soy Larissa, me encantan las mascotas, me considero muy capaz para el cuidado de reptiles en particular.', Imagen='/images/nuevaImgReptil.jpg' WHERE Id_user_Card;"

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