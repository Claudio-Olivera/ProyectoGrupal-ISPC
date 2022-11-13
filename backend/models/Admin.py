from controller.Sql_Insert import insert_admin
from controller.Sql_Select import get_admin
from controller.Sql_Delete import delete_admin, delete_all_user_data
from controller.Sql_Update import update_admin_data


class Admin:

    def __init__(self, id_admin, username, email, password):
        self.Id_Admin = id_admin
        self.username = username
        self.email = email
        self.password = password

    def crear_Admin(self):
        insert_admin(self)

    def obtener_admin(self):
        get_admin([self.Id_Admin])

    def borrar_admin(self):
        delete_admin([self.Id_Admin])

    def actualizar_admin(self):
        update_admin_data(self)

    def delete_user(id):
        delete_all_user_data(id)
        # -----------------INVOCACION DE METODOS Y CREACION DE OBJETOS----------------------#

#admin1 = Admin(1, 'Admin1', 'admin1@gmail.com', 'adminPassword1')
#admin1.crear_Admin()
#admin1.obtener_admin()
#admin1 = Admin(1,'Admin1', 'adminCambio@gmail.com', 'adminPassword1')
#admin1.actualizar_admin()
#admin1.borrar_admin()

