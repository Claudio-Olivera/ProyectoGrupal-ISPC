from Insert_more_Data import insert_more_data
from Select_only_more_data import get_only_more_data
from Update_more_Data import update_more_data

class MoreData:
    def __init__(self, name, lastName, calle,direccion,piso_Depto,ciudad,provincia,telefono,Id_User, Id_more_data ):
        self.name = name
        self.lastName = lastName
        self.calle = calle
        self.direccion = direccion
        self.piso_Depto  = piso_Depto
        self.ciudad = ciudad
        self.provincia = provincia
        self.telefono  = telefono
        self.Id_User = Id_User
        self.Id_more_data = Id_more_data

#crea nuevo registro de datos en la tabla more_data
    def crear_data(self):
        insert_more_data(self)

#obtiene el registro seleccionado por id desde la tabla more_data
    def obtener_data(self):
        get_only_more_data([self.Id_User])

#actualiza el registro de la tabla more_data.
    def actualizar_more_data(self):
            update_more_data(self)

#Esta clase no tiene el metodo borrar/delete, ya que solo puede ser modificada y no se busca eliminarla.

#-----------------INVOCACION DE METODOS Y CREACION DE OBJETOS----------------------#

#data1 = MoreData('Fernanda','Robledo','San Martin','513','','General Roca','Rio Negro','2984788455',2,2)

#data1.crear_data()

#data1.obtener_data()

#data1 = MoreData('Fernanda','Robledo','Alsina','413','','General Roca','Rio Negro','2984788455',2,2)
#data1.actualizar_more_data()


