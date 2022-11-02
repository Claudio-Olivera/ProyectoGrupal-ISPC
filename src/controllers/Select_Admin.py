import mysql.connector

def get_admin(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')

    #esta consulta devuelve el admin correspondiente a la id que se le pasa por parametro a la funcion.
        mySql_query = "select*from admin where id_Admin=%s"

        record=(id)
        cursor = connection.cursor()
        cursor.execute(mySql_query, record)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to get admin data from admin table. {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")


get_admin([1])