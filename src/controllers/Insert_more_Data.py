import mysql.connector

def insert_more_data(self):
        try:
                connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')
                cursor = connection.cursor()

                mySql_insert_query = """INSERT INTO more_data (Id_more_data, Name, LastName, Calle, Direccion, Piso_Depto, Ciudad, Provincia, Telefono, Id_User) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """
#Tener en cuenta que le estoy pasando el Id_User para que haga la relacion entre tablas fijarse como hacer para que ingrese automaticamente el Id_User del user que este logueado.
                record = (self.Id_more_data, self.name, self.lastName, self.calle, self.direccion, self.piso_Depto, self.ciudad, self.provincia, self.telefono, self.Id_User)
                cursor.execute(mySql_insert_query, record)
                connection.commit()
                print("Record inserted successfully into more_Data table")

        except mysql.connector.Error as error:
                print("Failed to insert data into more_Data table {}".format(error))

        finally:
                if connection.is_connected():
                        cursor.close()
                        connection.close()
                        print("MySQL connection is closed")


#insert_more_data('Laura','Robledo','Alsina','413','','General Roca','Rio Negro','2984788455',1)

