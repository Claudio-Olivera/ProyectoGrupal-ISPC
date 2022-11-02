import mysql.connector

def update_user_card(mascotas,presentacion,Imagen,id_user_Card):
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    #Aca hay que pasarle un parametro a Id_user_Card, para saber a quien modificar y hay que ver como pasarle todos los datos o solo uno..
        mySql_insert_query = " UPDATE user_card SET Mascotas=%s, Presentacion=%s, Imagen=%s WHERE Id_user_Card=%s;"
        record=(mascotas,presentacion,Imagen,id_user_Card)
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print(cursor.rowcount, "registro(s) actualizado") 

    except mysql.connector.Error as error:
        print("Failed to update data into user_Card table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            
update_user_card('Aves, Perros','Soy Larisa, me encantan las mascotas, me considero muy capaz para el cuidado de reptiles en particular.','/images/nuevaImgReptil.jpg',1)