import mysql.connector

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