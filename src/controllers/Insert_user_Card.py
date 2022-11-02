import mysql.connector

def insert_user_card(self):
        try:
                connection = mysql.connector.connect(host='localhost',
                                                database='new_schema',
                                                user='root',
                                                password='rionegri12')
                cursor = connection.cursor()

                mySql_insert_query = """INSERT INTO user_card ( Mascotas, Presentacion, Imagen,Id_more_Data,Id_user_Card) VALUES (%s,%s,%s,%s,%s) """

#Tener en cuenta que le estoy pasando el Id_more_Data para que haga la relacion entre tablas fijarse como hacer para que ingrese automaticamente el Id_more_Data del user que este logueado.

                record = (self.Mascotas,self.Presentacion, self.Imagen, self.Id_more_Data, self.Id_user_Card)
                cursor.execute(mySql_insert_query, record)
                connection.commit()
                print("Record inserted successfully into user_Card table")

        except mysql.connector.Error as error:
                print("Failed to insert new Card into user_Card table {}".format(error))

        finally:
                if connection.is_connected():
                        cursor.close()
                        connection.close()
                        print("MySQL connection is closed")

#insert_user_card('Perros, Gatos, Hamsters', 'Se administrar medicacion a perros y gatos, hago paseos, tengo experiencia con reptiles ', '/images/laura.jpg',1)