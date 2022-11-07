from Insert_Admin import insert_admin
from Select_Admin import get_admin
from Delete_Admin import delete_admin
from Update_Admin import update_admin_data


class Admin:

    def __init__(self,Id_Admin,username,email,password):
        self.Id_Admin = Id_Admin
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
        
        #-----------------INVOCACION DE METODOS Y CREACION DE OBJETOS----------------------#
    
#admin1 = Admin(1,'Admin1', 'admin1@gmail.com', 'adminPassword1')

#admin1.crear_Admin()

#admin1.obtener_admin()

#admin1 = Admin(1,'Admin1', 'adminCambio@gmail.com', 'adminPassword1')
#admin1.actualizar_admin()

#admin1.borrar_admin()