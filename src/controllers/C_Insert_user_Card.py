import mysql.connector
#recordar colocar la funcion que pasara los parametros a "record" para que los inserte en la tabla, y luego llamarla pasandole esos datos.
try:
        connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')
        cursor = connection.cursor()
#No le paso id , ya que al estar seteado automatico en la tabla no es necesario enviarlo desde aqui.
        mySql_insert_query = """INSERT INTO user_card ( Mascotas, Presentacion, Imagen,Id_more_Data) 
                                VALUES (%s,%s,%s,%s) """
#Tener en cuenta que le estoy pasando el Id_more_Data para que haga la relacion entre tablas fijarse como hacer para que ingrese automaticamente el Id_more_Data del user que este logueado.
        record = ('Perros, Gatos, Hamsters', 'Me encantan los animales, paseo perros, doy medicamentos ', '/images/laura.jpg',1)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into products table")

except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

