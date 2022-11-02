import mysql.connector

def update_admin_data(username,email,password,Id_admin):
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    #Aca hay que pasarle un parametro a id_admin, para que sepa a que admin modificarle el password.

        mySql_insert_query = " UPDATE admin SET username=%s,email=%s,password=%s WHERE Id_admin=%s"
        record=(username,email,password,Id_admin)
        cursor = connection.cursor()
        cursor.execute(mySql_insert_query, record, id)
        connection.commit()
        print(cursor.rowcount, "registro(s) actualizado") 

    except mysql.connector.Error as error:
        print("Failed to update data into Admin table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

update_admin_data("FernadoL","fernando@hotmail.com","lagartija15",1)