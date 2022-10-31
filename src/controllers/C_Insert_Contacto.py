import mysql.connector
#recordar colocar la funcion que pasara los parametros a "record" para que los inserte en la tabla, y luego llamarla pasandole esos datos.
try:
        connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')
        cursor = connection.cursor()
#No le paso id , ya que al estar seteado automatico en la tabla no es necesario enviarlo desde aqui.
        mySql_insert_query = """INSERT INTO contacto (Name, Email, Message) 
                                VALUES (%s,%s,%s) """

        record = ('Patricio','patricio@gmail.com','Como recomendación, me gustaria poder comprar cosas para mis mascotas en la web')
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
