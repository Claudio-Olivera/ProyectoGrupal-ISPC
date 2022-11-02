import mysql.connector

def update_admin_data(self):
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    #Aca hay que pasarle un parametro a id_admin, para que sepa a que admin modificarle el password.

        cursor = connection.cursor()
        mySql_insert_query = " UPDATE admin SET username=%s,email=%s,password=%s WHERE Id_Admin=%s"
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