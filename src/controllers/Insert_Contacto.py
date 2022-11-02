import mysql.connector

def insert_contacto(self):
        try:
                connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')
                cursor = connection.cursor()
#No le paso id , ya que al estar seteado automatico en la tabla no es necesario enviarlo desde aqui.
                mySql_insert_query = """INSERT INTO contacto (Name, Email, Message, Id_Contacto) 
                                VALUES (%s,%s,%s,%s) """
        
                record = (self.name, self.email, self.message, self.Id_Contacto)
                cursor.execute(mySql_insert_query, record)
                connection.commit()
                print("Record inserted successfully into Contacto table")

        except mysql.connector.Error as error:
                print("Failed to insert new data into Contacto table {}".format(error))

        finally:
                if connection.is_connected():
                        cursor.close()
                        connection.close()
                        print("MySQL connection is closed")

#insert_contacto('Patricio','patricio@gmail.com','Como recomendación, me gustaria poder comprar cosas para mis mascotas en la web')