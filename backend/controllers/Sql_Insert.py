import mysql.connector

###--- insert new admin ---###
def insert_admin(self):
        try:
                connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='1234')
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

###--- insert new contacto ---###
def insert_contacto(self):
        try:
                connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='1234')
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


###--- insert new more_data ---###
def insert_more_data(self):
        try:
                connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='1234')
                cursor = connection.cursor()

                mySql_insert_query = """INSERT INTO more_data (Id_more_data, Name, LastName, Calle, Direccion, Piso_Depto, Ciudad, Provincia, Telefono, Id_User) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """

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


###--- insert new user_card ---###
def insert_user_card(self):
        try:
                connection = mysql.connector.connect(host='localhost',
                                                database='new_schema',
                                                user='root',
                                                password='1234')
                cursor = connection.cursor()

                mySql_insert_query = """INSERT INTO user_card ( Mascotas, Presentacion, Imagen,Id_more_Data,Id_user_Card) VALUES (%s,%s,%s,%s,%s) """

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


###--- insert new user ---###
def insert_user(self):
        try:
                connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='1234')
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
