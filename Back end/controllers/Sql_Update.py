import mysql.connector

def update_admin_data(self):
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    #Aca hay que pasarle un parametro a id_admin, para que sepa a que admin modificarle el password.

        cursor = connection.cursor()
        mySql_insert_query = " UPDATE admin SET username=%s,email=%s,password=%s WHERE id_admin=%s"
        record=(self.username,self.email,self.password,self.Id_Admin)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print(cursor.rowcount, "registro(s) actualizado") 

    except mysql.connector.Error as error:
        print("Failed to update data into Admin table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

#update_admin_data("FernadoL","fernando@hotmail.com","lagartija15",3)



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



def update_user_card(self):
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    #Aca hay que pasarle un parametro a Id_user_Card, para saber a quien modificar y hay que ver como pasarle todos los datos o solo uno..
        cursor = connection.cursor()
        mySql_insert_query = " UPDATE user_card SET Mascotas=%s, Presentacion=%s, Imagen=%s WHERE Id_user_Card=%s;"
        record=(self.Mascotas,self.Presentacion,self.Imagen,self.Id_user_Card)
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
            
#update_user_card('Aves, Perros','Soy Larisa, me encantan las mascotas, me considero muy capaz para el cuidado de reptiles en particular.','/images/nuevaImgReptil.jpg',1)



def update_user(self):
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    #Aca hay que pasarle un parametro a Id_User, para que sepa a que admin modificarle el password.
        cursor = connection.cursor()
        mySql_insert_query = " UPDATE user SET User=%s, Email=%s, Password=%s WHERE Id_user=%s;"

        record= (self.user, self.email,self.password, self.Id_User)
        cursor.execute(mySql_insert_query,record)
        connection.commit()
        print(cursor.rowcount, "registro(s) actualizado") 

    except mysql.connector.Error as error:
        print("Failed to update data into User table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            
#update_user('Larissa99', 'nuevoMailLarissa@gmail.com', 'nuevaPassLarissa88', 1)