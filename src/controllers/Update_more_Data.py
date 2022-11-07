import mysql.connector

def update_more_data(self):
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    
        cursor = connection.cursor()
        mySql_insert_query = " UPDATE more_data SET Calle=%s, Direccion=%s, Piso_Depto=%s, Ciudad=%s, Provincia=%s, Telefono=%s WHERE Id_more_data=%s;"
        record=(self.calle,self.direccion,self.piso_Depto,self.ciudad,self.provincia,self.telefono,self.Id_more_data)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print(cursor.rowcount, "registro(s) actualizado") 

    except mysql.connector.Error as error:
        print("Failed to update data into more_Data table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

#update_more_data('Picaflor','1500','5','General Roca','Rio Negro','2984788433',1)