#En este insert estoy colocando el id del admin y el id del user, pero tengo que revisar como hacer que esto se genere automaticamente al crear un usuario nuevo..

import mysql.connector
#recordar colocar la funcion que pasara los parametros a "record" para que los inserte en la tabla, y luego llamarla pasandole esos datos.
try:
        connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')
        cursor = connection.cursor()
#No le paso id , ya que al estar seteado automatico en la tabla no es necesario enviarlo desde aqui.
        mySql_insert_query = """INSERT INTO list_users (Id_list_Users, Id_list_Admins) 
                                VALUES (%s,%s) """

        record = (3,2)
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