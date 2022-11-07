import mysql.connector

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