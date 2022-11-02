import mysql.connector

def select_contacto(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    #Esta consulta devuelve solo los datos de la tabla user
    # Hay que pasarle el id_user que quiero consultar.

        mySql_query = "select*from contacto WHERE contacto.Id_Contacto = %s;"

        record=(id)
        cursor = connection.cursor()
        cursor.execute(mySql_query, record)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to select all data related to contacto table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

