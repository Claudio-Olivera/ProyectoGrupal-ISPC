import mysql.connector


###--- select admin por id ---###
def get_admin(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='new_schema',
                                            user='root',
                                            password='1234')

        # esta consulta devuelve el admin correspondiente a la id que se le pasa por parametro a la funcion.
        mySql_query = "select*from admin where id_Admin=%s"

        record = (id)
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


###--- select all contacto ---###
def get_all_contacto():
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='new_schema',
                                            user='root',
                                            password='1234')

        mySql_query = "select*from contacto;"

        cursor = connection.cursor()
        cursor.execute(mySql_query)

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


###--- select all user, user_card , more_data ---###
def get_complete_user_data(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='new_schema',
                                            user='root',
                                            password='1234')

        # Esta consulta devuelve todos los datos de user y con los datos de user_card y more_data,de esta forma obtengo en 1 consulta todos los datos relacionados a user.
        # Hay que pasarle el id_user que quiero consultar.

        mySql_query = "select*from user inner JOIN (more_data, user_Card) on user_card.Id_user_Card = more_data.Id_more_Data WHERE user.id_user = %s;"

        record = (id)
        cursor = connection.cursor()
        cursor.execute(mySql_query, record)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to select all data related to User table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")


###--- select contacto por id ---###
def select_contacto(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='new_schema',
                                            user='root',
                                            password='1234')

        # Hay que pasarle el id_contacto que quiero consultar.

        mySql_query = "select*from contacto WHERE contacto.Id_Contacto = %s;"

        record = (id)
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


###--- select more_data por id ---###
def get_only_more_data(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='new_schema',
                                            user='root',
                                            password='1234')


        mySql_query = "select*from more_data WHERE more_data.Id_more_Data = %s;"

        record = (id)
        cursor = connection.cursor()
        cursor.execute(mySql_query, record)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to select data related to more_data table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")


###--- select user_card por id ---###
def get_only_user_card(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='new_schema',
                                            user='root',
                                            password='1234')

        # Esta consulta devuelve solo los datos de la tabla user_card
        # Hay que pasarle el id_user_card que quiero consultar.

        mySql_query = "select*from user_card WHERE user_card.Id_user_card = %s;"

        record = (id)
        cursor = connection.cursor()
        cursor.execute(mySql_query, record)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to select data related to user_card table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")


###--- select user por id ---###
def get_only_user(id):
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='new_schema',
                                            user='root',
                                            password='1234')

        # Esta consulta devuelve solo los datos de la tabla user
        # Hay que pasarle el id_user que quiero consultar.

        mySql_query = "select*from user WHERE user.id_user = %s;"

        record = (id)
        cursor = connection.cursor()
        cursor.execute(mySql_query, record)

        rows = cursor.fetchall()
        for row in rows:
            print(row)

        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to select all data related to User table {}".format(error))

    finally:
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed")


