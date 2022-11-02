import mysql.connector

def create_admin(username, email, password):
    try:
        connection = mysql.connector.connect(host='localhost',
                                        database='new_schema',
                                        user='root',
                                        password='rionegri12')
        cursor = connection.cursor()
# No le paso id , ya que al estar seteado automatico en la tabla no es necesario enviarlo desde aqui.
        mySql_insert_query = """INSERT INTO admin (Username, Email, Password) 
                                VALUES (%s,%s,%s) """

        record = (username, email, password)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into products table")

    except mysql.connector.Error as error:
                print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

#paso parametros a la variable create_admin.
create_admin('Claude', 'claude89@gmail.com', 'rioja12')
create_admin('Marian', 'marian19@gmail.com', 'marialQ12')

