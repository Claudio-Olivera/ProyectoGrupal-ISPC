from controller.Sql_Delete import delete_all_user_data
from controller.Sql_Insert import insert_user
from controller.Sql_Select import get_complete_user_data, get_only_user
from controller.Sql_Update import update_user


class User:
    def __init__(self, Id_User, user, email, password):
        self.Id_User = Id_User
        self.user = user
        self.email = email
        self.password = password

    # crea un nuevo user
    def crear_User(self):
        insert_user(self)

    # muestra solo los datos de la tabla user
    def obtener_user(self):
        get_only_user([self.Id_User])

    # Obtiene todos los datos relacionados a el user, para usar este metodo, debe primero tener registros en user_card y more_data
    def all_user_data(self):
        get_complete_user_data([self.Id_User])

    # este metodo borra en cascada el usuario, su card y su more_data
    def borrar_User(self):
        delete_all_user_data([self.Id_User])

    # actualiza la tabla user
    def actualizar_User(self):
        update_user(self)

# -----------------INVOCACION DE METODOS Y CREACION DE OBJETOS----------------------#

user2 = User(2,'mal1', 'mal2@gmail.com', 'mal2Pass')

#user2.crear_User()

user2.obtener_user()

user2.borrar_User()

#Obtiene todos los datos relacionados a el user, para usar este metodo, debe primero tener registros en user_card y more_data
#user2.all_user_data()


#user2 = User(2,'User02', 'user02@gmail.com', 'user2Password')
#user2.actualizar_User()
