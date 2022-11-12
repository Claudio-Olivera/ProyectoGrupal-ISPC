import mysql.connector

def insert_admin(self):
        try:
                connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')
                cursor = connection.cursor()
# No le paso id , ya que al estar seteado automatico en la tabla no es necesario enviarlo desde aqui.
                mySql_insert_query = """INSERT INTO admin (id_admin, Username, Email, Password) 
                                VALUES (%s,%s,%s,%s) """

                record = (self.Id_Admin, self.username, self.email, self.password)
                cursor.execute(mySql_insert_query, record)
                connection.commit()
                print("Record inserted successfully into Admin table")

        except mysql.connector.Error as error:
                        print("Failed to insert new admin into Admin table {}".format(error))

        finally:
                if connection.is_connected():
                        cursor.close()
                        connection.close()
                        print("MySQL connection is closed")

#paso parametros a la variable create_admin.
#insert_admin('Claude', 'claude89@gmail.com', 'rioja12')
#insert_admin('Marian', 'marian19@gmail.com', 'marialQ12')



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


def insert_user(self):
        try:
                connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')
                cursor = connection.cursor()

                mySql_insert_query = """INSERT INTO user (Id_User, User, Email, Password) 
                                VALUES (%s,%s,%s,%s) """
                
                record = (self.Id_User, self.user, self.email, self.password)
                cursor.execute(mySql_insert_query, record)
                connection.commit()
                print("Record inserted successfully into User table")

        except mysql.connector.Error as error:
                print("Failed to insert new User into User table {}".format(error))

        finally:
                if connection.is_connected():
                        cursor.close()
                        connection.close()
                        print("MySQL connection is closed")

#insert_user('LarissaCaptain', 'Timonesrobados@gmail.com', 'timonesl23')